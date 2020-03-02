from typing import Dict

from pydantic import BaseModel


class market_response(BaseModel):
    result: Dict[str, str]
