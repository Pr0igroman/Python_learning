# file_name = "res.txt"
#
# lst = [4.5, 2.8, 3.9, 0.3, 1.0, 4.33, 7.777]
#
# with open(file_name, "w") as f:
#     # f.write((str(lst)))
#     for i in lst:
#         f.write(str(i) + " ")
#
# print("Done")


def longest_words(file):
    with open(file, "r") as text:
        w = text.read().split()
        max_length = len(max(w, key=len))
        res = [i for i in w if len(i) == max_length]
        if len(res) == 1:
            return res[0]
        else:
            return res


print(longest_words("text.txt"))
