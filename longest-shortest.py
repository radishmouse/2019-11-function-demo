# shortest "accepts" a list of strings 
# or shortest "expects to receive" a list of strings
def shortest(word_list):
    # assume the first
    # one is the shortest
    the_shortest = word_list[0]
    # work through the list
    # or check every item
    # in the list
    for word in word_list:
        # compare the lengths
        if len(word) < len(the_shortest):
            # if we find one that is
            # shorter, we "save" that
            # as the new "shortest"
            the_shortest = word
    return the_shortest

# list can be changed with .append() and .pop() and other methods
some_words = ["coffee", "a", "laptops", "sky"]

# tuples cannot be changed.
#some_words = ("coffee", "a", "laptops", "sky")
# 

the_word = shortest(some_words)
print(the_word)

def longest(word_list):
    # assume the first
    # one is the longest
    the_longest = word_list[0]
    # work through the list
    # or check every item
    # in the list
    for jeff in word_list:
        # compare the lengths
        if len(jeff) > len(the_longest):
            # if we find one that is
            # shorter, we "save" that
            # as the new "longest"
            the_longest = jeff
    return the_longest

the_word = longest(some_words)
print(the_word)