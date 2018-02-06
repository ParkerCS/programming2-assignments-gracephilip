def my_function4(name = "Grace"):
    '''
    Says hellp
    :param name:
    :return:
    '''
    name = input("Enter your username: ")
    if name == "Grace":
        password = input("Enter your password: ")
        if password == "12345":
            print("Welcome")
            done = True
        else:
            print("Incorrect")
            done = True
    else:
        print("Access denied")
        done = True


if __name__ == "__main__":
    pass
