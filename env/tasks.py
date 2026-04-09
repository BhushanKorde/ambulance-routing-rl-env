TASKS = {
    "easy": {
        "description": "Nearby patient, low traffic, clear route",
        "start": "A",
        "patient_location": "B",
        "hospitals": ["H1"],
        "traffic": {
            ("A", "B"): 0.2,
            ("B", "H1"): 0.3
        },
        "optimal_time": 5
    },

    "medium": {
        "description": "Multiple route choices with moderate traffic",
        "start": "A",
        "patient_location": "C",
        "hospitals": ["H1", "H2"],
        "traffic": {
            ("A", "B"): 0.5,
            ("B", "C"): 0.6,
            ("A", "C"): 0.8,
            ("C", "H1"): 0.4,
            ("C", "H2"): 0.7
        },
        "optimal_time": 8
    },

    "hard": {
        "description": "Critical patient, high traffic, must optimize route + hospital",
        "start": "A",
        "patient_location": "D",
        "hospitals": ["H1", "H2"],
        "traffic": {
            ("A", "B"): 0.9,
            ("B", "C"): 0.8,
            ("C", "D"): 0.7,
            ("A", "D"): 1.2,
            ("D", "H1"): 0.9,
            ("D", "H2"): 0.4
        },
        "optimal_time": 10
    }
}