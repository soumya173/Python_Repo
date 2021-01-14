
def stockBuySell(stock, n):
    if n == 1:
        print("At least 2 points needed to buy and sell")
        return
    profit = i = 0
    while i < (n-1):
        # Find the local minima
        while i < n and stock[i+1] <= stock[i]:
            i += 1
        # Reached the end of the list, no further solution exist
        if i == n-1:
            break
        buy = i
        i += 1
        # Find the local maxima
        while i < n and stock[i] >= stock[i-1]:
            i += 1

        sell = i - 1
        profit += (stock[sell] - stock[buy])
        print(f"Buying on day: {buy}({stock[buy]}) and Selling on day: {sell}({stock[sell]}). Profit: {stock[sell] - stock[buy]}")
    print(f"Total Profit: {profit}")


# stock = [6, 3, 1, 5, 2, 7, 9, 4]
stock = [100, 180, 260, 310, 40, 535, 695]
stockBuySell(stock, len(stock))

