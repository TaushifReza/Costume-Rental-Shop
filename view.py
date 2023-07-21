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
