def fiel_read_():
    """This function opean the text file in Read Mode and put it into a dictionary"""
    count = 0 # set a counter
    file = open("stock.txt", "r") # open the text file in a read mode
    file_data = file.read() # read the text
    file_data = file_data.split("\n") # break the line at the end of file

    #This while loop is used to remove empty string in a list
    while ("" in file_data):
        file_data.remove("")
    dictionary = {}
    for i in range(len(file_data)):
        if file_data[i] != []: # check if file_data[i] is empty or not 
            count = count + 1 # increase the value by 1 in each iteration
            # inser the value from file_data in dictionary in a key and separate the value by ","
            dictionary [count] = file_data[i].split(",")
    file.close()
    return dictionary
