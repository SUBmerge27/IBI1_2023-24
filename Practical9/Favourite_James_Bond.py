birth_year = 1970

def FJB(birth_year):
    if 1955 <= birth_year <= 1968:
        James_Bond = "Roger Moore"
    elif 1969 <= birth_year <= 1976:
        James_Bond = "Timothy Dalton"
    elif 1977 <= birth_year <= 1987:
        James_Bond = "Pierce Brosnan"
    elif 1988 <= birth_year <= 2003:
        James_Bond = "Daniel Craig"
    else:
        James_Bond = "Maybe James Bond doesn't belong to your time."
    return James_Bond

result = FJB(birth_year)
print("Your favorite actor of James Bond might be: " + result)

