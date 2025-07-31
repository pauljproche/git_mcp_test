from fastapi import FastAPI
from tool import UserRequest, DocumentList, get_user_documents_logic
app = FastAPI()

@app.get("/")
def root():
	return {"message":"Hello Test MCP!"}

@app.post("/get_user_documents", response_model=DocumentList)
def get_user_documents(request: UserRequest):
	return {"documents": get_user_documents_logic(request.user_id)}