# You can use Counter from the collections' library to get a dictionary with counts of all the unique elements in a list
from collections import Counter

LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore"

if __name__ == '__main__':
    print(f"Lorem ipsum counter: {Counter(LOREM_IPSUM)}")
