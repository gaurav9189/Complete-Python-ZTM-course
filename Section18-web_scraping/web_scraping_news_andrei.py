from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/')
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
# scores = soup.select('.score')
subtext = soup.select('.subtext')

# There can sometimes be a difference between these hence use a different approach
print(len(links))
print(len(subtext))


def combined(links, subtext):
    combined_li = []
    for idx, item in enumerate(links):
        # print(links[idx].select('a')[0].get('href'))
        # print(links[idx].select('a')[0].get_text())
        vote = subtext[idx].select('.subline')
        # print(vote)
        if vote:
            vote_count = subtext[idx].select('.subline')[0].select('.score')[
                0].get_text().split(' ')[0]
            link_text = links[idx].select('a')[0].get_text()
            link = links[idx].select('a')[0].get('href')
            if int(vote_count) > 100:
                combined_li.append((link_text, link, vote_count))
    return combined_li


print(combined(links, subtext))
