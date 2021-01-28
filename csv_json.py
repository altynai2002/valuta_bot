import csv
import json

# элементы csv файла в словарь
with open('valuta.csv') as f:
    reader = csv.DictReader(f) # Определяет заголовки для столбцов
    rows = list(reader)
# сохраняет в красивом виде
with open('test.json', 'w+', encoding="utf-8") as f:
    json.dump(rows, f, indent=4, separators=(',', ': '), ensure_ascii=False)
    f.seek(0)# перенос на первую строку

# Функция для нахождения банка и лучшего курса валют
def value_of_valuta(valuta, pok_prod):
        file=open("test.json","r")
        data = json.load(file)

        if pok_prod == 'Покупка':
            if valuta == 'usd':
                data = {line['название']:line['usd_покупка'] for line in data}
            elif valuta == 'eur':
                data = {line['название']:line['eur_покупка'] for line in data}
            elif valuta == 'rub':
                data = {line['название']:line['rub_покупка'] for line in data}
            else:
                data = {line['название']:line['kzt_покупка'] if line['kzt_покупка'] != '—' else 0 for line in data }

            min_values = min(x for x in data.values() if x != 0) # находит минимальный
            final_data = {k:v for k,v in data.items() if v == min_values}
            a = '\n'.join(f'{k}, {v}' for k, v in final_data.items()) # соединение пары в строку
            print("Список банков", a)
            return  a

        elif pok_prod == 'Продажа':
            if valuta == 'usd':
                data = {line['название']:line['usd_продажа'] for line in data}
            elif valuta == 'eur':
                data = {line['название']:line['eur_продажа'] for line in data}
            elif valuta == 'rub':
                data = {line['название']:line['rub_продажа'] for line in data}
            else:
                data = {line['название']:line['kzt_продажа'] if line['kzt_продажа'] != '—' else 0 for line in data}

            max_values = max(x for x in data.values() if x != 0) # находит максимальный
            final_data = {k:v for k,v in data.items() if v == max_values}
            a = '\n'.join(f'{k}, {v}' for k, v in final_data.items()) # соединение пары в строку
            print("Список банков", a)
            return  a
