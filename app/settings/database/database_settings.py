from pydantic import Field, PostgresDsn

from app.settings.base import Settings


class DatabaseSettings(Settings):
    DATABASE_USERNAME: str = Field(default="postgres")
    DATABASE_PASSWORD: str = Field(default="postgres")
    DATABASE_PORT: int = Field(default=5432)
    DATABASE_HOST: str = Field(default="localhost")
    DATABASE_NAME: str = "postgis3"

    def dsn(self) -> str:
        url = PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.DATABASE_USERNAME,
            password=self.DATABASE_PASSWORD,
            host=self.DATABASE_HOST,
            path=f"{self.DATABASE_NAME}",
            port=self.DATABASE_PORT,
        )
        return str(url)
