'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
count = 0 
def count_th(word):
    global count
    # print(word)
    if len(word) < 2:
        return 0 
    elif word[-2:] == "th":
        # print("found th!")
        count += 1
        # print(count)
    # print("recursive case called!",word)
    count_th(word[:-1])
    return count

# if __name__ == "__main__":
#     print(count_th("abcthefthghith"))
