from fastapi import FastAPI
from env.ambulance_env import AmbulanceEnv
from env.models import AmbulanceAction

app = FastAPI()

env = AmbulanceEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: AmbulanceAction):
    return env.step(action)

@app.get("/state")
def state():
    return env.state_fn()