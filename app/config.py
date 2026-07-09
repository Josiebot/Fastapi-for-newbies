from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    
    # class Config:
    #     env_file = ".env"
   
    model_config = SettingsConfigDict(
        env_file=".env",
       env_file_encoding="utf-8"

        
    )

    # database_password:str = "localhost"
   
    # database_username:str = "postgres"
    # secret_key:str = "2u393udbs"


settings = Settings()

