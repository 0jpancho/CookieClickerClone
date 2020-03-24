#!/usr/bin/kivy
import kivy
from kivy.properties import StringProperty
from kivy.uix.label import Label

kivy.require('1.7.2')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

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
    r1c2 = StringProperty(str("Currency: " + str(count)))

    def increment(self):
        self.count = self.count + 1

        self.r1c2 = str("Currency: " + str(self.count))


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Highest(name='Highest'))


class MyApp(App):

    def build(self):
        #return Label(text = "Jancho Test")
        return sm


if __name__ == '__main__':
    MyApp().run()
