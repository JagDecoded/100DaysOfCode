#Given a year, return the century it is in.
#The first century spans from the year 1 up to and including the year 100,
#the second - from the year 101 up to and including the year 200, etc.

def centuryFromYear(year):
    #return (year//100)+1 if year%100 !=0 else year//100
    return (year-1)//100 +1
