from dataclasses import dataclass
from typing import List

@dataclass
class Stack:
    id: str
    intermediate_results: List[int]