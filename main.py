from fastapi import FastAPI
app = FastAPI()
@app.get("/home")
def send_text_to_server():
    return "text"
