from datetime import datetime

from pydantic import (
    BaseModel,
    Field,
    PositiveInt,
    ConfigDict,
)


class ReservationBase(BaseModel):
    customer_name: str = Field(
        min_length=2,
        max_length=55,
    )
    reservation_time: datetime = Field(examples=["2032-04-23T10:20:30.400"])
    duration_minutes: PositiveInt

    table_id: int = Field(examples=[1])


class ReservationCreate(ReservationBase):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
    )

class ReservationRead(ReservationBase):
    id: int

class ReservationDelete(ReservationBase):
    id: int
