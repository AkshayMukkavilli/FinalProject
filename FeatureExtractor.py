import re
import pandas as pd
import numpy as np

ASIN_list = []


def percentages_upper_lower(line):
    no_upper_case_letters = 0
    no_lower_case_letters = 0
    total_no_letters = (len(line)-1)
    # total - 1 since every line has a \n at the end of the line
    for l in line[:-1]:
        if l.islower():
            no_lower_case_letters += 1
        elif l.isupper():
            no_upper_case_letters += 1
        elif l.isspace():
            total_no_letters -= 1
        else:
            pass
    if total_no_letters == 0:
        upper_case_percentage = 0
        lower_case_percentage = 0
    else:
        upper_case_percentage = round(((no_upper_case_letters / total_no_letters) * 100))
        # print(f"Upper Case: {upper_case_percentage}")
        lower_case_percentage = round(((no_lower_case_letters / total_no_letters) * 100))
        # print(f"Lower Case: {lower_case_percentage}")
    return upper_case_percentage, lower_case_percentage

with open('asin_test.txt','r') as fi:
    ASIN_list = fi.read().splitlines()

for asin in ASIN_list:
    words_per_review_list = []
    paragraphs_per_review = []
    avg_len_paragraphs_per_review = []
    break_tags_per_review = []
    upper_percentage_list = []
    lower_percentage_list = []
    fr = open('./review_data/'+asin+".txt",'r',encoding='utf-8')
    counter = 0
    for f_line in fr.readlines():
        temp_sum = 0
        print(f"this is f_line: {f_line} in the {counter}th iteration \n")
        counter += 1
        upper_percentage, lower_percentage = percentages_upper_lower(f_line)
        upper_percentage_list.append(upper_percentage)
        lower_percentage_list.append(lower_percentage)
        print(f" Upper case : {upper_percentage} \n Lower Case: {lower_percentage}")
        break_counter = 0
        words = len(f_line.split())
        words_per_review_list.append(words)
        break_pattern = re.compile(r'<br/>')
        pattern = re.compile(r"(<br/>)+")
        matches = pattern.finditer(f_line)
        break_matches = break_pattern.findall(f_line)
        for match in break_matches:
            break_counter += 1
        break_tags_per_review.append(break_counter)
        new_line = pattern.sub(r'<br/>', f_line)
        if len(new_line)==2 and new_line[0:1]==" ":
            paragraphs = 0
            avg_len_paragraphs = 0
        else:
            temp_for_paragraphs = new_line.split('<br/>')
            paragraphs = len(temp_for_paragraphs)
            for paragraph in temp_for_paragraphs:
                temp_sum += len(paragraph)
            avg_len_paragraphs = (temp_sum/paragraphs)-2
            #TODO: Check the logic of subtracting 2 from the average since the result is a bit off when paragraphs > 1
        paragraphs_per_review.append(paragraphs)
        avg_len_paragraphs_per_review.append(avg_len_paragraphs)
    print(len(words_per_review_list))
    print(words_per_review_list)
    print(len(paragraphs_per_review))
    print(f"the number of paragraphs is {paragraphs_per_review}")



    fr_1 = open('./review_data/'+asin+'metadata.csv','r',encoding='utf-8')
    # metadata =  fr_1.readlines()
    df = pd.read_csv('./review_data/'+asin+"metadata.csv", header= None, names=["Date","Stars","Helpful Votes"], thousands=r',', index_col=False)
    df['Z_Score_HelpfulVotes'] = (df['Helpful Votes'] - df['Helpful Votes'].mean()) / df['Helpful Votes'].std(ddof=0)
    df['Words']= words_per_review_list
    df['Z_Score_Words'] = (df['Words'] - df['Words'].mean()) / df['Words'].std(ddof=0)
    df['Paragraphs'] = paragraphs_per_review

    df['Z_Score_HelpfulVotes'] = (df['Paragraphs'] - df['Paragraphs'].mean()) / df['Paragraphs'].std(ddof=0)
    df['No.break tags'] = break_tags_per_review
    df['Percentage_Upper_Case']= upper_percentage_list
    df['Percentage_Lower_Case'] = lower_percentage_list
    df['Avg_len_paragraph_per_review'] = avg_len_paragraphs_per_review
    df.to_csv('./review_data/'+asin+'metadata.csv',index=False, header=True)
    fr_1.close()
