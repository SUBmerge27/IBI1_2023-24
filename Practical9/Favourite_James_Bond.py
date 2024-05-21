birth_year = 1970 # Define a variable that represents the year of birth of the user

def FJB(birth_year): # Define a function to determine the user's favorite James Bond actor
    # Determine the user's favorite James Bond actor based on their birth year
    if 1955 <= birth_year <= 1968: # Roger Moore as James Bond time frame
        James_Bond = "Roger Moore"
    elif 1969 <= birth_year <= 1976: # Timeframe for Timothy Dalton to play James Bond
        James_Bond = "Timothy Dalton"
    elif 1977 <= birth_year <= 1987: # Pierce Brosnan as James Bond
        James_Bond = "Pierce Brosnan"
    elif 1988 <= birth_year <= 2003: #The time frame in which Daniel Craig plays James Bond
        James_Bond = "Daniel Craig"
    else:
        James_Bond = "Maybe James Bond doesn't belong to your time."# If the year of birth does not fall within the above range
# Returns the name of the user's favorite James Bond actor
    return James_Bond

result = FJB(birth_year)# Call the FJB function and pass in the user's birth year
print("Your favorite actor of James Bond might be: " + result) # Print the name of the user's likely favorite James Bond actor

