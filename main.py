import view
import rent
import return_

#Displaying Messages
def main():
    """This function call all the method of other mode"""
    print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++
|                          Welcome to costume rental application                        |
+++++++++++++++++++++++++++++++++++++++++++++++++++
        """)

    command = ""
    continu_loop = True
    while continu_loop == True:
        continloop = False
        while continloop == False:
            try:
                command = int(input("Select a desirable option\
                                        \n(1) || Press 1 to view a costume.\
                                        \n(2) || Press 2 to rent a costume.\
                                        \n(3) || Press 3 to retune a costume.\
                                        \n(4) || Press 4 to exit.\
                                        \nEnter a option: "))
                continloop = True
            except:
                print("")
                print("*" * 29)
                print("|\tInvalid Input!!!\t|")
                print("*" * 29)
                print("")
        if command == 1:
            print("")
            print("-" * 57)
            print("|\tLet's view a costume.\t\t|")
            print("-" * 57)
            print("")
            view.dic_print()
            print("")
        elif command == 2:
            print("")
            print("-" * 57)
            print("|\tLet's rents a costume.\t\t|")
            print("-" * 57)
            print("")
            rent.dic_print()
            rent.id_quantity_validation()
        elif command == 3 :
            print("")
            print("-" * 58)
            print("|\tLet's return a costume.\t |")
            print("-" * 58)
            print("")
            return_.dic_print()
            return_.id_quantity_validation()
        elif command == 4:
            print("")
            a = input("Do you really want to quit?\nIf yes then type 'y' or else other letter.  ").lower()
            if a == "y":
                print("")
                print("\t\t", "=" * 42)
                print("\t\t|\t", "Thanks You for using our application.\t          |")
                print("\t\t", "=" * 42)
                continu_loop = False
            print("")
        else:
            print("*" * 66)
            print("|\tPlease select the value as per the provided option!!!\t\t |")
            print("*" * 66)
            
main()
