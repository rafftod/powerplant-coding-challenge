from pydantic import BaseModel, Field


class Fuels(BaseModel):
    gas: float = Field(alias="gas(euro/MWh)")
    kerosine: float = Field(alias="kerosine(euro/MWh)")
    co2: float = Field(alias="co2(euro/ton)")
    wind: float = Field(alias="wind(%)")


class Powerplant(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: float
    pmax: float


class ProblemPayload(BaseModel):
    load: int
    fuels: Fuels
    powerplants: list[Powerplant]
