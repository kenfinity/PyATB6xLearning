def add_security(test):
    def wrapper():
        print("1.Before the function is called")
        print("2.Add Helmet, Dashcam, gloves, knee guard, License")
        test()
        print("3.After the function is called")
        print("4.secure driving")
    return wrapper()


@add_security
def drive_ola_scooter():
    print("Driving ola scooter")

print()

@add_security
def drive_kawasaki_ninja():
    print("Driving kawasaki ninja")