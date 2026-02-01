def outer_function():
    var1 = 30

    def inner_function():
        var2 = 40
        print(var1, var2)

    def inner_function2():
        print(var1)

    inner_function()
    inner_function2()

outer_function()
