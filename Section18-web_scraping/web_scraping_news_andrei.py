from bs4 import BeautifulSoup
import requests
import pprint

res = requests.get('https://news.ycombinator.com/')
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
# scores = soup.select('.score') -> this was discarded because some news didn't have score
subtexts = soup.select('.subtext')

# Now the lenth of both the news are same!
# print(len(subtexts))

# Adding more pages to the soup:-


def mega_pages(links, subtexts, pages=0):
    mega_links = links[:]
    mega_subtexts = subtexts[:]
    if pages:
        for page in range(2, pages+1):
            # print(f'page num is {page}')
            next_res = requests.get(f'https://news.ycombinator.com/?p={page}')
            next_soup = BeautifulSoup(next_res.text, 'html.parser')
            next_links = next_soup.select('.titleline')
            next_subtexts = next_soup.select('.subtext')
            # print(len(next_links))
            # print(len(mega_links))
            # Mistake was to use append here, since we're not adding single elements but entire list
            mega_links = mega_links + next_links
            mega_subtexts = mega_subtexts + next_subtexts
    else:
        print('Page isn\'t working')
    return combined(mega_links, mega_subtexts)
    # print(len(mega_subtexts))


def combined(links, subtexts):
    combined_li = []
    for idx, item in enumerate(links):
        # since it returns a list, the ones without score is empty list
        vote = subtexts[idx].select('.subline')
        # print(vote)
        if vote:
            vote_count = subtexts[idx].select('.subline')[0].select('.score')[
                0].get_text().split(' ')[0]
            link_text = links[idx].select('a')[0].get_text()
            link = links[idx].select('a')[0].get('href')
            if int(vote_count) > 100:
                combined_li.append((link_text, link, vote_count))
    return combined_li


pprint.pprint(mega_pages(links, subtexts, 3))

# print(combined(links, subtexts))
