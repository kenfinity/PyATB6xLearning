def display_information(name, role):
    print("Name: ",name,"\b,", "Role: ",role)
    print(f"Name: {name}, Role: {role}")


display_information("Pramod","QA")

# Better Version - location does not matter as long as you give a name for the arugment
display_information(name="Pramod1", role="QA1")
display_information(role="QA3", name="Pramod3")