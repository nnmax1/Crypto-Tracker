#Created By Nick N
import os
import data
import time 
import kivy
kivy.require("1.11.1")
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from data import Bitcoin
from data import Ethereum
from data import Litecoin as LTC
from data import Ripple as XRP
from data import Tether as USDT
from data import BitcoinCash as BCC
from datetime import date
from time import ctime

#load kivy files
Builder.load_file("./kv/main.kv")
Builder.load_file("./kv/buttons.kv")


#Container
class Container(GridLayout):
    display = ObjectProperty()

    def bitcoin_data(self):
        name = Bitcoin.get_name()
        price = Bitcoin.get_price()
        change= Bitcoin.get_change()
        pChange= Bitcoin.get_percentChange()
        mCap =  Bitcoin.get_marketCap()
        today = ctime()
        self.display.text = str(name + "\nPrice: $"+ price +"\nChange: "+change+ "\nPercent Change: "+pChange +"\nTotal Volume: $"+ mCap + "\nDate: " + today)
    def ethereum_data(self):
        name = Ethereum.get_name()
        price = Ethereum.get_price()
        change= Ethereum.get_change()
        pChange= Ethereum.get_percentChange()
        mCap = Ethereum.get_marketCap()
        today = ctime()
        self.display.text = str(name + "\nPrice: $"+ price +"\nChange: "+change+ "\nPercent Change: "+pChange +"\nTotal Volume: $"+ mCap + "\nDate: " + today)
    def litecoin_data(self):
        name = LTC.get_name()
        price = LTC.get_price()
        change= LTC.get_change()
        pChange= LTC.get_percentChange()
        mCap = LTC.get_marketCap()
        today = ctime()
        self.display.text = str(name + "\nPrice: $"+ price +"\nChange: "+change+ "\nPercent Change: "+pChange +"\nTotal Volume: $"+ mCap + "\nDate: " + today)
    def bitcoincash_data(self):
        name = BCC.get_name()
        price = BCC.get_price()
        change= BCC.get_change()
        pChange= BCC.get_percentChange()
        mCap = BCC.get_marketCap()
        today = ctime()
        self.display.text = str(name + "\nPrice: $"+ price +"\nChange: "+change+ "\nPercent Change: "+pChange +"\nTotal Volume: $"+ mCap + "\nDate: " + today)
    def ripple_data(self):
        name = XRP.get_name()
        price = XRP.get_price()
        change= XRP.get_change()
        pChange= XRP.get_percentChange()
        mCap = XRP.get_marketCap()
        today = ctime()
        self.display.text = str(name + "\nPrice: $"+ price +"\nChange: "+change+ "\nPercent Change: "+pChange +"\nTotal Volume: $"+ mCap + "\nDate: " + today)
    def tether_data(self):
        name = USDT.get_name()
        price = USDT.get_price()
        change= USDT.get_change()
        pChange= USDT.get_percentChange()
        mCap = USDT.get_marketCap()
        today = ctime()
        self.display.text = str(name + "\nPrice: $"+ price +"\nChange: "+change+ "\nPercent Change: "+pChange +"\nTotal Volume: $"+ mCap + "\nDate: " + today)
#buttons
class Bitcoin_Button(Button):
    pass
class Ethereum_Button(Button):
    pass
class Litecoin_Button(Button):
    pass
class BitcoinCash_Button(Button):
    pass
class Ripple_Button(Button):
    pass
class Tether_Button(Button):
    pass

#The App
class CryptoTrackerApp(App):
    def build(self):
        self.title = 'Cryptocurrency Tracker.'
        return Container()

#Run the App
if __name__ == "__main__":
	app = CryptoTrackerApp()
	CryptoTrackerApp().run()