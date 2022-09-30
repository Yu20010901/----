if __name__ =="__main__":
    
    f = open("day1.txt","r")
    data = f.read().splitlines()#Extract numbers in the text file 

    data_length = len(data)#Change the data type to int
    for i in range(data_length):
        data[i] = int(data[i])

    counter = 0
    for i in range(data_length-1):
        if data[i+1]-data[i]>0:
            counter += 1

    print(counter)


