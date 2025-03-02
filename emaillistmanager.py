import re
from datetime import datetime 

def display_menu():
    print("\nWelcome to the Email List Manager.")
    print("What would you like to do?")
    print("1. Add Email")
    print("2. Search Email")
    print("3. Show Email List")
    print("4. Quit")

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

    while True: 
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            email = input("Enter your email: ")
            email_manager.add_email(email)
        elif choice == "2":
            query = input("Enter search query: ")
            print("🔍 Search Result: ", email_manager.search_email(query))
        elif choice == "3":
            print("📃 Email List: ", email_manager.show_all())
        elif choice == "4":
            print("GoodBye!")
            break
        else: 
            print("Inavlid Input! Please try again.")

   