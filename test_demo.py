from fastapi import FastAPI
from fastapi.testclient import TestClient

demo_app = FastAPI()
demo_test_client = TestClient(demo_app)


@demo_app.get("/")
def demo_home():
    return {"message": "Hello Demo!"}


client = TestClient(demo_app)
def test_demo_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Demo!"}