# 🚑 Emergency Ambulance Routing RL Environment (OpenEnv)

## 📌 Overview

This project implements a **real-world Reinforcement Learning (RL) environment** using the **OpenEnv framework**, designed for deployment on **Hugging Face Spaces (Docker)**.

The environment simulates an **Emergency Ambulance Routing System**, where an AI agent must:

* Navigate through traffic
* Select optimal routes
* Choose the best hospital
* Minimize response time
* Maximize patient survival probability

---

## 🌍 Real-World Relevance

Ambulance routing is a critical real-world problem in smart cities and healthcare systems. This environment models:

* 🚦 Dynamic traffic conditions
* 🧑‍⚕️ Patient severity levels
* 🏥 Hospital availability

It is suitable for:

* RL research
* LLM agent evaluation
* Real-world decision-making simulations

---

## ⚙️ OpenEnv API Support

This environment fully implements the OpenEnv specification:

* `reset()` → Initializes environment
* `step(action)` → Executes agent action
* `state()` → Returns current state

---

## 🧠 Observation Space

```json
{
  "location": "string",
  "traffic_level": "float (0-1)",
  "patient_severity": "float (0-1)",
  "hospitals": ["H1", "H2"],
  "time_elapsed": "float"
}
```

---

## 🎮 Action Space

```json
{
  "next_location": "string",
  "hospital_choice": "string"
}
```

---

## 🏆 Reward Function

Reward is based on efficiency of routing:

```
reward = 1 / (1 + time_elapsed)
```

### Key Features:

* Continuous reward (not sparse)
* Penalizes poor decisions
* Encourages faster delivery

### ⚠️ Important (Phase 2 Compliance)

All rewards and scores are strictly clipped:

```
0.01 ≤ reward ≤ 0.99
```

👉 Ensures scores are always within **(0,1)** (required for validation)

---

## 🧪 Tasks

### ✅ Easy

* Low traffic
* Stable patient
* Simple routing

### ⚖️ Medium

* Moderate traffic
* More decision complexity

### 🔥 Hard

* High traffic
* Critical patient condition
* Requires optimal strategy

---

## 🧮 Grading System

Each task uses a deterministic grader:

```
score = 1 / (1 + total_time)
```

Clipped to:

```
0.05 ≤ score ≤ 0.95
```

✔ No binary scoring
✔ No 0.0 or 1.0 values
✔ Fully OpenEnv compliant

---

## 📁 Project Structure

```
ambulance-routing-rl-env/
│
├── Dockerfile
├── openenv.yaml
├── inference.py
├── requirements.txt
├── README.md
│
├── env/
│   ├── models.py
│   ├── ambulance_env.py
│   ├── tasks.py
│   ├── graders.py
│
├── server/
│   ├── app.py
```

---

## 🚀 Running Locally

### 1. Create Virtual Environment

```
python -m venv venv
```

### 2. Activate

Windows:

```
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Server

```
uvicorn server.app:app --host 0.0.0.0 --port 7860
```

Open:

```
http://127.0.0.1:7860/docs
```

---

## 🐳 Docker (Hugging Face Ready)

### Build

```
docker build -t ambulance-env .
```

### Run

```
docker run -p 7860:7860 ambulance-env
```

---

## 🌐 Hugging Face Deployment

1. Create a new **Hugging Face Space**
2. Select **SDK: Docker**
3. Upload or connect this repository
4. Wait for build completion

### Test Endpoint:

```
POST /reset
```

👉 Must return HTTP 200 for validation

---

## 🤖 Inference Script

The `inference.py` script:

* Uses OpenAI client
* Runs agent in environment
* Outputs structured logs:

```
[START]
[STEP]
[END]
```

✔ Fully compliant with evaluation format
✔ Produces reproducible scores

---

## ✅ Validation Checklist

* ✔ Dockerfile in root
* ✔ `/reset` endpoint working
* ✔ OpenEnv spec implemented
* ✔ 3 tasks with graders
* ✔ Scores strictly within (0,1)
* ✔ inference.py in root
* ✔ HF Space deploys successfully

---

## ⚡ Future Improvements

* Real road network graph (nodes + edges)
* Dynamic traffic simulation
* Multi-ambulance coordination
* Integration with real-world map data

---

## 👨‍💻 Author

**Bhushan Korde**

---

## 🏁 License

MIT License.
