import time

def print_logs(func):
    def wrapper():
        print("Start of the logs")
        func()
        print("End of the logs")
    return wrapper

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("start_time = ", start_time)
        func()
        end_time = time.time()
        print("end_time = ", end_time)
        print("Total time: ", end_time - start_time)
    return wrapper

@print_logs
@time_decorator
def test_ui_1():
    print("Add a function, time taken by  the function 1")
    time.sleep(2)

@print_logs
@time_decorator
def test_ui_2():
    print("Add a function, time taken by  the function 2")
    time.sleep(5)

test_ui_1()
test_ui_2()



# Start of the logs
# start_time
# Add a function, time taken by  the function 1
# end_time
# Total time
# End of the logs
# start_time
# Add a function, time taken by  the function 2
# end_time
# Total time
# End of the logs
