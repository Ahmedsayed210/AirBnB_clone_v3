import os
from sqlalchemy import create_engine

# Set up the engine using environment variables
engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}'.format(
    os.getenv('HBNB_MYSQL_USER'),
    os.getenv('HBNB_MYSQL_PWD'),
    os.getenv('HBNB_MYSQL_HOST'),
    os.getenv('HBNB_MYSQL_DB')))
