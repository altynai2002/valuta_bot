import csv
import requests
from bs4 import BeautifulSoup


main_url = 'https://valuta.kg/'

def get_html(url):
    res = requests.get(url) # делает запрос и хранит response
    return res.text # возвр-ет html код как текст

# В первую строку записываются ключи
with open('valuta.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(('название','usd_покупка','usd_продажа','eur_покупка','eur_продажа','rub_покупка','rub_продажа','kzt_покупка','kzt_продажа'))

# Добавление данных в строку
def write_csv(data):
    with open('valuta.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((
            data['название'],
            data['usd покупка'],
            data['usd продажа'],
            data['eur покупка'],
            data['eur продажа'],
            data['rub покупка'],
            data['rub продажа'],
            data['kzt покупка'],
            data['kzt продажа'],
        ))


def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser') # Сохраняет красивый код
    trs = soup.find('div', class_ = 'rate-list').find('table', class_='vl-list').find('tbody').find_all('tr') # нахождения тега tr
    list_= []
    for tr in trs:
        try:
            title = tr.find('div', class_='td-member__info').find('h4').find('a').text
            # print(title)
            
            valuta = tr.find_all('td', class_='td-rate')
            for td in valuta:
                # print(td)
                all_valutas = td.find('div', class_='td-rate__wrp').text.strip()
                list_.append(all_valutas) # внутри содержатся все валюты по порядку
            
            # к переменной присваивается элемент списка
            usd_pokupka = list_[0]
            usd_prodaja = list_[1]
            eur_pokupka = list_[2]
            eur_prodaja = list_[3]
            rub_pokupka = list_[4]
            rub_prodaja = list_[5]
            kzt_pokupka = list_[6]
            kzt_prodaja = list_[7]

            # создается словарь
            data = {
                    'название' : title,
                    "usd покупка" : usd_pokupka,
                    "usd продажа" : usd_prodaja,
                    "eur покупка" : eur_pokupka,
                    "eur продажа" : eur_prodaja,
                    "rub покупка" : rub_pokupka,
                    "rub продажа" : rub_prodaja,
                    "kzt покупка" : kzt_pokupka,
                    "kzt продажа" : kzt_prodaja,
                }
            list_.clear() # после записи в data список очищается
            # print(data)
        except:
            list_.append(0) 

        write_csv(data)



def main():
    html_text = get_html(main_url)
    all_links = get_all_links(html_text)
    

if __name__ == '__main__':
    main()