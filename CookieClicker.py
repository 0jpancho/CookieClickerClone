#!/usr/bin/kivy

from enum import Enum

import kivy
from kivy.app import App
from kivy.clock import Clock
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
            BoxLayout:
                orientation: 'vertical'
                Label: 
                    text: 'Buy a Pointer'
                Button:
                    text: root.pointerCostText
                    on_press: root.addPointers(1)
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'Increase the Base Multiplier'
                Button:
                    text: root.multiplierCostText
                    on_press: root.changeMultiplier(1)
            BoxLayout:
                orientation: 'vertical'
                Label: 
                    text: 'Auto Clicker +1'
                Button:
                    text: root.autoClickerCostText
                    on_press: root.addAutoClicker()
            BoxLayout:
                orientation: 'vertical'
                Label:
                    text: 'Save + Exit'                 
                Button:
"""
Builder.load_string(formatting)


class PlayerData:

    # Init normal values, as well as tracker variables for those values
    def __init__(self, cookies=0, pointers=1, multiplier=1, multiplierTracker=0, autoAddValue=0):
        self.cookies: int = cookies
        self.pointers: int = pointers
        self.multiplier: int = multiplier

        self.name: str = ""

        self.pointerCost: int = self.pointers * 20

        self.multiplierTracker: int = multiplierTracker
        self.multiplierCost: int = multiplierTracker * 100

        self.autoAddValue: int = autoAddValue

        Clock.schedule_interval(self.incrementCookies(self.getAutoAddVal(), True, False, False, False), 0.5)

    # Calculate new pointer cost
    def getNewPointerCost(self):
        self.pointerCost = self.pointers ** 3
        return self.pointerCost

    # Calculate new multiplier cost
    def getNewMultiplierCost(self):
        self.multiplierCost = (self.multiplierTracker ** 6) - self.multiplierTracker ** 5
        return self.multiplierCost

    # Increment autoAdd val by 1
    def incrementAutoVal(self):
        self.autoAddValue = self.autoAddValue + 1
        return self.autoAddValue

    # Calculate new auto clicker cost
    def getNewAutoValCost(self):
        self.autoAddValue = self.autoAddValue + 200
        return self.autoAddValue

    def getAutoAddVal(self):
        return self.autoAddValue

    def create_from_save(self):
        pass

    # Unused
    def importSaveData(self):
        pass

    # Set name value
    def setName(self, name=""):
        self.name = name

    # Main function for cookie addition. Booleans change purpose for function call
    # normalIncrement modifies self.cookies directly
    # addPointers increments the # of pointers + increases the cost per purchase
    # changeMultiplier adds an exponentially increasing base multiplier to (inputVal * pointers).
    # inputVal is static w/ value of 1
    def incrementCookies(self, inputVal=1, incrementByOne=False, incrementWithLogic=False, addPointers=False,
                         changeMultiplier=False):

        if addPointers:

            # Init tracker variable and set cost of next pointer
            cookieTracker = self.cookies

            # Calculate the theoretical new cost
            costDifference = cookieTracker - self.getNewPointerCost()

            # Set the current value of cookies to the cost difference if it is positive
            if costDifference >= 0:
                self.cookies = costDifference
                self.pointers = self.pointers + 1
                # Ignore if cost difference is negative: can't have negative cookies
            else:
                pass

        if changeMultiplier:

            # Init a temp tracking variables
            cookieTracker = self.cookies

            costDifference = cookieTracker - self.getNewMultiplierCost()

            # Set the current value of cookies to the cost difference if it is positive
            if costDifference >= 0:
                self.cookies = costDifference

                # Increment the multiplier tracker by 1
                self.multiplierTracker = self.multiplierTracker + 1

                # Arbitrary multiplier of 0.2 added to itself. To be edited later
                self.multiplier = self.multiplier + (0.5 * self.multiplierTracker)

            # Ignore if cost difference is negative: can't have negative cookies
            else:
                pass

        # Calculate a new value of cookies with logic added
        if incrementWithLogic:
            self.cookies = self.cookies + ((inputVal * self.pointers) * self.multiplier)
        pass

        if incrementByOne:
            self.cookies = self.cookies + inputVal

    def __str__(self):
        return str(
            self.name + " | " + "Cookies: " + str("{:.2f}").format(self.cookies) + "\n" +
            "# of Pointers: " + str(self.pointers) + "\n" +
            "Multiplier: " + str("{:.2f}".format(self.multiplier)) + "\n" +
            "Auto Clicker Value" + str(self.autoAddValue)
        )


class MyScreenManager(ScreenManager, Widget):
    data = ObjectProperty(PlayerData)


class WelcomeScreen(Screen):
    instructions = StringProperty(str('''
    Welcome to the Android's Cookie Clicker Clone! Hope you have a nice time.
    If it's your first time playing, press the button below to continue.
    If you wish to load a save, type your save code and continue
    '''))

    # Unfinished: Later issue
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
    Type in a name for yourself
    '''))

    failText = StringProperty(str('''
    Give yourself a name to continue to play you absolute dingus
    '''))

    data_stats: PlayerData = ObjectProperty(PlayerData)

    # Create a new save data if text field isn't blank
    def createSaveData(self, username):
        if username != '':
            self.data_stats = PlayerData()
            self.data_stats.setName(username)
            self.manager.get_screen('game').display = str(self.data_stats)
            self.manager.current = 'game'
        # Display failText until textbox is no longer empty
        else:
            self.defaultText = self.failText
        pass

    pass


class GameScreen(Screen):

    def get_data(self) -> PlayerData:
        return self.manager.get_screen('load').data_stats

    display = StringProperty("Blank is Bad")
    pointerCostText = StringProperty("Blank is Bad")
    multiplierCostText = StringProperty("Blank is Bad")
    autoClickerCostText = StringProperty("Blank is Bad")

    def addCookies(self, amount):
        stats: PlayerData = self.get_data()
        stats.incrementCookies(amount, False, True, False, False)
        self.display = str(stats)

    def addPointers(self, amount):
        stats: PlayerData = self.get_data()
        stats.incrementCookies(amount, False, False, True, False)
        self.display = str(stats)
        self.pointerCostText = str(stats.getNewPointerCost())

    def changeMultiplier(self, amount):
        stats: PlayerData = self.get_data()
        stats.incrementCookies(amount, False, False, False, True)
        self.display = str(stats)
        self.multiplierCostText = str(stats.getNewMultiplierCost())

    def addAutoClicker(self):
        stats: PlayerData = self.get_data()
        stats.incrementAutoVal()
        self.display = str(stats)
        self.autoClickerCostText = str(stats.getNewAutoValCost())


class CloneApp(App):

    def build(self):
        return MyScreenManager()


# Run the app
if __name__ == '__main__':
    CloneApp().run()
