from fastapi import APIRouter, HTTPException, status, Depends
from app.services.database_service import *
from app.services.rpn_services import *
from app.schemas.stacks_requests import *

router = APIRouter()

db_service = None
rpn_service = None

async def build():
    global rpn_service
    rpn_service = RpnService()
    global db_service
    db_service = DatabaseService()
    
async def get_rpn_service():
    return rpn_service

async def get_db_service():
    return db_service

@router.post("/rpn/stack/")
async def create_stack(db = Depends(get_db_service)):
    id = await db.create_stack()
    return {"result": id}

@router.post("/rpn/op/{op}/stack/{stack_id}")
async def apply_operand(op: str, stack_id: int, db = Depends(get_db_service), rpn = Depends(get_rpn_service)):
    stack = await db.get_stack(stack_id)
    result = await rpn.run(stack, op)
    return {"result" : result}

@router.post("/rpn/stack/{stack_id}")
async def push_value(stack_id: int, data: ValueDataRequest, db = Depends(get_db_service)):
    await db.push_value(stack_id, data.value)
    return {"Status": "Success"}

@router.get("/rpn/stack/{stack_id}")
async def get_stack(stack_id: int, db = Depends(get_db_service)):
    stack = await db.get_stack(stack_id)
    return {"result": stack}