from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


URL_DATABASE= 'sqlite:///./finance.db'

engine =  create_engine(URL_DATABASE, connect_args={"check_same_thread":False}) 

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
