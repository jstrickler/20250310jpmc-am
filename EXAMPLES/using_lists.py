cities = []  # preferred
cities = list()  # not preferred
cities = ['Portland', 'Pittsburgh', 'Peoria']
print(f"cities: {cities}\n")

misc = ['abc', 5, 9.7, ['spam', 'ham']]

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
cities.insert(99, "Birmingham")
print(f"cities: {cities}\n")
print(f"{cities[7] = }")
# cities[20] = "Peoria" ERROR

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)
print(f"cities: {cities}\n")

# LIST.append(obj) LIST.insert(idx, obj) LIST.extend(iterable)

del cities[3]   # del cities[3:5]  NOT del cities[3,4]
print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

if "Durham" in cities:
    index = cities.index('Durham')
    cities.remove("Durham")

city = cities.pop()  # remove last element
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)  # remove element at index
print(f"city: {city}")
print(f"cities: {cities}\n")

# del LIST[idx]  LIST.remove(value) LIST.pop() LIST.pop(idx)    

cities[2] = "Milwaukee"
print(f"{cities = }")
print(f"{len(cities) = }")

print(f"{cities[4] = }")
print(f"{cities[-1] = }")  #  len(cities) - 1

