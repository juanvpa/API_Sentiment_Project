import sqlalchemy as alch
from getpass import getpass
import dotenv
import os 

dotenv.load_dotenv()

password = os.getenv('sqlpassword')
dbName="Elonmusk_API"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)