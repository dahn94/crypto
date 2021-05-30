import json
import requests
import time
import curses


def main(stdscr):
    while True:
        url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=USD'

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.text
            parsed = json.loads(data)
            btc_price = parsed['BTC']['USD']
            eth_price = parsed['ETH']['USD']
            ltc_price = parsed['LTC']['USD']

            stdscr.clear()
            stdscr.addstr(1, 0, f'# BTCUSD: {btc_price} \n# ETHUSD: {eth_price} \n# LTCUSD: {ltc_price}')
            stdscr.addstr(5, 0, 'Taxa de atualização: 4 seg')
            stdscr.addstr(7, 0, 'Pressione CTRL + C para sair.')
            stdscr.refresh()
            time.sleep(4)

        else:
            print('Sem conexão')


curses.wrapper(main)
