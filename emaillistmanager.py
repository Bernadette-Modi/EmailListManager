import re
from datetime import datetime 

def display_menu():
    print("\nWelcome to the Email List Manager.")
    print("What would you like to do?")
    print("1. Add Email")
    print("2. Search Email")
    print("3. Show Email List")

Reg_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__} called at {datetime.now()}")
        return func(*args, **kwargs)
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
    
    @log
    def search_email(self, query):
        """Searches for emails containing a given query"""
        found_emails = list(filter(lambda e: query in e, self.emails))
        return found_emails if found_emails else "No matches found."

    @log
    def show_all(self):
        """Displays all stored emails."""
        return self.emails if self.emails else "No emails stored."

if __name__ == "__main__":
    email_manager = EmailList()

    display_menu()
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        add_email()
    elif choice == "2":
        search_email()
    elif chice == "3":
        show_all()
    else: 
        print("Inavlid Input! Please try again.")

    email_manager.add_email(input("Enter your email please: "))
    print("🔍 Search Result: ", email_manager.search_email("example"))
    print("📃 Email List: ", email_manager.show_all())