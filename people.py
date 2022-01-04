import re
"""
This function contain one parameter, text, a string representing a single line of the file.
This function uses re to capture the first name and last name
return a tuple
"""
def parse_name(line):
    line = line.split(" ")
    line = [line[0],line[1]]
    return tuple(line)

"""
This function contain one parameter, text, a string representing a single line of the file.
This function uses re to capture street, city and state
return a tuple
"""


def parse_address(line):
    line = line.split(" ")
    street = line [2:-3]
    street = " ".join(street)
    city = line[-3]
    state = line[-2]
    address = [street,city,state]
    return tuple(address)

"""
This function contain one parameter, text, a string representing a single line of the file.
This function uses re to capture email of the person
return the email identified
"""
def parse_email(line):
    email = re.search(r"(\S+?@\S+?.\S+)", line).group()
    return email.strip()

"""
This class have 3 attributes street, city, state
"""
class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

"""
This class have 4 attributes first_name, last_name, address, email
The first_name and last_name attributes are created by calling the parse_name function
The address attribute is created by calling the parse_address function
The  email  attribute  is  created  by  calling  the  parse_email  function
"""
        
class Employee:
    def __init__(self, line):
        self.first_name = parse_name(line) [0]
        self.last_name = parse_name(line) [1]
        street = parse_address(line) [0]
        city = parse_address(line) [1]
        state = parse_address(line) [2]
        self.address = Address(street,city,state)
        self.email = parse_email(line)

"""
An empty list called employee_list is been created
Open up the file from the path
For each line in the file, an instance of employee has been created by passing in the string 
Append the instance to the employee_list.
return
"""
        
def main(new_text):
    employee_list = []
    with open(new_text, "r", encoding="utf-8") as file:
        for line in file:
            num_employee = Employee(line)
            employee_list.append(num_employee)
    
    
    return employee_list
    

"""
Called the main using the "people.txt" file
Print the returned value.
"""

if __name__ == "__main__":
    employee_list = main("people.txt")
    print("Number of emolpyee:", len(employee_list))
    print(employee_list)
    for i in employee_list:
        print("\n\tFirst Name: ",i.first_name)
        print("\tLast Name:  ",i.last_name)
        print("\tAddress:    ",i.address.street)
        print("\tCity:       ",i.address.city)
        print("\tState:      ",i.address.state)
        print("\tEmail:      ",i.email)
