import os
import psycopg2

print('Available env vars', os.environ)
db_name = os.environ['DB_NAME']
db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASSWORD']
db_port = os.environ['DB_PORT']
print('Connecting to db', db_name, 'on host', db_host, 'at port', db_port, 'with user', db_user, 'and password length', str(len(db_pass)))
conn = psycopg2.connect(database=db_name,
                        host=db_host,
                        user=db_user,
                        password=db_pass,
                        port=db_port)
print('Successfully connected to client')
conn.close()
print('Exit application')
