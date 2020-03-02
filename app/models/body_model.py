from datetime import datetime
from typing import List, Dict
from uuid import UUID
from pydantic import BaseModel


class methods_parm(BaseModel):
    name: str
    type: str
    uid: UUID
    img_url: str
    is_authenticated: str
    contacts: List[Dict[str, str]]
    client_id: UUID
    idcard: Dict[str, str]
    isSubmit: str
    authenticate_time: datetime


class market_parm(BaseModel):
    position: List[float]