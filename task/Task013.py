# Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
#
# Hint: Use a counter (like wait_time) and break condition.
import time
import random

#******************* Method 1 **********************

# page_loaded = False
# wait_time = 0
# max_wait_time = 5
#
# while wait_time < max_wait_time:
#     page_loaded = random.choice([True, False])
#
#     if page_loaded:
#         print(f"Page loaded in {wait_time} seconds")
#         break
#
#     time.sleep(1)
#     wait_time = wait_time + 1
#     print(f"Page waiting for {wait_time} seconds")
#
# if not page_loaded:
#     print(f"Page not loaded within {max_wait_time} seconds")


#******************* Method 2 **********************
wait_time = 0
page_loaded = False


def api_response():
    return random.choice([False, True])


while wait_time < 5:
    page_loaded = api_response()
    if page_loaded:
        print(f"✅ Page loaded successfully in {wait_time + 1} seconds.")
        break
    else:
        print(f"⏳ Checking... (second {wait_time + 1})")
        time.sleep(1)  # wait for 1 second
        wait_time += 1

if not page_loaded:
    print("❌ Timeout! Page failed to load within 5 seconds.")