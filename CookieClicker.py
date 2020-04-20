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

# Create the screen manager
formatting = """
<MyScreenManager>:
    WelcomeScreen:
    LoadSaveScreen:
    GameScreen:
    
<WelcomeScreen>:
    name: 'welcome'
    
    BoxLayout:
        orientation: 'vertical'
        
        Label:
            text: root.instructions
            font_size: 20
            
        TextInput:
            id: save_code
            font_size: 20
            
        Button:
            text: 'Press to Continue'
            on_press: root.load_or_start_new(save_code.text)
            
<LoadSaveScreen>:
    name: 'load'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: instr
            size: self.texture_size
            text: root.defaultText
        TextInput:
            id: name
            font_size: 20
        Button:
            text: 'Enter a name for yourself'
            on_press: root.createSaveData(name.text)
            
<GameScreen>:
    name: 'game'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: display
            text: root.display
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'Click for Cookies'
                on_press: root.addCookies(1)
            Button:
                text:
            Button:
                text:
            Button:
                text:
            Button:
                text:
"""
Builder.load_string(formatting)


class PlayerData:

    def __init__(self, cookies=0, tier=1):
        self.cookies: int = cookies
        self.name: str = ""
        self.tier = tier

    def create_from_save(self):
        pass

    def importSaveData(self):
        pass

    def setName(self, name=""):
        self.name = name

    def incrementCookies(self, amount=1):
        self.cookies = self.cookies + amount
        pass

    def __str__(self):
        return str(
            self.name + " | " + "Cookies: " + str(self.cookies)
        )


class MyScreenManager(ScreenManager, Widget):
    data = ObjectProperty(PlayerData)


class WelcomeScreen(Screen):
    instructions = StringProperty(str('''
    Welcome to the Android's Cookie Clicker Clone! Hope you have a nice time.
    If it's your first time playing, press the button below to continue.
    If you wish to load a save, type your save code and continue
    '''))

    def load_or_start_new(self, savedata=''):
        # For now we always start a new game
        if savedata != '':
            self.loadSave(savedata)
        else:
            self.createNewSave()
        pass

    # Right now load and new do the same thing, but that might change in the future
    def loadSave(self, data):
        self.manager.current = 'load'
        pass

    def createNewSave(self):
        self.manager.current = 'load'
        pass

    pass


class LoadSaveScreen(Screen):
    defaultText = StringProperty(str('''
    Type in a name or nickname for yourself
    '''))

    failText = StringProperty(str('''
    ERROR: Give yourself a name to continue to play
    '''))

    data_stats: PlayerData = ObjectProperty(PlayerData)

    def createSaveData(self, username):
        if username != '':
            self.data_stats = PlayerData()
            self.data_stats.setName(username)
            self.manager.get_screen('game').display = str(self.data_stats)
            self.manager.current = 'game'
        else:
            self.defaultText = self.failText
        pass

    pass


class GameScreen(Screen):

    def get_data(self) -> PlayerData:
        return self.manager.get_screen('load').data_stats

    display = StringProperty("IF THIS IS SHOWING SOMETHING WENT WRONG")

    def addCookies(self, amount):
        stats: PlayerData = self.get_data()
        stats.incrementCookies(amount)
        self.display = str(stats)


class MyApp(App):

    def build(self):
        return MyScreenManager()


# Run the app
if __name__ == '__main__':
    MyApp().run()
