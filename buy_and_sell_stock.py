#Time Complexity : O(n^2)
#Space Complexity : O(1)
def buy_sell_stock(A):
    max_profit=0
    for i in range(len(A)-1):
        for j in range (i+1,len(A)):
            if(A[j]-A[i])>max_profit:
                max_profit = A[j]-A[i]
    return print(max_profit)

#Time Complexity : O(n)
#Space Complexity : O(1)
def buy_sell_stock_optimized(A):
    max_profit = 0
    min_price = A[0]
    for price in A:
        min_price = min(min_price,price)
        compare_profit = price - min_price
        max_profit = max(compare_profit,max_profit)
    return print(max_profit)


buy_sell_stock([310,315,275,295,260,270,290,230,255,250])
buy_sell_stock_optimized([310,315,275,295,260,270,290,230,255,250])