from pydantic import BaseModel
from datetime import datetime

class Invoice(BaseModel):
    number : int
    id : int
    period : int
    date: datetime
    description : str
    amount : float
    expiration : datetime
    status : str

class Payments(BaseModel):
    id_user : str
    payments : list[Invoice]
    last_updated : datetime