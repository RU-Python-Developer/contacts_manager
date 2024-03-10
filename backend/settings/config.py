from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    TESTING: bool = False
    HOST: list = [
        "http://localhost",
        "http://localhost:4200",
    ]
    DB_HOST: str = "db"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "Ngeom0booyae2hi7quuo8oonohxahVohzooja6"
    DB_NAME: str = "postgres_db"


settings = Settings()
