# Q - You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.
#
# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

response = int(input("Enter the API Response Code: "))

# Check if the response is successful
if response == 400:
    print("O/P ❌ Failed API Request")
elif response == 200:
    print("O/P ✅ Passed API Request")