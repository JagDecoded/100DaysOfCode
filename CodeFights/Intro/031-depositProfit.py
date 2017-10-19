def depositProfit(deposit, rate, threshold):
    year=0
    while deposit < threshold:
        year+=1
        deposit=deposit+deposit*(rate/100)
    return year
