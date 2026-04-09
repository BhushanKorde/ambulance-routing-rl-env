from fastapi import FastAPI
import uvicorn

from env.ambulance_env import AmbulanceEnv
from env.models import AmbulanceAction

app = FastAPI()
env = AmbulanceEnv(task="easy")


@app.post("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(action: dict):
    act = AmbulanceAction(**action)
    return env.step(act)


@app.get("/state")
def state():
    return env.state_fn()


# ✅ REQUIRED FOR OPENENV
def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)


# ✅ REQUIRED ENTRYPOINT
if __name__ == "__main__":
    main()
