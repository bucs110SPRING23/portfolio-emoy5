#FIZZBUZZ

num = int(input("enter an upper limit: "))

for i in range(num+1):
    print("number:", i)
    if i % 5 == 0 and i % 3== 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    

    #notes printing stuff on separate lines print("hi", "bye", sep=",")