import re
from datetime import datetime 

email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called at {datetime.now()}")
        returen func(*args, **kwargs)
    return wrapper