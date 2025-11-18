# Print even numbers between 1 and 20
for i in range(1,21):
    if i % 2 == 0:
        print(i, end=" ")

print()

# Print numbers from 10 down to 1
for i in range(10,0,-1):
    print(i, end=" ")

print()

# Skip numbers divisible by 3, from (0,100)
for i in range(1,101):
    if i % 3 == 0:
        continue
    else:
        print(i)