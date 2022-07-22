import requests


if __name__ == '__main__':
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    smartest = max(
        [hero for hero in response.json() if hero['name'] in ['Hulk', 'Captain America', 'Thanos']],
        key=lambda x: x['powerstats']['intelligence']
    )
    print(f'{smartest["name"]} - самый умный с IQ {smartest["powerstats"]["intelligence"]}')
