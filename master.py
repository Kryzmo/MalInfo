import re
import requests

url = input('daj linka')

def get_mal_info():
    while True:
        for r in range(10):
            try:
                get_id = re.findall('\d+', url)
                anime_id = get_id[0]
                api_url = 'https://api.jikan.moe/v4/anime/{}'.format(anime_id)
                headers = { 
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117', 
                'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
                'Accept-Language' : 'en-US,en;q=0.5', 
                'Accept-Encoding' : 'gzip', 
                'DNT' : '1',
                'Connection' : 'close' }
                r = requests.get(api_url, headers=headers)
                r_json = r.json()
                anime_title = r_json['data']['title']
                anime_eng_title = r_json['data']['title_english']
                anime_japanese_title = r_json['data']['title_japanese']
                anime_synonyms_title_list = r_json['data']['title_synonyms']
                anime_titles = [titles["title"] for titles in r_json['data']["titles"]]
                anime_titlesx2 = r_json['data']['titles']
                anime_synonyms_title = ''.join(anime_synonyms_title_list)
                anime_episodes = r_json['data']['episodes']
                anime_type = r_json['data']['type']
                anime_tags_all = [genres["name"] for genres in r_json['data']["genres"]]
                anime_tags = ', '.join(anime_tags_all)
                anime_status = r_json['data']['status']
                anime_airing = r_json['data']['airing']
                anime_hentai = r_json['data']['genres']
                studios = [studio["name"] for studio in r_json['data']["studios"]]
                ls = []
                for tits in r_json['data']["titles"]:
                    if tits['type'] == "Synonym" or tits['type'] == "English":
                        ls.append(tits['title'])
                        print(tits['title'])
                try:
                    anime_img = r_json['data']['images']['jpg']['large_image_url']
                except:
                    anime_img = r_json['data']['images']['jpg']['image_url']
                anime_popularity = r_json['data']['popularity']
                print('\nTitle: ' + str(anime_title) + '\n' + 'English Title: ' + str(anime_eng_title) + '\n' + 'Japanese Title: ' + str(anime_japanese_title) + '\n' + 'Synonyms Title: ' + str(anime_synonyms_title) + '\n' + 'Episodes: ' + str(anime_episodes) + '\n' + 'Type: ' + str(anime_type) + '\n' + 'Tags: ' + str(anime_tags) + '\n' + 'Status: ' + str(anime_status) + '\n' + "Image: " + str(anime_img) + "\n")
                return
            except:
                continue
        else:
            print('\nSomething goes wrong try again twice, check provided URL.\n\n')
        break

get_mal_info()