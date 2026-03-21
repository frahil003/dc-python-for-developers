from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root(name: str = "Susi"):
    return {"message 1": "Hello World",
            "message 2": f"Hello {name}"}

# >>> curl localhost:8000

