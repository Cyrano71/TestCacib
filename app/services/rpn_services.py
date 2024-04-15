from app.database.models.stack import Stack

class RpnService:
    _operators = {'+' : lambda a,b : a + b,
                '-' : lambda a,b : a - b,
                '*' : lambda a,b : a * b,
                '/' : lambda a,b : a // b}
    
    async def get_operands(self):
        return self._operators.keys()

    async def run(self, stack: Stack, operand: str):
        result = self._operators[operand](stack.intermediate_results.pop(), stack.intermediate_results.pop())
        stack.intermediate_results.append(result)
        return result