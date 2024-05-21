def calculator(total_money,price): #Defeine a fuction to determine the amount of chocolate a user can buy and the amount of change left over
    number=int(total_money//price) #Use the divisor to calculate the amount of chocolate a user can buy
    changes=total_money-number*price # Calculate the amount left after purchasing chocolate
    result=number,changes # Return the number of chocolates purchased and the remaining change 
    return(result)
total_money=100 #Defines the total amount of money owned by the user
price=7 # Define the price per chocolate bar
bars_bought,change_left=calculator(total_money,price) #Call calculator and get the number of chocolates purchased and the remaining change
print(f"You can buy {bars_bought} bars of chocolate, and you can get {change_left} yuan change.") 
# Print the number of chocolates users can buy and the remaining change