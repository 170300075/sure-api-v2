from pydantic import BaseModel
from datetime import datetime

class Payment(BaseModel):
    number : int
    id : int
    period : int
    date: datetime
    description : str
    amount : float
    expiration : datetime
    status : str

class PaymentsList(BaseModel):
    id_user : str
    payments : list[Payment]
    last_updated : datetime