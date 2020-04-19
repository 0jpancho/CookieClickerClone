"""
The idea for this game is for the person to try and gain eternal life. The player starts at a certain age, and tries to
get more resources to become stronger and complete different challenges. The game restarts when the player dies.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

formatting = """
<MyScreenManager>:
    StartScreen:
    CreateNewCharacterScreen:
    MainGameScreen:
<StartScreen>:
    name: 'start'
    BoxLayout:
        orientation: 'vertical'
        Label:
            color: [1,0,0,1]
            text: root.instructions  
            font_size: 28
        TextInput:
            id: save_code
            font_size: 28
        Button:
            text: 'Press me to go to the Game Screen'
            on_press: root.load_or_start_new(save_code.text)
<CreateNewCharacterScreen>:
    name: 'character'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: instr
            size: self.texture_size
            text: root.instructions  
        TextInput:
            id: name
            font_size: 28
        Button:
            text: 'Enter a name for your character'
            on_press: root.create_character(name.text)
<MainGameScreen>:
    name: 'game'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: display
            text: root.display
        BoxLayout:
            Button:
                text: 'Read a Book'
                on_press: root.read_a_book()
                on_press: root.add_time(1)
            Button:
                text: 'Workout'
                on_press: root.workout()
                on_press: root.add_time(1) 
"""
Builder.load_string(formatting)


class PlayerStatistics:
    def __init__(self, strength=0, wisdom=0, timeHours=0, timeDays=0):
        self.timeHours: int = timeHours
        self.timeDays: float = timeDays
        self.name: str = ""
        self.strength: int = strength
        self.wisdom: int = wisdom
        self.attributeDict = {"STR": self.strength, "WIS": self.wisdom, "TIME": self.timeHours}

    def create_from_save(self):
        pass

    def set_name(self, username):
        self.name = username

    def increment_Strength(self, amount=1):
        self.strength = self.strength + amount

    def increment_Wisdom(self, amount=1):
        self.wisdom = self.wisdom + amount
        pass

    def increment(self, parameter, amount=1):
        if self.attributeDict.__contains__(parameter):
            self.attributeDict[parameter] = self.attributeDict[parameter] + amount
        else:
            print("That Parameter does not exist")

    def increment_Time(self, amount=1):
        self.timeHours = self.timeHours + amount
        self.timeDays = self.timeHours / 24
        pass

    def __str__(self):
        return str(
            "Name: " + self.name + " | " + "Time Spent (Hours): " + str(self.timeHours) + " " +
            "Time Spent (Days): {:0.2f}".format(self.timeDays)
            + "\n" + "Strength: " + str(self.strength)
            + "\n" + "Wisdom: " + str(self.wisdom)
        )


# Create the screen manager = sm
class MyScreenManager(ScreenManager, Widget):
    data = ObjectProperty(PlayerStatistics)


class StartScreen(Screen):
    instructions = StringProperty(str('''
    Welcome to this fun game!
    If you're new to the game or you want to start from the beginning just press the button!
    Otherwise, first paste in your save code, and then press the button to load the game.
    '''))

    def load_or_start_new(self, savedata=''):
        # For now we always start a new game
        if savedata != '':
            self.load_game(savedata)
        else:
            self.start_new_game()
        pass

    # Right now load and new do the same thing, but that might change in the future
    def load_game(self, data):
        self.manager.current = 'character'
        pass

    def start_new_game(self):
        self.manager.current = 'character'
        pass

    pass


class CreateNewCharacterScreen(Screen):
    instructions = StringProperty(str('''
        This world is unlike any world you've known before. Great Things await. But first, you'll need a name...
        '''))
    fail_instructions = StringProperty(str('''
        This world is unlike any world you've known before. Great Things await. But first, you'll need a name...
        FOOLISH MORTAL!!! ENTER A NAME FIRST BEFORE YOU CLICK THE BUTTON. 
        '''))
    data_stats: PlayerStatistics = ObjectProperty(PlayerStatistics)

    def create_character(self, username):
        if username != '':
            self.data_stats = PlayerStatistics()
            self.data_stats.set_name(username)
            self.manager.get_screen('game').display = str(self.data_stats)
            self.manager.current = 'game'
        else:
            self.instructions = self.fail_instructions
        pass

    pass


class MainGameScreen(Screen):
    def get_data(self) -> PlayerStatistics:
        return self.manager.get_screen('character').data_stats

    display = StringProperty("IF THIS IS SHOWING SOMETHING WENT WRONG")

    # StringProperty("Name: " + "Dummy" + "\n" + "Strength: " + str(Strength))
    def workout(self):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Strength(1)
        self.display = str(stats)

    def read_a_book(self):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Wisdom(1)
        self.display = str(stats)

    def add_time(self, amount):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Time(amount)
        self.display = str(stats)


class GUIApp(App):
    def build(self):
        return MyScreenManager()


# Entry point into the game
if __name__ == '__main__':
    GUIApp().run()
