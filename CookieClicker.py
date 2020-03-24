#!/usr/bin/kivy

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('1.7.2')
'''
Builder.load_string("""
<Highest>:
    GridLayout:
        cols: 1
        Button:
            text: root.r1c2
            on_press: root.increment()
        # Button:
        #     text: root.r1c2
        #     on_press: root.increment()
""")



class Highest(Screen):
    count = 0
    r1c2 = StringProperty(str("Total Cookies: " + str(count)))

    def increment(self):
        self.count = self.count + 1

        self.r1c2 = str("Total Cookies: " + str(self.count))



'''

# Create the screen manager
# sm = ScreenManager()
# sm.add_widget(Highest(name='Cookies'))


class MyGrid(GridLayout):
    count = 0

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        count = 0
        r1c2 = (str("Total Cookies: " + str(count)))

        click = Button(text=r1c2, font_size=12)
        click.bind(on_press=self.increment)
        self.add_widget(click)

    def increment(self, instance):
        self.count = self.count + 1

        self.r1c2 = str("Total Cookies: " + str(self.count))


class MyApp(App):

    def build(self):
        # return Label(text = "Jancho Test")
        return MyGrid()


if __name__ == '__main__':
    MyApp().run()
