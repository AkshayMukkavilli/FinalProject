


#This script is to take a list of ASIN numbers as input in the form of a text file
#and downloads all the reviews of each individual product with a unique ASIN and then saves the
#reviews of every product in a separate text file named in the format ASIN_number.txt in the present working directory


import requests
from bs4 import BeautifulSoup
from lxml import html
import random
import re
# import proxies
import time


users = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/6.2.8 Safari/537.85.17',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Mozilla/5.0 (Linux; U; Android 4.3; de-de; SAMSUNG GT-I9300/I9300XXUGNA5 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SPH-L710 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 4.3; de-de; SAMSUNG GT-I9305/I9305XXUENH1 Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt)',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Thunderbird/45.8.0',
    'Mozilla/5.0 (X11; Datanyze; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) Qt/4.8.2',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20150101 Firefox/47.0 (Chrome)',
    'Opera/9.80 (Windows NT 5.1; WOW64) Presto/2.12.388 Version/12.17',
    'Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.9.168 Version/11.50'
]


header = {'User-Agent': users[random.randint(0, len(users) - 1)]}
ASIN_list = []
with open('asin_test.txt','r') as fi:
    ASIN_list = fi.read().splitlines()

i = 0
counter = 0
# proxies_here = proxies.get_proxies()
# proxy_pool = cycle(proxies_here)
for asin in ASIN_list:
    total_reviews = ""
    print("Working on the product wiith ASIN: ",ASIN_list[i])
    #url = "https://www.amazon.com/dp/" + ASIN_list[i]
    url = "https://www.amazon.com/dp/" + asin

    # proxies



    source_code = requests.get(url, headers=header)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")

    # Getting the link that says see all reviews
    all_reviews_link = soup.find('a',{'class': "a-link-emphasis a-text-bold", 'data-hook': "see-all-reviews-link-foot"})
    while all_reviews_link == None:
        source_code = requests.get(url, headers=header)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        all_reviews_link = soup.find('a',
                                     {'class': "a-link-emphasis a-text-bold", 'data-hook': "see-all-reviews-link-foot"})
    print("The all reviews link is: " , all_reviews_link)
    only_link = (all_reviews_link['href'])
    total_link = "https://www.amazon.com" + only_link + "&pageNumber="
    print(total_link)

    # For getting the total number of pages with reviews
    see_all_reviews_text = all_reviews_link.text
    list_after_splitting = see_all_reviews_text.split()[2]
    try:
        str_no_of_reviews = int(list_after_splitting)
    except:
        str_no_of_reviews = int(list_after_splitting.replace(',', ''))
    iterator= int(str_no_of_reviews/10)
    if (str_no_of_reviews%10) == 0:
        iterator = int(str_no_of_reviews/10)
    else:
        iterator += 1
    print("The product has ", iterator , "pages of reviews")


    page = 1
    fw = open(asin + '.txt', 'w+', encoding="utf-8")
    while page <= iterator:
        print("Now, working on page: ", page)
        review_link_with_pageno = total_link + str(page)
        header_1 = {'User-Agent': users[random.randint(0, len(users) - 1)]}
        source_code_1 = requests.get(review_link_with_pageno, headers=header_1)
        plain_code = source_code_1.text
        soup_1 = BeautifulSoup(plain_code, "lxml")
        reviews = soup_1.findAll('span', {'class': "a-size-base review-text", 'data-hook': "review-body"})
        # The type of reviews is <class 'bs4.element.ResultSet'>
        # Thus, converting it into string format below
        str_reviews = str(reviews)
        one_review_per_line = str_reviews.replace('[<span class="a-size-base review-text" data-hook="review-body">', '')
        one_review_per_line = str_reviews.replace('<span class="a-size-base review-text" data-hook="review-body">', '')
        one_review_per_line = one_review_per_line.replace('</span>,', '\n')
        one_review_per_line = one_review_per_line.replace('</span>]','')
        one_review_per_line = one_review_per_line.replace(one_review_per_line[0], ' ')
        if len(one_review_per_line) < 3 and one_review_per_line[1]=="]":
            print("the data could not be retrieved from the page: ", page)
            one_review_per_line = ""
        if one_review_per_line !="":
            total_reviews = total_reviews  + one_review_per_line + "\n"
        else:
            continue


        page += 1
        date = ""
        stars = 0
        helpful_votes = 0
        '''
        Collecting the following metadata from each customer review:
        1. Date of review
        2. Star rating
        3. Number of helpful votes on each review
        4. Percentage of upper case letters in each review
        5. Percentage of lower case letters in each review
        '''


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
            upper_case_percentage = round(((no_upper_case_letters / total_no_letters) * 100))
            # print(f"Upper Case: {upper_case_percentage}")
            lower_case_percentage = round(((no_lower_case_letters / total_no_letters) * 100))
            # print(f"Lower Case: {lower_case_percentage}")
            return upper_case_percentage, lower_case_percentage


        with open(asin + 'metadata.csv', 'a') as fa:
            with open(asin + 'titles.txt', 'a', encoding="utf-8") as fs:
                for rev in soup_1.findAll('div', {'data-hook': "review", 'class': "a-section review aok-relative"}):
                    just_one_review_out_of_10 = str(rev)
                    mini_soup = BeautifulSoup(just_one_review_out_of_10, "lxml")
                    print(rev.prettify())
                    print("\n\n\n")


                    # mini_content_for_xpath = html.fromstring(mini_soup.text)
                    # helpful_votes_xpath = '//span[@data-hook="helpful-vote-statement"]/text()'
                    # helpful_votes_using_xpath = mini_content_for_xpath.xpath(helpful_votes_xpath)
                    # print(helpful_votes_using_xpath)


                    date = mini_soup.find('span', {'data-hook': "review-date"}).string
                    rep = {"January": "01", "February": "02","March": "03","April": "04","May": "05","June": "06", "July": "07","August": "08", "September": "09","October": "10","November": "11","December": "12"}  # define desired replacements here

                    rep = dict((re.escape(k), v) for k, v in rep.items())
                    date_pattern = re.compile("|".join(rep.keys()))
                    date = date_pattern.sub(lambda m: rep[re.escape(m.group(0))], date)

                    date = date.replace('on ', '')
                    date = date.replace(', ', '/')
                    date = date.replace(' ', '/')

                    stars = str(mini_soup.find('span', {'class': "a-icon-alt"}).string[0])
                    helpful_votes = str(mini_soup.find('span', {'data-hook': "helpful-vote-statement", 'class': "a-size-base a-color-tertiary cr-vote-text cr-vote-error cr-vote-component"}))
                    # print(f" ==================================\n\n {mini_soup.prettify()}")


                    helpful_votes = str(mini_soup.find('span', {'data-hook': "helpful-vote-statement",'class': "a-size-base a-color-tertiary cr-vote-text cr-vote-error cr-vote-component"}))
                    try:
                        helpful_votes = helpful_votes.replace(
                            '<span class="a-size-base a-color-tertiary cr-vote-text cr-vote-error cr-vote-component" data-hook="helpful-vote-statement">','')
                    except:
                        pass
                    if helpful_votes == 'None':
                        helpful_votes = str(mini_soup.find('span', {'data-hook': "helpful-vote-statement",'class': "a-size-base a-color-tertiary cr-vote-text"}))
                        try:
                            helpful_votes = helpful_votes.replace(
                                '<span class="a-size-base a-color-tertiary cr-vote-text" data-hook="helpful-vote-statement">','')
                        except:
                            pass
                    if helpful_votes == 'None':
                        helpful_votes = '0'
                    if helpful_votes != '0':
                        helpful_votes = helpful_votes.replace(' found this helpful</span>', '')
                        if 'people' in helpful_votes:
                            helpful_votes = helpful_votes.replace(' people' , '')
                        elif 'One person' in helpful_votes:
                            helpful_votes = helpful_votes.replace('One person', '1')


                    fa.write(date + ',' + stars + ',' + helpful_votes  + "\n")
                for title in soup_1.findAll('a', {'data-hook': "review-title",
                                                  'class': "a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"}).text():
                    total_review_titles = ''
                    title = str(title)
                    print(title)
                    title = title[194:]
                    if title[0] == '>':
                        title = title[1:]
                    title = title.replace('</a>', '')
                    # print(f" Title Upper : {title_lower_percentage} \n Title Lower:{ title_upper_percentage}")
                    # print("====================================================")

                    total_review_titles = total_review_titles + title + '\n'
                    fs.write(total_review_titles)
    i += 1
    fw.write(total_reviews)
    fw.close()

    with open(asin +'titles.txt','r', encoding="utf-8") as title_read:
        with open(asin + 'titles_metadata.csv', 'w+') as title_write:
            for t_line in title_read.readlines():
                title_lower_percentage = 0
                title_upper_percentage = 0
                title_upper_percentage, title_lower_percentage = percentages_upper_lower(t_line)
                no_words_in_title = len(t_line.split())
                length_title = len(t_line)-1
                title_metadata = str(no_words_in_title) + ',' + str(length_title) + ',' + str(title_upper_percentage) + ',' + str(title_lower_percentage) +'\n'
                title_write.write(title_metadata)






