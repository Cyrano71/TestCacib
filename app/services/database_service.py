from app.database.models.stack import Stack

class DatabaseService:
    _stacks: dict[str, Stack]
    _fake_db_id = 0

    def __init__(self) -> None:
       self._stacks = {}

    async def create_stack(self):
        self._stacks[self._fake_db_id] = Stack(self._fake_db_id, list())
        self._fake_db_id += 1
        return self._fake_db_id - 1

    async def delete_stack(self, id:int):
        del self._stacks[id]
        self._fake_db_id -= 1

    async def get_stack(self, id: int):
        return self._stacks[id]

    async def push_value(self, id: int, value: int):
        self._stacks[id].intermediate_results.append(value)