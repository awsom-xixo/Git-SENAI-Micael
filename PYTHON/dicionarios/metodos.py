ra = {'Liz':229874, 'Hugo':215793, 'Sofia':199745}

print(list(ra.items()))
print(list(ra.keys()))
print(list(ra.values()))


print(ra.get('Hugo'))
print(ra.get('Maria'))
print(ra.get('Maria', 'N/A'))