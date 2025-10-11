# Escape Sequence
# \n -> new line
# \t -> tab
# \b -> backspace (1 char backspace)

# \n ->next line
print("Hello\nWorld")
""" 0/p 
Hello
World """

#\t -> tab space
print("Hello\tWorld") # Hello   World

# \b -> backspace
print("Hello\bWorld") # HelloWorld

# \' -> single quote
print("It\'s OK")  # It's OK

# \\ => back slash
txt = "This will insert one \\ (backslash)."
print(txt)  # This will insert one \ (backslash).

# \r -> Carriage Return ->goes to the beginning of the current line and overites with chars written after r
txt = "Hello\rWorld!"
print(txt) # World

# \f -> Form Feed
price = 34.521094
print("The item costs %f" % price) # The item costs 34.521094

discounted_price = 19.99
print("The discounted price is %.2f" % discounted_price) # The discounted price is 19.99

# \ooo -> oct value
txt = "\110\145\154\154\157"
print(txt) # Hello

#\xhh -> Hex Value
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) # Hello
