from requests import get, post
from json import loads
from terminaltables import AsciiTable

input = input('Podaj nawę miasta: ')

def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = (get(url))
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura', 'Ciśnienie']
    ]
    
    for row in loads(response.text):
        if row['stacja'] in input:
            rows.append([
                row['stacja'], 
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie']
            ])

    table = AsciiTable(rows)
    print(table.table)

if __name__ == '__main__':
    print('Weather forecast for',input)
    main()