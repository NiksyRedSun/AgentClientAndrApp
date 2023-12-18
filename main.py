from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, WipeTransition, SwapTransition, CardTransition, SlideTransition, ShaderTransition
from reqs import get_all_active_agents, get_all_clients, get_all_events
import datetime
from MenuScreen import MenuScreen
from AgentsScreen import AgentsScreen
from AgentScreen import AgentScreen
from ClientScreen import ClientScreen
from ClientsScreen import ClientsScreen
from EventsScreen import EventsScreen

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "585")


LabelBase.register(name='Lucida Console',
                      fn_regular='C:\\repos\\AgentClientAndrApp\\lucida-console.ttf')



class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)





class Application(App):
    def build(self):
        sm = ScreenManagement(transition=SlideTransition())

        sm.add_widget(MenuScreen(name="MenuScreen"))
        sm.add_widget(AgentsScreen(name="AgentsScreen"))
        sm.add_widget(AgentScreen(name="AgentScreen"))
        sm.add_widget(ClientsScreen(name="ClientsScreen"))
        sm.add_widget(ClientScreen(name="ClientScreen"))
        sm.add_widget(EventsScreen(name="EventsScreen"))
        print(sm.screens)

        return sm





if __name__ == "__main__":
    Application().run()
