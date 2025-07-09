from fastapi import FastAPI , Request
from langchain_google_genai import ChatGoogleGenerativeAI
import uvicorn
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

chat_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.0
)

@app.get("/")
async def get_healthcheck():
    return {"status": "ok"}

@app.post("/v1/chat/completion")
async def get_posthealthcheck(request: Request):
    body = await request.json()
    response = chat_model.invoke(body['query'])
    return {
        "message": "Success",
        "data": response.content
    }

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)