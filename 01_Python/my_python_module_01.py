
def addition(a,b):
    return a+b

def say_hello():
    while True:
        i = input("Please enter a name: ")
        try:
            name = str(i)
        except:
            print("The input cannot be converted to a string. Please, try again.")
        else:
            print(f"Hello {name}!")
            break
