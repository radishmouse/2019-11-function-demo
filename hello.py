whom = "Chris"
# How do I define a function?
def greet(whom):
    print(f"Hayyyy {whom.upper()}")

# How do I use a function?
greet("Bob")
# We "call" the function by typing its name and passing it any arguments it needs.
# Another way to say this is: we "invoke" the function.

# Are arguments required?
#greet()
# Yes, they are required if there were arguments included in the definition of the function.

# Can I access arguments outside the body of a function?
print(whom)