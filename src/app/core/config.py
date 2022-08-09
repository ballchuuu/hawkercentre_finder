from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    ###
    # Logging
    ##
    log_level: str = "INFO"

    ###
    # Sqlite database
    ###
    database_name: str = "app//core//sqlite//database.db"
    hawkercentre_table_name = "hawkercentre"


settings = Settings()
