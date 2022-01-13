from pydantic import BaseSettings


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_name: str
    db_port: int

    @property
    def db_url(self):
        return f"postgresql://{self.db_username}:{self.db_password}@db:{self.db_port}/{self.db_name}"
        # return "sqlite:////home/kaique/Projects/test/mini_ecomerce_clean/database.db"


settings = Settings()
