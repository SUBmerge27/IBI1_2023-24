def calculator(total_money,price):
    number=int(total_money//price)
    changes=total_money-number*price
    result=number,changes
    return(result)
total_money=100
price=7
bars_bought,change_left=calculator(total_money,price)
print(f"You can buy {bars_bought} bars of chocolate, and you can get {change_left} yuan change.")