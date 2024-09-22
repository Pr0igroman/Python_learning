from parser import Parser


def main():
    h = Parser("https://matchtv.ru/football/rpl/stats/2024-25?tour=c5e9d279-5a97-5a10-89bb-fffa4d405687", "score.csv")
    h.run()


if __name__ == '__main__':
    main()
