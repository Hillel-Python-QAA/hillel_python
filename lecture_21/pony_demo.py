from pony.orm import Required, Set, Database, db_session

db = Database()
db.bind(
    provider="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    database="my_db",
    port="5432",
)



class Departments(db.Entity):
    name = Required(str)
    employee = Set("Employee")


class Employee(db.Entity):
    name = Required(str)
    department_id = Required("Departments")


db.generate_mapping(create_tables=True)  # create tables


@db_session
def add_employee():
    devops_dep = Departments(name="DevOps")
    john2 = Employee(name="John2", department_id=devops_dep)
    db.commit()


add_employee()


with db_session:
    Employee(name="Kate", department_id=Departments(name="Sales"))
    db.commit()
