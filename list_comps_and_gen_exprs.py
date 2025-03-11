fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    value = f.upper()
    f0.append(value)
print(f"{f0 = }\n")

# [VALUE for VAR in ITERABLE]
f1 = [f.upper() for f in fruits]
print(f"{f1 = }\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"{f2 = }\n")

f3 = [f for f in fruits if len(f) > 8]
print(f"{f3 = }\n")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

n1 = [float(x) * 10 for x in nums]
print(f"{n1 = }\n")

word = "mango\u00B0"
print(f"{word = }")
uvalues = [ord(c) for c in word]
print(f"{uvalues = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[3] for p in people]
print(f"{dobs = }\n")

nums = [800, 80.9, 1000, 32, -3, 8.4, 18, 255, 400.0, 5, 5000]
n2 = [n + 1000 for n in nums if isinstance(n, int)]
print(f"{n2 = }\n")

fruits_upper = [f.upper() for f in fruits]  # makes a list
fruits_gen = (f.upper() for f in fruits) # fruits_gen contains 0% fruits
print(f"{fruits_gen = }")
for fruit in fruits_gen:
    print(fruit)

