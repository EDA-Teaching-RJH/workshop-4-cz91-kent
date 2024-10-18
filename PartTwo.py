


cost = 0
remainder = 0
change = 0
x=75

while cost <= 75:
    print("input ", x,"p")
    coffee =  int(input())

    if coffee == 50 :
        cost += 50
        remainder - 50
        
        #coffee = int(input("remainder = ", remainder))

    elif coffee == 20 :
        cost += 20
        remainder - 20
        #coffee = int(input("remainder = ", remainder))
    elif coffee == 10 :
        cost += 10
        remainder - 10
        #coffee = int(input("remainder = ", remainder))
    
    elif coffee == 5 :
        cost += 5
        remainder - 5
        #coffee = int(input("remainder = ", remainder))

    else :
        print("we only accept 50p, 20p, 10p or 5p ")
    x=75-cost
    if x>0 :
        print("you need to add ",x)
    elif x==0:
                print("done")
    else:
                 print("your change is ",abs(x))




