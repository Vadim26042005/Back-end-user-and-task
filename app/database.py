from datetime import datetime

mock_users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]
mock_tasks = [
    {"id": 1, "name": "Complete report", "created_at": datetime(2024, 10, 28, 14, 30), "user_id": 1, "duration": "2h"},
    {"id": 2, "name": "Review budget", "created_at": datetime(2024, 10, 28, 15, 0), "user_id": 2, "duration": "1.5h"},
    {"id": 3, "name": "Update roadmap", "created_at": datetime(2024, 10, 28, 16, 0), "user_id": 1, "duration": "3h"},
    {"id": 4, "name": "Plan marketing campaign", "created_at": datetime(2024, 10, 29, 10, 0), "user_id": 3, "duration": "2h"},
]