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
from kivy import clock

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
            color: [218, 10, 17, 1]
            text: root.instructions  
            font_size: 40 
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
        BoxLayout:
            orientation: 'horizontal'
            Label:
                id: stuff_we_own
                text: root.owned
            Label:
                id: display
                text: root.display
            BoxLayout:
                id: infoboxes
                orientation: 'vertical'
                BoxLayout:
                    id: infobox_1
                    orientation: 'horizontal'
                    Label:
                        id: adsnum
                        text: "Number of ads: " + root.ads
                    Button:
                        id: adsprice
                        text: "Buy an ad for: " + root.ads_price
                        on_press: root.buy_ad()
                BoxLayout:
                    id: infobox_2
                    orientation: 'horizontal'                   
                    Label:
                        text: "Middle Owned"
                    Button:
                        text: "Button Middle"   
                BoxLayout:
                    id: infobox_4
                    orientation: 'horizontal'                   
                    Label:
                        text: "Middle2 Owned"
                    Button:
                        text: "Button Middle2"               
                BoxLayout:
                    id: infobox_3
                    orientation: 'horizontal'    
                    Label:
                        text: "Bottom Owned"   
                    Button:
                        text: "Button Bottom"    
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'Read a Book'
                on_press: root.read_a_book()
                on_press: root.add_time(25)   
            Button:
                text: 'Workout'
                on_press: root.workout() 
                on_press: root.add_time(15)  
            Button:
                text: 'Job work' 
                on_press: root.get_paid()
                on_press: root.add_time(50)             
"""
Builder.load_string(formatting)


class PlayerStatistics:
    def __init__(self, strength=0, wisdom=0, time=0, ascension=0, jtier=10, liquidfunds=1000, myads=0):
        self.wallet = liquidfunds
        self.jobtier = jtier
        self.ascension = ascension
        self.time: int = time
        self.name: str = ""
        self.strength: int = strength
        self.wisdom: int = wisdom
        self.attributeDict = {"STR": self.strength, "WIS": self.wisdom}
        self.ads = myads

    def create_from_save(self):
        pass

    def set_name(self, username):
        self.name = username

    def increment_Strength(self, amount=1):
        self.strength = self.strength + amount

    def increment(self, parameter, amount=1):
        if self.attributeDict.__contains__(parameter):
            self.attributeDict[parameter] = self.attributeDict[parameter] + amount
        else:
            print("That Parameter does not exist")

    def next_ads_price(self):
        return self.ads + 0.1 * self.ads

    def increment_Wisdom(self, amount=1):
        self.wisdom = self.wisdom + amount
        pass

    def __str__(self):
        return str(
            "Name: " + self.name + "|" + "time: " + str(self.time)
            + "\n" + "Strength: " + str(self.strength)
            + "\n" + "Wisdom: " + str(self.wisdom)
            + "\n" + "$" + str(self.wallet)
        )

    def increment_Time(self, amount=1):
        # ads
        if self.time % 50 == 0:
            # add money to wallet from ad revenue
            self.wallet = self.wallet + self.ads * 5
        self.time = self.time + amount
        pass

    def get_paid(self):
        paycheck = self.calculate_paycheck()
        self.wallet = self.wallet + paycheck
        pass

    def calculate_paycheck(self):
        strength_modifier = .000001
        wisdom_modifier = .00001
        asc_modifier = (self.ascension + .1)
        money_from_strength = (self.strength * strength_modifier * asc_modifier)
        money_from_wisdom = self.wisdom * wisdom_modifier * asc_modifier
        paycheck = self.jobtier * (money_from_strength + money_from_wisdom)
        return paycheck

    def increment_ads(self):
        # Check if we have enough money
        price = self.next_ads_price()
        if self.wallet > price:
            # If we do, then remove from wallet
            self.wallet = self.wallet - price
            # add the ad
            self.ads = self.ads + 1
            # print("Incremented an add, total ads: " + str(self.ads))
        else:
            pass
        pass


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
            self.manager.get_screen('game').adsnum = str(self.data_stats.ads)
            self.manager.get_screen('game').adsprice = str(self.data_stats.next_ads_price())
            self.manager.current = 'game'
        else:
            self.instructions = self.fail_instructions
        pass

    pass


class MainGameScreen(Screen):
    def get_data(self) -> PlayerStatistics:
        return self.manager.get_screen('character').data_stats

    display = StringProperty("IF THIS IS SHOWING SOMETHING WENT WRONG")
    owned = StringProperty("IF THIS IS SHOWING SOMETHING WENT WRONG")
    ads = StringProperty("WRONG ads")
    ads_price = StringProperty("WRONG price")

    # StringProperty("Name: " + "Dummy" + "\n" + "Strength: " + str(Strength))
    def buy_ad(self):
        stats: PlayerStatistics = self.get_data()
        stats.increment_ads()
        # update the ad price on the button
        self.ads_price = str(stats.next_ads_price())
        # update the text of the number of ads
        self.ads = str(stats.ads)
        self.display = str(stats)

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

    def get_paid(self):
        stats: PlayerStatistics = self.get_data()
        stats.get_paid()
        self.display = str(stats)


class GUIApp(App):
    def build(self):
        return MyScreenManager()


# Entry point into the game
if __name__ == '__main__':
    GUIApp().run()
