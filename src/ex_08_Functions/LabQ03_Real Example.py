def validate_response_code(response_code):
    if response_code == 200:
        print("Request is successful")
    else:
        print("Error in the Request")

# validate_response_code(400)
#validate_response_code(200)
# validate_response_code(response_code=200)
validate_response_code(int(input("Enter your status code: ")))
