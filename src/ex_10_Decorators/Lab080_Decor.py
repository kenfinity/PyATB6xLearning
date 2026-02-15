def before_after_ui_test(driver):
    def wrapper():
        print("before running UI Code")
        driver()
        print("after running UI Code")
    return wrapper()


@before_after_ui_test
def test_ui():
    print("UI Test")