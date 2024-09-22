from bs4 import BeautifulSoup
import requests
import csv


class Parser:
    html = ""
    result = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def run(self):
        self.get_html()
        self.parsing_table()
        self.write_to_csv()

    def get_html(self):
        request = requests.get(self.url).text
        self.html = BeautifulSoup(request, "lxml")

    def parsing_table(self):
        table = self.html.find('table')
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            self.result.append(cols)
        # print(self.result[1:-1])

    def write_to_csv(self):
        with open(self.path, "w", newline='') as f:
            fieldnames = ["Место", "Команда", "Всего игр", "Побед", "Ничьих", "Поражений",
                          "Забитых мячей", "Пропущенных мячей", "Разница", "Всего очков"]
            writer = csv.writer(f, lineterminator="\r")
            writer.writerow(fieldnames)
            writer.writerows(self.result[1:-1])
