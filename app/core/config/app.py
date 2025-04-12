from pydantic import BaseModel


class AppConfig(BaseModel):
    api_prefix: str = "/api"
    app_title: str = "Table Reservation API"
    app_description: str = "Powerful API to reserve tables"
