from sqlalchemy import create_engine, inspect, exists, MetaData, func, Table, Column, Integer, String, JSON
from sqlalchemy.sql import insert, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import json
import os

load_dotenv()

db = os.getenv("DB")
user = os.getenv("DB_USER")
pwd = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
table = os.getenv("DB_TABLE")

DB_URL = f"postgresql+psycopg2://{user}:{pwd}@host.docker.internal:{port}/{db}"
engine = create_engine(DB_URL)
metadata = MetaData()

inspector = inspect(engine)

Base = declarative_base()

class Boards(Base):
    __tablename__="boards"
    id = Column(Integer, primary_key=True)
    size = Column(String)
    board = Column(JSON)


#Insert the size and the boards like json data
def insert_boards(size, list_p):

    Base.metadata.create_all(engine)

    tables = inspector.get_table_names()

    #print(Boards.__tablename__) 

    Session = sessionmaker(bind=engine)
    session = Session()
    #loop to the list of board and store it!
    for item in list_p:
        try:          
            board = Boards()
            board.size = size   
            board.board = item

            session.add(board)
            session.commit()
        
        except Exception as e:
                session.rollback()
                print(f"Error: {e}")

#This function searches if the solution has already in the database
#the argument is: size of the board
def exist_solutions(n):
    n=str(n)
    Session = sessionmaker(bind=engine)
    session = Session()

    in_table = session.query(exists().where(Boards.size == n)).scalar()

    return in_table

#This function count all possible solutions counting the rows in database 
# according the size of the board
def solutions_count(size_board):

    size_board = str(size_board)

    with engine.connect() as connection:
        t = connection.begin()        
        query = select(func.count()).select_from(Boards).where(Boards.size == size_board)
        result = connection.execute(query)
        d = result.mappings().all()
        return d[0]['count_1']

#Get boards from postgres and return all the possbilities
def get_boards(size):    
    size = str(size)

    with engine.connect() as connection:
        query = select(Boards.board).where(Boards.size == size)
        result = connection.execute(query)
        rows_as_lists = [list(row) for row in result]

        return rows_as_lists



   