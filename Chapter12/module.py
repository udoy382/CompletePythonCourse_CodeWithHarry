def myFunc():
    print("Hello world! This is myFunc function")

if __name__ == '__main__':
    # If this code is directly executed by running the file its present in.
    print("We are directly running the file")
    myFunc()

    print(__name__)
