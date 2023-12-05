from fastapi import FastAPI

app = FastAPI()

@app.get('/firstAPI')
def fastapi_url():
    return {'message': 'This is first API'}