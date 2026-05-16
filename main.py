from fastapi import FastAPI
app = FastAPI()
@app.post("/home")
def send_text_to_server():
    return "text"