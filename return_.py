import random
import converter


dictionary = converter.fiel_read_()
def dic_print():
    print("-"*95)
    print("ID\tName\t\tBrand\t\t Price\tQuantity")
    print("-" * 95)

    # place all the value of dictionary in a tabular form
    for key, value in dictionary .items():
        print(key, end="\t") # give a tab at the end of key
        for i in value:
            print(i, end="\t") # give a tab between each value
        print("")
    print("-" * 95)


costume_name = []
brand_ = []
price_ = []
quantity_ = []
single_price = []
user_selected_costume_ID = []
all_items_dic = {}


def id_quantity_validation():
    """This function validate ID and quantity enter by user"""
    loop1 = False
    while loop1 == False:
        try:
            ID = int(input("Enter ID of the costume: "))
            loop1 = True
        except:
            print("")
            print("*" * 29)
            print("|\tInvalid Input!!!\t|")
            print("*" * 29)
            print("")
    if 0 < ID <= len(dictionary):
        print("")
        loop2 = False
        while loop2 == False:
            try:
                qty = int(input("Enter the Quantity: "))
                loop2 = True
            except:
                print("")
                print("*" * 29)
                print("|\tInvalid Input!!!\t|")
                print("*" * 29)
                print("")
        dictionary_selected = dictionary[ID] # dictionary_selected yo dictionary user ley ID rakha ko value store garxa
        if int(qty >0):
            user_selected_costume_ID.append(ID)
            update_qty = int(dictionary_selected[3]) + qty
            dictionary_selected[3] = str(update_qty)
            print("")
            print(dictionary)
            print("")
            update_file()
            price = float(dictionary_selected[2].replace("$", "")) * qty

            # append costume name, brand, price, quantity in a different list
            costume_name.append(dictionary_selected[0])
            brand_.append(dictionary_selected[1])
            price_.append(price)  # This list contain costume price  * total no quantity
            quantity_.append(qty)
            single_price.append(dictionary_selected[2])  # individual price of a single costume
            
            # store all item and their details in a dictionary
            j = 0
            d= {1:"",2:"",3:"" ,4:"",5:"",6:"",7:""}
            print(user_selected_costume_ID)
            for i in user_selected_costume_ID:
                x =  user_selected_costume_ID.count(i)
                d[i] = x

            for k, v in d.items():
                if v == 1:
                    all_items_dic[k] = [costume_name[j], brand_[j], single_price[j], quantity_[j]]
                    j =j+1
                    #print(j)
                elif v == "":
                    pass
                elif v > 1:
                    c = 0
                    for l in range(v):
                        c = c + quantity_[l]
                    all_items_dic[k] = [costume_name[j], brand_[j], single_price[j], c]
                    j = j+v


            # asked the user if you want to rent more
            again = input("Do you wise to return more?\nIf yes then type 'y' or else type any other letter: ").lower()
            if again == "y":
                dic_print()
                id_quantity_validation()
            else:
                invoice()
        else:
            print("")
            print("*"*29)
            print("|\tInvalid Quantity!!!\t |")
            print("*"*29)
            print("")
            id_quantity_validation()
    else:
        print("")
        print("*" * 56)
        print("|\tPlease provide a valid costume ID !!!\t\t|")
        print("*" * 56, "\n")
        print("")
        id_quantity_validation()


def update_file():
    """This function update the main stock file"""
    f = open("stock.txt", "w")
    for key, value in dictionary.items():
        string = ",".join(value)
        f.write(string)
        f.write("\n")
    f.close()


invoice_file = []
invoice_file1 = []
from datetime import datetime, date


def invoice():
    """Print the invoice bill and write it into a txt file"""
    print("")
    name = input("Enter your name: ")
    phone = phone_validate()
    random_ = random.randint(1, 100)
    fine = 0
    while True:
        try:
            rentday = input("Enter the date you rent costume(yyyy-mm-dd): ")
            bDate = datetime.strptime(str(rentday), "%Y-%m-%d")
            break
        except:
            print("")
            print("Invalid date format.Please enter correct date(yyyy-mm-dd)")
            print("")
    returndate = date.today()
    rDate = datetime.strptime(str(returndate), "%Y-%m-%d")
    delta = rDate - bDate
    noDayCostumeRented = delta.days
    if noDayCostumeRented > 5:
        fineDay = noDayCostumeRented - 5
        # Calculating fine
        fine = fineDay * 1
    else:
        fine = 0
    totalAmount = price_total() + fine
    print("")
    print("\t\t", "+" * 23)
    print("\t\t|\tBill Details\t|")
    print("\t\t", "+" * 23)
    print("=" * 55)
    print("\t\t\tCostume Rental shop")
    print("-" * 97)
    print("Name: ", name)
    print("Phone: ", phone)
    print("Date of return: ", returndate)
    print("Date of rent: ", rentday)
    print("Number of day Costume rented: ", noDayCostumeRented)
    print("Fine Amount: $", fine)
    print("-" * 97)
    print("ID\tCostume Name\t Brand\t\t Price\tQuantity")
    print("-" * 97)
    for key, value in all_items_dic.items():
        print(key, "\t", value[0], "\t", value[1], "\t", value[2], "\t", value[3])
    print("-" * 97)
    print("\t\t\t           Total Amount: $", totalAmount)
    print("-" * 97)
    print("\t\t|© 2022 || Costume Rental Shop.|")
    print("*" * 65)
    print("")
    alert = name + str(random_)
    print("*" * 56)
    print(f"|  Note: Please remember your bile number is {[alert]}\t|")
    print("*" * 58)
    print("")
    
    xy = "------------------------ Return Bill -------------------------------"
    a = "-" * 69
    b = "ID\tCostume Name\t\tBrand\t\t\tPrice\t\tQuantity"
    c = "\t\t\t|© 2022 || Costume Rental Shop.|"

    invoice_file.append(xy)
    invoice_file.append("")
    invoice_file.append("\t\t\t\t\t\t\tDate of return: " + str(returndate))
    invoice_file.append("\t\t\t\t\t\t\tDate of rent: " + rentday)
    invoice_file.append("Customer Name: " + name)
    invoice_file.append("Phone number: " + str(phone))
    invoice_file.append("Bill number: " + alert)
    invoice_file.append("Number of day Costume rented: " + str(noDayCostumeRented))
    invoice_file.append("Fine Amount: $" + str(fine))
    invoice_file.append("")
    invoice_file.append(a)
    invoice_file.append(b)
    invoice_file.append(a)
    invoice_file1.append(a)
    invoice_file1.append("\t\t\t\t\t    Total Amount: $" + str(totalAmount))
    invoice_file1.append(a)
    invoice_file1.append(c)
    invoice_file1.append(a)

    file_save = alert + ".txt"
    with open(f"Return/{file_save}", 'w') as f:
        for line in invoice_file:
            f.write(f"{line}\n")
        for key, value in all_items_dic.items():
            a = key
            b = value[0]
            c = value[1]
            d = value[2]
            e = value[3]
            f.write(f"{a}\t{b}\t\t{c}\t\t{d}\t\t{e}\n")
        for line1 in invoice_file1:
            f.write(f"{line1}\n")


total_price = []


def price_total():
    """This function calculate the total amount of all renturn costume"""
    sum1 = 0
    for i in range(len(price_)):
        total_price = price_[i]
        sum1 += total_price

    return sum1



def phone_validate():
    """This function ask phone number and check validation"""
    loop3 = False
    while loop3 == False:
        loop4 = False
        while loop4 == False:
            try:
                phone = int(input("Enter phone Number: "))
                loop4 = True
            except:
                print("")
                print("*" * 29)
                print("|\tInvalid Input!!!\t|")
                print("*" * 29)
                print("")
        if len(str(phone)) == 10:
            loop3 = True
        else:
            print("")
            print("*" * 56)
            print("|\tPhone number must be 10 digits!!!\t\t|")
            print("*" * 56)
            print("")
    return phone



