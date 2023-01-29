from pydantic import BaseModel, Field


class Config(BaseModel):
    host: str = Field("0.0.0.0", const=True)
    port: int = Field(8080, const=True, ge=1, le=65535)


CONFIG = Config()
