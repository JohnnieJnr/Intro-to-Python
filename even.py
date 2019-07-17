def is_even(x):
    number = []
    for a in x:
        if a % 2 == 0:
            number.append(a)
    return number
print(is_even([1,56,234,87,4,76,24,69,90,135]))

#displaying even numbers
numbers = [1,56,234,87,4,76,24,69,90,135]
is_even = list(filter((lambda x: x % 2 ==0 ), numbers))
print(is_even)

#displaying odd numbers
numbers = [1,56,234,87,4,76,24,69,90,135]
is_odd = (list(filter((lambda x:not( x % 2 ==0) ), numbers)))
print(is_odd)