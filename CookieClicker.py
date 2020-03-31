#!/usr/bin/kivy

from enum import Enum

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

kivy.require('1.7.2')


class ChangeOperators(Enum):
    ADD = 0
    SUBTRACT = 1
    MULTIPLY = 2
    DIVIDE = 3


# Create the screen manager
formatting = """
<MyScreenManager>:
    GameScreen:
<GameScreen>:
    name: 'game'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: display
            text: root.display
        BoxLayout:
            Button:
                text: 'Click for Cookies'
                on_press: root.addCookies()
"""
Builder.load_string(formatting)


class PlayerData:

    def __init__(self, cookies):
        self.cookies = cookies
        self.name: str = ""
        self.attributeDict = {"COOKIES": self.cookies}

    def importSaveData(self):
        pass

    def setName(self, name=""):
        pass

    def addCookies(self, amount=1):
        self.cookies = self.cookies + amount

    def __str__(self):
        return str(
            "\n" + "Cookies: " + str(self.cookies)
        )


class MyScreenManager(ScreenManager, Widget):
    data = ObjectProperty(PlayerData)


class GameScreen(Screen):
    data_stats: PlayerData = ObjectProperty(PlayerData)

    def loadData(self):

        self.data_stats = PlayerData()
        self.manager.get_screen('game').display = str(self.data_stats)

    def get_data(self) -> PlayerData:
        return self.manager.get_screen('game').data_stats

    display = StringProperty("IF THIS IS SHOWING SOMETHING WENT WRONG")

    def addCookies(self):
        stats: PlayerData = self.get_data()
        stats.addCookies(1)
        self.display = str(stats)


class MyApp(App):

    def build(self):
        return MyScreenManager()


# Run the app
if __name__ == '__main__':
    MyApp().run()
