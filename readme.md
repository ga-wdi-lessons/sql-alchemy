# SQLAlchemy

## Learning Objectives

- Define ORM and why we use it over a database language.
- Explain what SQLAlchemy is and what problems it solves.
- Explain convention over configuration and how it relates to SQLAlchemy
- Define a class that inherits from SA
- Utilize SA to perform the following CRUD actions on a database
  - create
  - new
  - save
  - all
  - find, find_by
  - where
  - update
  - destroy

- Differentiate between class versus instant methods in Active Record objects/classes

- Utilize has_many, belongs_to to establish associations/relationships with AR
Seed a database using AR

## Framing

So far, you've learned how to interact with a database using SQL.

Specifically, you used postgresql. In today's lesson, we're doing to work with SQLite, which is similar, but distributable via the file system.

## Querying the DB w/ Python

## ORMs

### Doc Dive (5 mins)

Read the following docs

- https://en.wikipedia.org/wiki/Object-relational_mapping
- http://www.sqlalchemy.org/

### Turn and Talk (5 mins)

Now, turn & talk to your neighbor and discuss:

- At a high level, what are ORM's and how might they be useful?
- What is the importance of having an interface between python and the DB?

## SQLAlchemy

### We Do Person model and People Seeds

### You do: NBA Stats Part 1

### Sync Up

### You do: NBA Stats Part 2

##  Relationships

There are many common relationship types within a relational database:

- one to one
  - fiancee has one fiancee
- one to many
  - one class has many students
- many to one
  - one student has many assignments
- many to many
  - one product has many orders
  - one order has many products

### One to Many

A person has many addresses. An address belongs to a person.

#### Person

| id | name |
| --- | --- |
| 6 | Jesse |
| 7 | Scott |

#### Address

| id | street_name | street_number | post_code | person_id |
| --- | --- | --- | --- |--- |
| 1 | 34th Street | 8907 | 21740 | 6 |
| 2 | 15th Street | 1133 | 20002 | 6 |

```python
class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
```

### You do:

Add a Job's model that belongs to a person: `A person has many jobs`

## Joins

### You do: Read

http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#querying-with-joins
http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#building-a-many-to-many-relationship

### You do:

Add a third model "Subject" to the harry potter example

A Student has many Subjects
A Subject has many Students
