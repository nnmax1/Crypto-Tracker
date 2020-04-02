import urllib3
from bs4 import BeautifulSoup

#initialize the html parser
url = "https://finance.yahoo.com/cryptocurrencies"
http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data.decode('utf-8'), features="html.parser")

class Bitcoin: 
    def get_name():
        bitcoin_nameBox= soup.find("a", attrs={"title":"Bitcoin USD", "class":"Fw(600)"})
        bitcoin_name = bitcoin_nameBox.text.strip()
        return bitcoin_name
    def get_price():
        bitcoin_priceBox = soup.find("span", attrs={"class":"Trsdu(0.3s)", "data-reactid":"92"})
        bitcoin_price=bitcoin_priceBox.text.strip()
        return bitcoin_price
    def get_change():
        bitcoin_changeBox = soup.find("span", attrs={"data-reactid":"94"})
        bitcoin_change = bitcoin_changeBox.text.strip()
        return bitcoin_change
    def get_percentChange():
        bitcoin_pChangeBox = soup.find("span", attrs={"data-reactid":"96"})
        bitcoin_percentChange = bitcoin_pChangeBox.text.strip()
        return bitcoin_percentChange
    def get_marketCap():
        bitcoin_marketCapBox = soup.find("span", attrs={"class":"Trsdu(0.3s)", "data-reactid":"98"})
        bitcoin_marketCap = bitcoin_marketCapBox.text.strip()
        return bitcoin_marketCap


class Ethereum:
    def get_name():
        eth_nameBox=soup.find("a", attrs={"title":"Ethereum USD","class":"Fw(600)","data-reactid":"119"}) 
        eth_name=eth_nameBox.text.strip()
        return eth_name
    def get_price():
        eth_priceBox = soup.find("span", attrs={"class":"Trsdu(0.3s)", "data-reactid":"124"})
        eth_price= eth_priceBox.text.strip()
        return eth_price
    def get_change():
        eth_changeBox = soup.find("span", attrs={"data-reactid":"126"})
        eth_change = eth_changeBox.text.strip()
        return eth_change
    def get_percentChange():
        eth_pChangeBox = soup.find("span", attrs={"data-reactid":"128"})
        eth_percentChange = eth_pChangeBox.text.strip()
        return eth_percentChange
    def get_marketCap():
        eth_marketCapBox = soup.find("span", attrs={"class":"Trsdu(0.3s)", "data-reactid":"130"})
        eth_marketCap = eth_marketCapBox.text.strip()
        return eth_marketCap


class Ripple:
    def get_name():
        XRP_nameBox=soup.find("a", attrs={"title":"XRP USD","class":"Fw(600)","data-reactid":"151"}) 
        XRP_name=XRP_nameBox.text.strip()
        return XRP_name
    def get_price():
        XRP_priceBox = soup.find("span", attrs={"class":"Trsdu(0.3s)","data-reactid":"156"})
        XRP_price= XRP_priceBox.text.strip()
        return XRP_price
    def get_change():
        XRP_changeBox = soup.find("span", attrs={"data-reactid":"158"})
        XRP_change = XRP_changeBox.text.strip()
        return XRP_change
    def get_percentChange():
        XRP_pChangeBox = soup.find("span", attrs={"data-reactid":"160"})
        XRP_percentChange = XRP_pChangeBox.text.strip()
        return XRP_percentChange
    def get_marketCap():
        XRP_marketCapBox = soup.find("span", attrs={"data-reactid":"162"})
        XRP_marketCap = XRP_marketCapBox.text.strip()
        return XRP_marketCap
 
class Tether:
    def get_name():
        USDT_nameBox=soup.find("a", attrs={"title":"Tether USD","class":"Fw(600)","data-reactid":"183"}) 
        USDT_name=USDT_nameBox.text.strip()
        return USDT_name
    def get_price():
        USDT_priceBox = soup.find("span", attrs={"data-reactid":"188"})
        USDT_price= USDT_priceBox.text.strip()
        return USDT_price
    def get_change():
        USDT_changeBox = soup.find("span", attrs={"data-reactid":"190"})
        USDT_change = USDT_changeBox.text.strip()
        return USDT_change
    def get_percentChange():
        USDT_pChangeBox = soup.find("span", attrs={"data-reactid":"192"})
        USDT_percentChange = USDT_pChangeBox.text.strip()
        return USDT_percentChange
    def get_marketCap():
        USDT_marketCapBox = soup.find("span", attrs={ "data-reactid":"194"})
        USDT_marketCap = USDT_marketCapBox.text.strip()
        return USDT_marketCap
 

class Litecoin:
    def get_name():
        LTC_nameBox=soup.find("a", attrs={"title":"Litecoin USD","class":"Fw(600)","data-reactid":"247"}) 
        LTC_name=LTC_nameBox.text.strip()
        return LTC_name
    def get_price():
        LTC_priceBox = soup.find("span", attrs={"data-reactid":"252"})
        LTC_price= LTC_priceBox.text.strip()
        return LTC_price
    def get_change():
        LTC_changeBox = soup.find("span", attrs={"data-reactid":"254"})
        LTC_change = LTC_changeBox.text.strip()
        return LTC_change
    def get_percentChange():
        LTC_pChangeBox = soup.find("span", attrs={"data-reactid":"256"})
        LTC_percentChange = LTC_pChangeBox.text.strip()
        return LTC_percentChange
    def get_marketCap():
        LTC_marketCapBox = soup.find("span", attrs={ "data-reactid":"258"})
        LTC_marketCap = LTC_marketCapBox.text.strip()
        return LTC_marketCap
    #member vars
    name = get_name()
    price = get_price()
    change=get_change()
    percentC=get_percentChange()
    mCap=get_marketCap()

class BitcoinCash:
    def get_name():
        BTCcash_nameBox=soup.find("a", attrs={"title":"Bitcoin Cash USD","class":"Fw(600)","data-reactid":"215"}) 
        BTCcash_name=BTCcash_nameBox.text.strip()
        return BTCcash_name
    def get_price():
        BTCcash_priceBox = soup.find("span", attrs={"data-reactid":"220"})
        BTCcash_price= BTCcash_priceBox.text.strip()
        return BTCcash_price
    def get_change():
        BTCcash_changeBox = soup.find("span", attrs={"data-reactid":"222"})
        BTCcash_change = BTCcash_changeBox.text.strip()
        return BTCcash_change
    def get_percentChange():
        BTCcash_pChangeBox = soup.find("span", attrs={"data-reactid":"224"})
        BTCcash_percentChange = BTCcash_pChangeBox.text.strip()
        return BTCcash_percentChange
    def get_marketCap():
        BTCcash_marketCapBox = soup.find("span", attrs={ "data-reactid":"226"})
        BTCcash_marketCap = BTCcash_marketCapBox.text.strip()
        return BTCcash_marketCap


