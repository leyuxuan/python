y = 0
n = 5
end = ''
candy = [1,2,3,4,5]
for i in candy:
    x = i//3
    candy[y] = x
    one = candy[y-1]
    candy[y-1] = one + x
    if y == len(candy) - 1:
        y = -1
    two = candy[y + 1]
    candy[y + 1] = two + x
    y += 1
for i in candy:
    end += str(i)
print(end)
