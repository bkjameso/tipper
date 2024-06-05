def tipper():
    #This does the math for the tip
    print("_____WELCOME TO TIPPER_____")

    amount_paid = float(input("how much did you pay?"))
    great = amount_paid * 0.3
    good = amount_paid * 0.25
    okay = amount_paid * 0.15
    bad = amount_paid * 0.05

    #finds tip due to waiter performance
    print("input great, good, okay, or bad please")
    waiter_performance = input("How was your service?")
    if waiter_performance == "great":
        print(f"I reccommend tipping ${great:.2f}")
    
    elif waiter_performance == "good":
        print(f"I reccommend tipping ${good:.2f}")
    
    elif waiter_performance == "okay":
        print(f"I reccommend tipping ${okay:.2f}")
    
    elif waiter_performance == "bad":
        print(f"I reccomend tipping ${bad:.2f}")
    
    else: print("Invalid input. Please input geat, good, okay, or bad")



    print("___THANK YOU FOR USING TIPPER___")

tipper()



    


    