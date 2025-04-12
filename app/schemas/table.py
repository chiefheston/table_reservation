from pydantic import (
    BaseModel,
    Field,
    PositiveInt,
    ConfigDict,
)


class TableBase(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=55,
    )
    seats: PositiveInt
    location: str = Field(
        ...,
        min_length=2,
        max_length=140,
    )


class TableCreate(TableBase):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
    )


class TableRead(TableBase):
    id: int


class TableDelete(TableBase):
    id: int
