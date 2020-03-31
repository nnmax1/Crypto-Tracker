#Nick N(github username: nnmax1)
import urllib3
import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter.messagebox import *
from bs4 import BeautifulSoup
from datetime import datetime


#init the web parser tool
url = "https://finance.yahoo.com/cryptocurrencies"
http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data.decode('utf-8'), features="html.parser")


#Classes for each cryptocurrency contain member function that
#return data parsed from Yahoo Finance

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

#Rusns the GUI application
def run_app():
    root = tk.Tk()
    #font specifier
    myFont = font.Font(family='Helvetica')
    myFont = font.Font(size=30)
    #title
    title = tk.Label(root, text = 'Cryptocurrency Tracker')
    title['font']=myFont
    title.pack()
    #some spacing
    space = tk.Label(root, text = "\n\n")
    space.pack()
    #buttons for each currency
    btn1=Button(root, text = "Bitcoin", command=show_btc)
    btn1['font']=myFont
    btn1.pack(side=tk.TOP)
    btn2=tk.Button(root, text = "Ethereum",command=show_eth)
    btn2['font']=myFont
    btn2.pack(side=tk.TOP)
    btn3=tk.Button(root, text = "Ripple", command=show_ripple)
    btn3['font']=myFont
    btn3.pack(side=tk.TOP)
    btn4=tk.Button(root, text = "Tether" ,command=show_tether)
    btn4['font']=myFont
    btn4.pack(side=tk.TOP)
    btn5=tk.Button(root, text = "Litecoin", command=show_litecoin)
    btn5['font']=myFont
    btn5.pack(side=tk.TOP)
    btn6=tk.Button(root, text = "Bitcoin Cash", command=show_BTCcash)
    btn6['font']=myFont
    btn6.pack(side=tk.TOP)
    #spacing
    w = tk.Label(root,text="\n\n\n")
    w.pack()
    #Quit button
    quitButton = tk.Button(root,text="QUIT", fg="red",command=quit)
    quitButton.pack(side=tk.LEFT)
    tk.mainloop()

#Below are the actions for each button in the run_app() function:

def show_btc():
    root = tk.Tk()
    fontStyle = font.Font(family="Helvetica", size=50)
    n = Bitcoin.get_name()
    p = "Price(intraday): $" + Bitcoin.get_price()
    c= "Change: "+Bitcoin.get_change()
    pc = "Percent Change: "+Bitcoin.get_percentChange()
    mc = "Market Cap: $"+Bitcoin.get_marketCap()
    item=tk.Label(root, text = datetime.now(), font=fontStyle)
    item.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    item1=tk.Label(root,  text = n , font=fontStyle)
    item1.pack(side=tk.TOP)
    item2=tk.Label(root,  text = p ,font=fontStyle)
    item2.pack(side=tk.TOP)
    item3=tk.Label(root,  text = c ,font=fontStyle)
    item3.pack(side=tk.TOP)
    item4=tk.Label(root,  text = pc ,font=fontStyle)
    item4.pack(side=tk.TOP)
    item5=tk.Label(root,  text = mc ,font=fontStyle)
    item5.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    quitButton = tk.Button(root,text="QUIT", fg="red",command=quit)
    quitButton.pack(side=tk.LEFT)
    tk.mainloop()


def show_eth():
    root = tk.Tk()
    fontStyle = font.Font(family="Helvetica", size=50)
    n = Ethereum.get_name()
    p = "Price(intraday): $" + Ethereum.get_price()
    c= "Change: "+Ethereum.get_change()
    pc = "Percent Change: "+Ethereum.get_percentChange()
    mc = "Market Cap: $"+Ethereum.get_marketCap()
    item=tk.Label(root, text = datetime.now(), font=fontStyle)
    item.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    item1=tk.Label(root,  text = n , font=fontStyle)
    item1.pack(side=tk.TOP)
    item2=tk.Label(root,  text = p ,font=fontStyle)
    item2.pack(side=tk.TOP)
    item3=tk.Label(root,  text = c ,font=fontStyle)
    item3.pack(side=tk.TOP)
    item4=tk.Label(root,  text = pc ,font=fontStyle)
    item4.pack(side=tk.TOP)
    item5=tk.Label(root,  text = mc ,font=fontStyle)
    item5.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    quitButton = tk.Button(root,text="QUIT", fg="red",command=quit)
    quitButton.pack(side=tk.LEFT)
    tk.mainloop()

def show_tether():
    root = tk.Tk()
    fontStyle = font.Font(family="Helvetica", size=50)
    n = Tether.get_name()
    p = "Price(intraday): $" + Tether.get_price()
    c= "Change: "+Tether.get_change()
    pc = "Percent Change: "+Tether.get_percentChange()
    mc = "Market Cap: $"+Tether.get_marketCap()
    item=tk.Label(root, text = datetime.now(), font=fontStyle)
    item.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    item1=tk.Label(root,  text = n , font=fontStyle)
    item1.pack(side=tk.TOP)
    item2=tk.Label(root,  text = p ,font=fontStyle)
    item2.pack(side=tk.TOP)
    item3=tk.Label(root,  text = c ,font=fontStyle)
    item3.pack(side=tk.TOP)
    item4=tk.Label(root,  text = pc ,font=fontStyle)
    item4.pack(side=tk.TOP)
    item5=tk.Label(root,  text = mc ,font=fontStyle)
    item5.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    quitButton = tk.Button(root,text="QUIT", fg="red",command=quit)
    quitButton.pack(side=tk.LEFT)
    tk.mainloop()

def show_ripple():
    root = tk.Tk()
    fontStyle = font.Font(family="Helvetica", size=50)
    n = Ripple.get_name()
    p = "Price(intraday): $" + Ripple.get_price()
    c= "Change: "+Ripple.get_change()
    pc = "Percent Change: "+Ripple.get_percentChange()
    mc = "Market Cap: $"+Ripple.get_marketCap()
    item=tk.Label(root, text = datetime.now(), font=fontStyle)
    item.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    item1=tk.Label(root,  text = n , font=fontStyle)
    item1.pack(side=tk.TOP)
    item2=tk.Label(root,  text = p ,font=fontStyle)
    item2.pack(side=tk.TOP)
    item3=tk.Label(root,  text = c ,font=fontStyle)
    item3.pack(side=tk.TOP)
    item4=tk.Label(root,  text = pc ,font=fontStyle)
    item4.pack(side=tk.TOP)
    item5=tk.Label(root,  text = mc ,font=fontStyle)
    item5.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    quitButton = tk.Button(root,text="QUIT", fg="red",command=quit)
    quitButton.pack(side=tk.LEFT)
    tk.mainloop()

def show_litecoin():
    root = tk.Tk()
    fontStyle = font.Font(family="Helvetica", size=50)
    n = Litecoin.get_name()
    p = "Price(intraday): $" + Litecoin.get_price()
    c= "Change: "+Litecoin.get_change()
    pc = "Percent Change: "+Litecoin.get_percentChange()
    mc = "Market Cap: $"+Litecoin.get_marketCap()
    item=tk.Label(root, text = datetime.now(), font=fontStyle)
    item.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    item1=tk.Label(root,  text = n , font=fontStyle)
    item1.pack(side=tk.TOP)
    item2=tk.Label(root,  text = p ,font=fontStyle)
    item2.pack(side=tk.TOP)
    item3=tk.Label(root,  text = c ,font=fontStyle)
    item3.pack(side=tk.TOP)
    item4=tk.Label(root,  text = pc ,font=fontStyle)
    item4.pack(side=tk.TOP)
    item5=tk.Label(root,  text = mc ,font=fontStyle)
    item5.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    quitButton = tk.Button(root,text="QUIT", fg="red",command=quit)
    quitButton.pack(side=tk.LEFT)
    tk.mainloop()

def show_BTCcash():
    root = tk.Tk()
    fontStyle = font.Font(family="Helvetica", size=50)
    n = BitcoinCash.get_name()
    p = "Price(intraday): $" + BitcoinCash.get_price()
    c= "Change: "+BitcoinCash.get_change()
    pc = "Percent Change: "+BitcoinCash.get_percentChange()
    mc = "Market Cap: $"+BitcoinCash.get_marketCap()
    item=tk.Label(root, text = datetime.now(), font=fontStyle)
    item.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    item1=tk.Label(root,  text = n , font=fontStyle)
    item1.pack(side=tk.TOP)
    item2=tk.Label(root,  text = p ,font=fontStyle)
    item2.pack(side=tk.TOP)
    item3=tk.Label(root,  text = c ,font=fontStyle)
    item3.pack(side=tk.TOP)
    item4=tk.Label(root,  text = pc ,font=fontStyle)
    item4.pack(side=tk.TOP)
    item5=tk.Label(root,  text = mc ,font=fontStyle)
    item5.pack(side=tk.TOP)
    space = tk.Label(root, text = "\n")
    space.pack()
    quitButton = tk.Button(root,text="QUIT", fg="red",command=quit)
    quitButton.pack(side=tk.LEFT) 
    tk.mainloop()



#execution
run_app()
