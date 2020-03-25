#!/usr/bin/kivy

from enum import Enum

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('1.7.2')


class ChangeOperators(Enum):
    ADD = 0
    SUBTRACT = 1
    MULTIPLY = 2
    DIVIDE = 3


# Create the screen manager
# sm = ScreenManager()
# sm.add_widget(Highest(name='Cookies'))


class MyGrid(GridLayout):
    count = 0

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        # Initialize count to 0
        count = 0

        # Replace r1c2 with more descriptive identifier
        # set value cookie amount to the count
        cookie_amount = str("Total Cookies: " + str(count))

        # create a Button using the cookie amount and a font size (I pick 48 because I'm old and my eyes can't see well)
        # Change name of button from click to cookiebutton
        self.cookiebutton = Button(text=cookie_amount, font_size=48)

        # Bind something to take place when the button is pressed
        self.cookiebutton.bind(on_press=self.increment)

        # Add widget to screen so that button is displayed
        self.add_widget(self.cookiebutton)

    def increment(self, instance):
        self.count = self.count + 1
        self.cookiebutton.text = str("Total Cookies: " + str(self.count))

    def changeTotal(self, changeOperator, value):
        if changeOperator is ChangeOperators.ADD:
            self.count = self.count + value

        if changeOperator is ChangeOperators.SUBTRACT:
            self.count = self.count - value

        if changeOperator is ChangeOperators.MULTIPLY:
            self.count = self.count * value

        if changeOperator is ChangeOperators.DIVIDE:
            self.count = self.count * value


class MyApp(App):

    def build(self):
        # return Label(text = "Jancho Test")
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
