import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class House(Base):
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    image_url = Column(String(250))
    students = relationship("Student",backref="student")

    def __repr__(self):
        return "House(id=%r,name=%r,image_url=%r)" % (self.id, self.name, self.image_url)

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    image_url = Column(String(250))
    house_id = Column(Integer, ForeignKey('house.id'))
    house = relationship(House)

engine = create_engine('sqlite:///hogwarts.db')
Base.metadata.create_all(engine)
