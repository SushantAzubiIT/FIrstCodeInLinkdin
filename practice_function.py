def find_the_biggest():
    Numbers = []
    while True:
        a = input("Enter a number or just press Enter to stop: ")
    
        if a == "":
            break

        try:
            b = int(a)
            # Use () for methods like append!
            Numbers.append(b) 

        except ValueError:
            print("Please Enter valid number")

    if Numbers:
        largest = Numbers[0]
        # Your manual logic is great!
        for i in range(len(Numbers)):
            if Numbers[i] > largest:
                largest = Numbers[i]
        print("the largest number is ", largest)    

    else:
        print("The list actually is empty")

find_the_biggest()