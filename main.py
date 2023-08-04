from flask import Flask, request
import db
import atexit

app = Flask(__name__)
connection = db.get_connection()

@app.route('/')
def hello():
    lattitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    # Distance is calculated using Haversine formula
    query = """
        select 
            subquery.id, subquery.name, subquery.latitude, subquery.longitude
        from (
            select 
                *, 
                acos(sin(latitude/57.3) * sin(%s/57.3) + cos(latitude/57.3) * cos(%s/57.3) * cos(%s/57.3-longitude/57.3)) * 6371 as km 
                from restaurant_branches
        ) as subquery
        where km <= 10
        order by km asc
        limit 5
        """
    result = db.execute_query(connection, query, [lattitude, lattitude, longitude])
    return result

def cleanup():
    db.close_connection(connection)
atexit.register(cleanup)

if __name__ == "__main__":
    app.run(debug=False)