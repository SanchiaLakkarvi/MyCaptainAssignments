#Python code to create a function called most frequent that takes a string and prints the letters in decreasing order of frequency
def most_frequent():
    str1 = str(input("Enter the word to find the frequency of the word:\n"))
    d = dict()
    for i in str1:
        d[i] = str1.count(i)
    for i in range(len(d)):
        max_1 = max(d, key=d.get)
        max_2 = max(d.values())
        print("{} = {}".format(max_1, max_2))
        d.pop(max_1)
most_frequent()
