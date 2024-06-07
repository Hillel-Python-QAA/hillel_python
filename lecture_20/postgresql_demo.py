import psycopg2


# DB Parameters
dbname = 'my_db'
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'

try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    print('Connected to the db {} successfully!'.format(dbname))

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees;")

    record = cursor.fetchall()
    print("You are connected to - {}".format(record))

    cursor.execute("DELETE FROM employees WHERE name = 'Bob';")
    cursor.execute("SELECT * FROM employees;")

    record = cursor.fetchall()
    print("You are connected to - {}".format(record))

    connection.commit()

except (Exception, psycopg2.Error) as error:
    print('Error while connecting to PostgreSQL', error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
