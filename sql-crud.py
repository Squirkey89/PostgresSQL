from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()
# create a class-based model for the "Programmer" table
# class Programmer(base):
#     __tablename__ = "Programmer"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String)
#     nationality = Column(String)
#     famous_for = Column(String)

#     # (Example)
class Place(base):
    __tablename__ = "Favourite Places"
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    country_name = Column(String)
    capital_city = Column(String)
    population = Column(String)
    currency = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()
# creating the database using declarative_base subclass
base.metadata.create_all(db)

#     # (Example)
james_smith = Place(
    full_name="James Smith",
    country_name="England",
    capital_city="London", 
    population="55.98 million",
    currency="British Pound"

)

sean_quirke = Place(
    full_name="Sean Quirke",
    country_name="Ireland",
    capital_city="Dublin", 
    population="5 million",
    currency="Euro"

)

shilpa_shetti = Place(
    full_name="Shilpa Shetti",
    country_name="India",
    capital_city="Delhi", 
    population="1.38 billion",
    currency="Rupee" 

)

josh_burns = Place(
    full_name="Josh Burns",
    country_name="USA",
    capital_city="Washington", 
    population="329.5 million",
    currency="US Dollar"
)

# session.add(james_smith)
# session.add(sean_quirke)
# session.add(shilpa_shetti)
# session.add(josh_burns)


# creating records on our Progammer table
# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     nationality="British",
#     famous_for="First Programmer"
# )
# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="M",
#     nationality="British",
#     famous_for="Modern Computing"
# )
# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     nationality="American",
#     famous_for="COBOL language"
# )
# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="F",
#     nationality="American",
#     famous_for="Apollo 11"
# )
# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="M",
#     nationality="American",
#     famous_for="Microsoft"
# )
# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="M",
#     nationality="British",
#     famous_for="World Wide Web"
# )

# sean_quirke = Programmer(
#     first_name="Sean",
#     last_name="Quirke",
#     gender="M",
#     nationality="Irish",
#     famous_for="Code Institute"
# )

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(sean_quirke)


# updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"


# commit our session to the database
# session.commit()


# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n)")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
# else:
#     print("No records found")


# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )

    # (Example)
places = session.query(Place)
for place in places:
    print(
        place.id,
        place.full_name,
        place.country_name,
        place.capital_city,
        place.currency,
        sep=" | "
  )