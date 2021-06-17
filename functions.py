#coffee_is_grinding=True

#def press_grind_beans():
#    global coffee_is_grinding
#    if coffee_is_grinding:
#        print("Stopping that grind")
#        coffee_is_grinding = False
#    else:
#        print("Getting on that grind")
#        coffee_is_grinding = True

#press_grind_beans()

#def cash_withdrawal(amount, accnum)
#print(f)

#Create a function that takes 2 paramaters for a coffee order (Size and Type) and prints them in a complete sentence

#def coffee_order(size, type):
#    print(f"Here is your {size} {type} thank you for coming to barstucks")

#coffee_order("large", "Americano")

#def multiply_by_nine_fifths(celsius):
#    return celsius * (9/5)
#def get_farenheit(celsius):
#    return multiply_by_nine_fifths(celsius) + 32
#print("the temperature is {}f".format(get_farenheit(15)))
#Output to be 59f

#order_count=0
#def take_order(size, topping):
#    global order_count
#    print(f"a {size} Pizza with {topping}")
#    order_count += 1
#take_order("Large", "ham&pinapple")
#take_order("small", "anchovies")
#print(order_count)


#def withdraw(pin, amount, accnum):
#    balance = 1500
#    if pin == 1357 and balance>=amount:
#        print(f"Dispensing {amount} from account {accnum}")
#        balance=balance-amount
#        print(f"balance remaining = {balance}")
#    elif pin == 1357 and balance<amount:
#        print("Insufficient funds")
#    else:
#        print("Incorrect Pin")

#withdraw(1357, 1200, 12345678)

#Output: Dispensing 1200 from account 12345678 balance remaining = 300

#def withdraw(accnum):
#    pin=input("Please enter your pin: ")
#    if pin == 1357:
#        amount=int(input("How much would you like to withdraw? ")
#        if (amount<=balance): # Not sure why this doesn't seem to work ??????
#            print(f"Dispensing {amount} from account {accnum} ")
#        else:
#            print(f"insufficient funds in account {accnum} ")
#    else:
#        print("Incorrect pin")

#withdraw(12345678)