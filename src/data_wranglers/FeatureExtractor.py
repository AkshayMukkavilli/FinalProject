import re
import pandas as pd
from textblob import TextBlob
from src.crawlers.upper_lower_percentages import percentages_upper_lower


def get_sentiment_polarity(line):
    sentiment = TextBlob(line)
    return sentiment.polarity


with open('/Users/t_velpac/mission/WorkingCopy/src/crawlers/asins.txt', 'r') as fi:
    ASIN_list = fi.read().splitlines()

for asin in ASIN_list:
    words_per_review_list = []
    paragraphs_per_review = []
    avg_len_paragraphs_per_review = []
    break_tags_per_review = []
    upper_percentage_list = []
    lower_percentage_list = []
    sentiment_polarity_list = []
    with open('./review_data_sentiments/'+asin+".txt", 'r', encoding='utf-8') as fr:
        counter = 0
        for f_line in fr.readlines():
            temp_sum = 0
            counter += 1
            upper_percentage, lower_percentage = percentages_upper_lower(f_line)
            upper_percentage_list.append(upper_percentage)
            lower_percentage_list.append(lower_percentage)
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
            if len(new_line) == 2 and new_line[0:1] == " ":
                paragraphs = 0
                avg_len_paragraphs = 0
            else:
                temp_for_paragraphs = new_line.split('<br/>')
                paragraphs = len(temp_for_paragraphs)
                for paragraph in temp_for_paragraphs:
                    temp_sum += len(paragraph)
                avg_len_paragraphs = (temp_sum/paragraphs)-2
            paragraphs_per_review.append(paragraphs)
            avg_len_paragraphs_per_review.append(avg_len_paragraphs)
            sentiment_polarity_list.append(get_sentiment_polarity(f_line))

    with open('./review_data_sentiments/'+asin+'metadata.csv', 'r', encoding='utf-8') as fr:
        df = pd.read_csv('./review_data_sentiments/'+asin+"metadata.csv",
                         header=None,
                         names=["Date", "Stars", "Helpful_Votes"],
                         thousands=r',',
                         index_col=False)

        df['Words'] = words_per_review_list
        df['Z_Score_Words'] = (df['Words'] - df['Words'].mean()) / df['Words'].std(ddof=0)
        df['Paragraphs'] = paragraphs_per_review
        df['Z_Score_Paragraphs'] = (df['Paragraphs'] - df['Paragraphs'].mean()) / df['Paragraphs'].std(ddof=0)
        df['Sentiment_Polarity'] = sentiment_polarity_list
        df['No.break tags'] = break_tags_per_review
        df['Percentage_Upper_Case'] = upper_percentage_list
        df['Percentage_Lower_Case'] = lower_percentage_list
        df['Avg_len_paragraph_per_review'] = avg_len_paragraphs_per_review
        df['Z_Score_HelpfulVotes'] = (df['Helpful_Votes'] - df['Helpful_Votes'].mean()) / df['Helpful_Votes'].std(ddof=0)
        df.to_csv('./review_data_sentiments/'+asin+'metadata.csv', index=False, header=True)
