from starlette.testclient import TestClient
from unittest.mock import  ANY, AsyncMock
from app.database.models.stack import *
from app.services.rpn_services import *
from app.routers.stacks import get_db_service, get_rpn_service
from main import app

testing_db = AsyncMock()

def get_testing_db():
    return testing_db 

def get_testing_rpn():
    return RpnService()

app.dependency_overrides[get_db_service] = get_testing_db
app.dependency_overrides[get_rpn_service] = get_testing_rpn

client = TestClient(app)

def test_create_stack():
    testing_db.reset_mock()
    stack_id = 100
    testing_db.create_stack.return_value = stack_id
    response = client.post(f'/rpn/stack/')
    assert response.status_code == 200
    assert response.json()["result"] == stack_id
    testing_db.create_stack.assert_called_once()

def test_get_stack():
    testing_db.reset_mock()
    stack_id = 1
    testing_db.get_stack.return_value = Stack(stack_id, [2,3])
    response = client.get(f'/rpn/stack/{stack_id}')
    assert response.status_code == 200
    stack = response.json()["result"]
    assert stack["id"] == stack_id
    assert stack["intermediate_results"] == [2,3]
    testing_db.get_stack.assert_called_once_with(stack_id)

def test_apply_operand():
    testing_db.reset_mock()
    stack_id = 150
    op = '+'
    testing_db.get_stack.return_value = Stack(stack_id, [2,3])
    response = client.post(f'/rpn/op/{op}/stack/{stack_id}')
    assert response.status_code == 200
    assert response.json()["result"] == 5
    testing_db.get_stack.assert_called_once_with(stack_id)