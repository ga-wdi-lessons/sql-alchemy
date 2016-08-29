from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

Base = declarative_base()
engine = create_engine('sqlite:///player.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Player(Base):
  __tablename__ = 'player'
  id = Column(Integer, primary_key=True)
  name = Column(String(250))
  age = Column(Integer)
  team = Column(String(250))
  game = Column(Integer)
  points = Column(Integer)

  def __repr__(self):
    return "Player(id=%r,name=%r,age=%r,team=%r,game=%r,points=%r)" % (self.id,self.name, self.age, self.team, self.game, self.points)

Base.metadata.create_all(engine)

with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
	session.add(Player(name=row[0],age=row[1],team=row[2],game=row[3],points=row[4]))
	session.commit()

import code; code.interact(local=dict(globals(), **locals()))

