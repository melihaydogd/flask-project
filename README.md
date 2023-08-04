# Starting the Application

Python 3.9.0 is used.

Create a PostgreSQL database in docker using following command.

```console
docker run -d -p 5432:5432 \
    --restart unless-stopped \
    --name postgres \
    -e POSTGRES_USER=user \
    -e POSTGRES_PASSWORD=password \
    -v postgresdata:/var/lib/postgresql/data \
    postgres:15.3-alpine
```

Create a database in default postgres database using following command.

```sql
create table "restaurant_branches" (
	"id" serial,
	"name" varchar(100),
	"lattitude" DOUBLE PRECISION,
	"longitude" DOUBLE PRECISION,
	primary key (id)
);
insert into public.restaurant_branches ("name", "latitude", "longitude") values ('pizza1', 40.9712703682321, 29.113750852693887);
insert into public.restaurant_branches ("name", "latitude", "longitude") values ('pizza2', 40.98500189082511, 29.063956361768913);
insert into public.restaurant_branches ("name", "latitude", "longitude") values ('pizza3', 39.095099567828015, 29.11592641811334);
```

Install requirements and start the python application.

```console
pip install -r requirements.txt
python main.py
```

You can use following request to make a GET request.

```console
curl --location 'http://localhost:5000?latitude=40.97088962750314&longitude=29.11279602202339'
```
