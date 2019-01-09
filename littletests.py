# test_line = "as described\n"
# # test_line1 = "Love it!\n"
# print(len("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaaa"))
#
# def percentages_upper_lower(line):
#     no_upper_case_letters = 0
#     no_lower_case_letters = 0
#     total_no_letters = (len(line) - 1)
#     print(f"actual length {len(line)}")
#     print(f"total length after taking one out is: {total_no_letters}")
#     print(line[-1])
#     # total - 1 since every line has a \n at the end of the line
#     for l in line[:-1]:
#
#         if l.islower():
#             no_lower_case_letters += 1
#             print(l)
#         elif l.isupper():
#             no_upper_case_letters += 1
#         elif l.isspace():
#             total_no_letters -= 1
#             print("one count decreased")
#             print(total_no_letters)
#         else:
#             pass
#     print(f"Upper case letters: {no_upper_case_letters}")
#     print(f"Lower case letters: {no_lower_case_letters}")
#     print(f"Total number of letters: {total_no_letters}")
#     upper_case_percentage = round(((no_upper_case_letters / total_no_letters) * 100))
#     # print(f"Upper Case: {upper_case_percentage}")
#     lower_case_percentage = round(((no_lower_case_letters / total_no_letters) * 100))
#     # print(f"Lower Case: {lower_case_percentage}")
#     return upper_case_percentage, lower_case_percentage
#
# a,b = percentages_upper_lower(test_line)
# # c,d = percentages_upper_lower(test_line1)
# print(a,b)

print(len("This is a flag and it will blow in the wind, but don't expect much! The one I was sent has a fiberglass pole that is bare. No handle and the end of the pole is just cut off rough fiberglass."))
print(len("I put some little plastic cap on the end, then wrapped hockey tape to protect your hand. It might hold up for the summer..."))