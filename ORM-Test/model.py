from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///./MoviesList.db', echo=True)
	#'mysql://root:@localhost:3306/ormPythonDB')

Base = declarative_base()

class Movie(Base):
	__tablename__ = 'Film'
	id = Column(Integer, primary_key = True)
	nameFilm = Column(String(48), nullable = False)
	nameRegista = Column(String(128), nullable = False)
	durata = Column(Integer, nullable = False)


Base.metadata.create_all(engine)