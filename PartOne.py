
camel_input = input("Input a Camel variable name ")

for c in camel_input :

    if c.islower() :

        print(c, end="")

    if c.isupper() :

        print("_" + c.lower(), end="")
    
print()