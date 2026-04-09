from pydantic import BaseModel
from typing import List

class AmbulanceState(BaseModel):
    location: str
    traffic_level: float
    patient_severity: float
    hospitals: List[str]
    time_elapsed: float

class AmbulanceAction(BaseModel):
    next_location: str
    hospital_choice: str

class AmbulanceObservation(BaseModel):
    message: str
    state: AmbulanceState