class Employee:
    def __init__(self, last=None, first=None, email=None):
        if email == None:
            self.last = input("Last ")
            self.first = input("First ")
            self.email = input("email ")
        else:
            self.last = last
            self.first = first
            self.email = email

    def __str__(self):
        return "Last: " + self.last + "\nFirst: " + self.first + "\nEmail: "\
               + self.email

    def __lt__(self, other):
        if (self.last < other.last) or\
            (self.last == other.last) and (self.first < other.first):
            return True
        else:
            return False

def menu():
    print("1. Add employee\n2. List employees\n3. Quit")
    choice = input("Please type in your choice")
    try:
        choice = int(choice)
        if not (1 <= choice <= 3):
            choice = menu()
    except ValueError:
        choice = menu()
    return choice

choice = menu()
employees = []

while choice != 3:
    if choice == 1:
        employees.append(Employee())
    elif choice == 2:
        employees.sort()
        for employee in employees:
            print(employee)
    choice = menu()
