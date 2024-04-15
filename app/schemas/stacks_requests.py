from pydantic import BaseModel

class ValueDataRequest(BaseModel):
    value: int