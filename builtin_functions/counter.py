# You can use Counter from the collections' library to get a dictionary with counts of all the unique elements in a list
from collections import Counter

if __name__ == '__main__':
    lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore"
    print(f"Lorem ipsum counter: {Counter(lorem_ipsum)}")
