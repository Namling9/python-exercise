# lambda function

# lambda input:expression

x = lambda x:x**2
x(2)

print(x)

# Filter
numbers = [1,2,4,5,6,7,8,8,9,10,55]
# def even(x):
#     return x%2==0

# even = list(filter(even, numbers))

# print(even)


# filter function lambda

even = list(filter(lambda x : x%2 == 0 and x <=50, numbers))
print(even) #[2, 4, 6, 8, 8, 10]


# Sorted function

city = ['kota', 'kathmandu', 'Damak', 'New york', 'paris']
# def length(city):
#     return len(city)

# sorted_city = list(sorted(city, key=length))
# print(sorted_city) #['kota', 'Damak', 'paris', 'New york', 'kathmandu']

# Sorted lambda function

sorted_city = list(sorted(city, key = lambda x: len(x) ))

print(sorted_city)