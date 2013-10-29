import psycopg2

conn = psycopg2.connect("dbname=testdb user=postgres")

cur = conn.cursor()

cur.execute("CREATE TABLE employee (id serial PRIMARY KEY, fname varchar, lname varchar, age integer);")

cur.execute("INSERT INTO employee (fname, lname, age) VALUES (%s, %s, %s)", ("Mac", "Mohan", 20))

cur.execute("SELECT * FROM employee;")

cur.fetchone()

cur.close()

conn.close()