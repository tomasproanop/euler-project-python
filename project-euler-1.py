def divisible_by_under(limit, divs):
    return (i for i in  range(limit) if any(i % div == 0 for div in divs))

print(sum(divisible_by_under(1000, (3, 5))))
