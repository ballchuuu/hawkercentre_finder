from pydantic import BaseSettings

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
