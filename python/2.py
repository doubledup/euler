#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

l = [1, 2]
while not l[-1] > 4000000:
    l.append(l[-1] + l[-2])
print(sum([x for x in l if x % 2 == 0]))
