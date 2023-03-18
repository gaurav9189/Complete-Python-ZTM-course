from bs4 import BeautifulSoup
import requests
# This is my take on the exercise, however what i didn't notice that the length of links and scores are not equal
res = requests.get('https://news.ycombinator.com/')
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')

# Since the links and scores are not equal the below approach becomes less valid!
# We can fix this by using the subtitle field of the article as the scores are seldom not valid
# print(links)
# print(len(subtext))
combined_data = [*zip(links, subtext)]

# print(combined_data)

final_data = []


def combined(combined_data):
    for link, vote in combined_data:
        if vote.select('.subline'):
            vote_count = vote.select('.subline')[0].select('.score')[
                0].get_text().split(' ')[0]
            link_text = link.select('a')[0].get_text()
            link_url = link.select('a')[0].get('href')
            # print(link_url, link_text, vote_count)
            if int(vote_count) > 100:
                final_data.append((link_url, link_text, vote_count))
    return final_data


print(combined(combined_data))
