import sm_core

def main():
    x = sm_core.get_int("Enter 1st number: ",1,100)
    y = sm_core.get_int("Enter 2nd number: ", 1, 100)

    print(sm_core.calc("add",float(x),float(y)))

if __name__ == "__main__":
    main()