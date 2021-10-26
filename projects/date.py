import datetime



# calling the current date and time
print("Default Current time ")
def time():
    dt = datetime.datetime.now()
    print(dt)

time()

# further more modification

print("More modification ")

def supertime():
    dt= datetime.datetime.now()
    print("Current Year: ", end="")
    print(dt.year)
    print("Current Month: ", end="")
    print(dt.month)
    print("Current date : ", end="")
    print( dt.day)

supertime()
