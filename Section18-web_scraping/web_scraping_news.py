from bs4 import BeautifulSoup
import requests
import pprint
# This is my take on the exercise, however what i didn't notice that the length of links and scores are not equal
res = requests.get('https://news.ycombinator.com/')
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
subtexts = soup.select('.subtext')
# Since the links and scores are not equal the below approach becomes less valid!
# We can fix this by using the subtitle field of the article as the scores are seldom not valid
# print(links)
# print(len(subtext))


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
    combined_data = [*zip(mega_links, mega_subtexts)]
    return combined(combined_data)
    # print(len(mega_subtexts))

# Function to combine and sort


def combined(combined_data):
    final_data = []
    for link, vote in combined_data:
        if vote.select('.subline'):
            vote_count = vote.select('.subline')[0].select('.score')[
                0].get_text().split(' ')[0]
            link_text = link.select('a')[0].get_text()
            link_url = link.select('a')[0].get('href')
            # print(link_url, link_text, vote_count)
            if int(vote_count) > 100:
                final_data.append((link_text, link_url, vote_count))
    return sorting(final_data)

# Sorting using the key


def sorting(final_data):
    return sorted(final_data, key=lambda x: x[2])


pprint.pprint(mega_pages(links, subtexts, 2))
