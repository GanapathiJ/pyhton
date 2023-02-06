def square_num(n):
    return n*n
nums=[4,5,2,9]
print("orinigal list:",nums)
result=map(square_num,nums)
print("squarethe elements of the said list using map():")
print(list(result))
            
