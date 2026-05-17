

# sqlalchemy-orm comparing with Sql queries

## sql-alchemy-orm

SQLAlchemy ORM is a Python library that is used to interact with databases through Python code instead of SQL queries.

## sql-alchemy

A Python SQL toolkit and Object Relational Mapper (ORM) for working with databases.



# Queries-comparison

## sqlalchemy-orm

db.query(Employee)

## Sql queries

SELECT * FROM employee;


## sqlalchemy-orm

db.query(Employee).filter(Employee.id == employee_id).first()

## Sql queries

SELECT * FROM employee WHERE id = employee_id;


## sqlalchemy-orm

db.query(Employee).filter(Employee.phone == phone).first()

## Sql queries

SELECT * FROM employee WHERE phone = phone;


## sqlalchemy-orm

db.delete(employee)
db.commit()

## Sql queries

DELETE FROM employee WHERE id = :employee_id;


## sqlalchemy-orm

employee = db.query(Employee).filter(Employee.id == "1").first()
print(employee)

## Sql queries

SELECT * FROM employee WHERE id = "1";



## sqlalchemy-orm

employee = db.query(Employee).filter(Employee.phone == "9876543210").first()
print(employee)

## Sql queries

SELECT * FROM employee WHERE phone = "9876543210";



## sqlalchemy-orm

employee = db.query(Employee).filter(Employee.id == "1").first()

if employee:
    db.delete(employee)
    db.commit()
    print("Employee deleted successfully")

## Sql queries

DELETE FROM employee WHERE id = "1";


## why .first() is used?

.first() is used to get the first result from the query. It is used to get the first result from the query. It is used to get the first result from the query. It is used to get the first result from the query.

## why .all() is used?

.all() is used to get all the results from the query. It is used to get all the results from the query. It is used to get all the results from the query. It is used to get all the results from the query.

## why .delete() is used?

.delete() is used to delete the result from the query. It is used to delete the result from the query. It is used to delete the result from the query. It is used to delete the result from the query.


## why .commit() is used?

.commit() is used to commit the transaction. It is used to commit the transaction. It is used to commit the transaction. It is used to commit the transaction.

## why .rollback() is used?

.rollback() is used to rollback the transaction. It is used to rollback the transaction. It is used to rollback the transaction. It is used to rollback the transaction.

