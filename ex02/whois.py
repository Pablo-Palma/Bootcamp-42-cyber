import sys

if len(sys.argv) == 1:
    print("AssertionError: argument is not an integer")
elif len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
else:
    try:
        number = int(sys.argv[1])
        if number == 0:
            print("I'm zero.")
        elif number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("Error: argument must be an integer.")

