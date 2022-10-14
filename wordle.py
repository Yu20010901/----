import random

if __name__ =="__main__":
    #user input answer
    user_input = input("input = ")


    #Specify an answer
    f = open("words.txt","r")
    dictionary = f.read().splitlines()
    f.close()
    answer = random.sample(dictionary, 1)[0]
    print(answer)

    if not user_input in answer:
        print("please input an valid word")
        exit()
    #compare user inpyt and answer
    for i in range(len(user_input)):
        if user_input[i] == answer[i]:
            print("A")
        elif user_input[i] in answer:
            print("B")
        else:
            print("X")
