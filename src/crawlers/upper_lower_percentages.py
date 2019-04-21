"""
Method to calculate the percentage of upper case and lower case letters in
a given line.
"""


def percentages_upper_lower(line):
    """
    Calculates the percentage of upper case and lower case letters.
    :param line:
    :return: upper case percentage and lower case percentage
    """

    no_upper_case_letters = 0
    no_lower_case_letters = 0
    total_no_letters = (len(line) - 1)

    for l in line[:-1]:
        if l.islower():
            no_lower_case_letters += 1
        elif l.isupper():
            no_upper_case_letters += 1
        elif l.isspace():
            total_no_letters -= 1
        else:
            pass

    upper_case_percentage = round(((no_upper_case_letters / total_no_letters) * 100))
    lower_case_percentage = round(((no_lower_case_letters / total_no_letters) * 100))

    return upper_case_percentage, lower_case_percentage
