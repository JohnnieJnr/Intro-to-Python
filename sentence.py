sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)
print([len(words) for word in words])


sentence = "I love Global Code"
sentence = sentence.split()
print([len(length)for length in sentence])

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive = list(filter((lambda x: x > -1), numbers))
print(positive)

numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
is_even = list(filter((lambda x: x % 2 ==0 ), numbers))
print(is_even)


list = range(1,51)
for a in list:
    print([n for n in list if n % 2==0])


numbers = range(1,51)
is_even = list(filter((lambda x: x % 2 ==0 ), numbers))
print("Even Numbers")
print(is_even)

numbers = range(1,51)
is_even = list(filter((lambda x: x % 2 ==1 ), numbers))
print("Odd Numbers")

words = ["hello", "my", "name", "is", "Sam"]
length = [len(word) for word in words]
word = [word.upper() for word in words]
print(tuple(zip(word,length)))