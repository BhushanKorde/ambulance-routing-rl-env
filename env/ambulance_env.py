import random
from .models import AmbulanceState, AmbulanceAction, AmbulanceObservation
from .tasks import TASKS

class AmbulanceEnv:

    def __init__(self, task="easy"):
        self.task_name = task
        self.task = TASKS[task]
        self.max_steps = 8
        self.current_step = 0
        self.done = False
        self.state = None
        self.current_location = self.task["start"]
        self.has_patient = False  # ✅ NEW

    def reset(self):
        self.current_step = 0
        self.done = False
        self.current_location = self.task["start"]
        self.has_patient = False  # ✅ RESET

        self.state = AmbulanceState(
            location=self.current_location,
            traffic_level=0.5,
            patient_severity=random.uniform(0.5, 1.0),
            hospitals=self.task["hospitals"],
            time_elapsed=0.0
        )

        return {
            "observation": AmbulanceObservation(
                message=f"Emergency! Reach patient at {self.task['patient_location']}",
                state=self.state
            ),
            "reward": 0.0,
            "done": False,
            "info": {}
        }

    def step(self, action: AmbulanceAction):

        if self.done:
            return self.reset()

        self.current_step += 1

        from_loc = self.current_location
        to_loc = action.next_location

        edge = (from_loc, to_loc)

        # 🚀 GRAPH-BASED MOVEMENT
        if edge in self.task["traffic"]:
            traffic = self.task["traffic"][edge]
            travel_time = random.uniform(1, 3) * (1 + traffic)
        else:
            # invalid move penalty
            travel_time = 5.0

        self.state.time_elapsed += travel_time
        self.current_location = to_loc
        self.state.location = to_loc

        # 🎯 GOAL CHECK
        reached_patient = (to_loc == self.task["patient_location"])
        reached_hospital = (to_loc in self.task["hospitals"])

        # 🎯 BASE REWARD
        reward = 1 / (1 + self.state.time_elapsed)

        # ✅ PATIENT PICKUP
        if reached_patient and not self.has_patient:
            self.has_patient = True
            reward += 0.2

        # ✅ HOSPITAL ONLY AFTER PATIENT
        if reached_hospital and self.has_patient:
            reward += 0.3
            self.done = True

        # ❌ PENALTY: hospital without patient
        if reached_hospital and not self.has_patient:
            reward *= 0.5

        # 🚨 HARD TASK BONUS
        if self.task_name == "hard":
            reward *= self.state.patient_severity

        # ✅ SAFE CLAMP
        reward = max(0.01, min(reward, 0.99))

        # max step end
        if self.current_step >= self.max_steps:
            self.done = True

        return {
            "observation": AmbulanceObservation(
                message=f"Moved to {to_loc}",
                state=self.state
            ),
            "reward": reward,
            "done": self.done,
            "info": {}
        }

    def state_fn(self):
        return self.state