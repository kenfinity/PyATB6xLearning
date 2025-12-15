# An API sometimes fails due to network delays.
# Write a program to retry the API call 3 times until the response code becomes 200.

# If it still fails after 3 tries, print a failure message.

# Hint: Use a while loop with a counter.
# Hint: Use a while loop with a counter.

# Expected Output Example:

# Attempt 1: Response 500

# Attempt 2: Response 200

# ✅ Test Passed

# count = 0
# while count < 3:
#     response = int(input("Enter response code "))
#     if response == 500:
#         print("500 Internal Server Error")
#     elif response == 400:
#         print("400 Page not found Error")
#     elif response == 200:
#         print("200 OK")
#         break
#     count += 1

#***************************
import random   # Simulating an API response (remove this in real use)

attempt = 1
max_attempts = 3

response_code = 0

while attempt <= max_attempts:
    # Simulate an API call using a random response (replace this with real API code)
    # response_code = int(input("Enter the response code: "))
    response_code = random.choice([200, 500, 404, 503])

    print(f"Attempt {attempt}: Response {response_code}")

    if response_code == 200:
        print("✅ Test Passed")
        break  # Exit loop if success

    attempt += 1  # Try again if not success

# After 3 attempts, if still not 200:
if response_code != 200:
    print("❌ Test Failed after 3 attempts")
