from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, House, Student

engine = create_engine('sqlite:///hogwarts.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

gryffindor = House(name="Gryffindor", image_url="http://images1.wikia.nocookie.net/__cb20120922143611/harrypotter/images/7/70/G_final.jpg")
hufflepuff = House(name="Hufflepuff", image_url="http://images3.wikia.nocookie.net/__cb20111027164827/harrypotter/images/3/3f/H_final.jpg")
ravenclaw = House(name="Ravenclaw", image_url="http://images2.wikia.nocookie.net/__cb20111021043857/harrypotter/images/d/da/R_final.jpg")
slytherin = House(name="Slytherin", image_url="http://images3.wikia.nocookie.net/__cb20111027165214/harrypotter/images/d/da/S_final.jpg")
session.add(gryffindor)
session.add(hufflepuff)
session.add(ravenclaw)
session.add(slytherin)
session.commit()

harry = Student(name="Harry Potter", image_url="http://images1.wikia.nocookie.net/__cb20111110202524/harrypotter/images/thumb/d/d4/Dhharryroomhighreso.jpg/250px-Dhharryroomhighreso.jpg", house=gryffindor)
ron = Student(name="Ron Weasley", image_url="http://images4.wikia.nocookie.net/__cb20090712085217/harrypotter/images/9/99/Ron_DH.PNG", house=gryffindor)
hermione = Student(name="Hermione Granger", image_url="http://images2.wikia.nocookie.net/__cb20120512155742/harrypotter/images/thumb/9/95/DeathlyPromo_Hermione.PNG/250px-DeathlyPromo_Hermione.PNG", house=gryffindor)
luna = Student(name="Luna Lovegood", image_url="http://images1.wikia.nocookie.net/__cb20101113121321/harrypotter/images/thumb/4/49/Luna_profile.jpg/250px-Luna_profile.jpg", house=ravenclaw)
cho = Student(name="Cho Chang", image_url="http://images3.wikia.nocookie.net/__cb20081103140303/harrypotter/images/thumb/c/c1/Cho_Chang_Profile.JPG/250px-Cho_Chang_Profile.JPG", house=ravenclaw)
cedric = Student(name="Cedric Diggory", image_url="http://images1.wikia.nocookie.net/__cb20111015180906/harrypotter/images/thumb/c/c5/Cedric.jpg/250px-Cedric.jpg", house=hufflepuff)
draco = Student(name="Draco Malfoy", image_url="http://images1.wikia.nocookie.net/__cb20100925140918/harrypotter/images/thumb/2/21/Dracodh.jpg/250px-Dracodh.jpg", house=slytherin)
pansy = Student(name="Pansy Parkinson", image_url="http://images1.wikia.nocookie.net/__cb20110801070343/harrypotter/images/thumb/6/62/Pansyinfobox.jpg/250px-Pansyinfobox.jpg", house=slytherin)

session.add(harry)
session.add(ron)
session.add(hermione)
session.add(luna)
session.add(cho)
session.add(cedric)
session.add(draco)
session.add(pansy)
session.commit()

import code; code.interact(local=dict(globals(), **locals()))
