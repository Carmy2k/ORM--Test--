from sqlalchemy.orm import sessionmaker
from model import Movie, engine

Session = sessionmaker(bind = engine)

session = Session()

session.add(Movie(nameFilm ='AAS', nameRegista ='', durata =120))
session.add(Movie(nameFilm ='CCC', nameRegista ='', durata =120))
session.add(Movie(nameFilm ='sdfsdfsdf', nameRegista ='', durata =120))
session.add(Movie(nameFilm ='asdasd', nameRegista ='', durata =120))
session.add(Movie(nameFilm ='wqeq', nameRegista ='', durata =120))
session.commit()

print(session.query(Movie).all()[0].nameFilm)