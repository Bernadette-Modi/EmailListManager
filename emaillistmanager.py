import re
from datetime import datetime 

Reg_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called at {datetime.now()}")
        returen func(*args, **kwargs)
    return wrapper

class EmailList:
    def __init__(self):
        self.emails = []
    
    def __iter__(self):
        return iter(self.emails)

    @log
    def add_email(self, *emails):
        """Adds multiple emails to the list after validation"""
        for email in emails:
            if re.fullmatch(Reg_email, email):
                self.emails.append(email)
                print(f"✅ Added: {email}")
            else:
                print(f"❌ Invalid email: {email}")
   