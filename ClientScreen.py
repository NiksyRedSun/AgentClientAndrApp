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



class ClientScreen(Screen):
    def __init__(self, **kwargs):
        super(ClientScreen, self).__init__(**kwargs)

        self.grid = GridLayout(cols=1)

        self.back_button = self.back_button = Button(text="[color=black]Вернуться[/color]", size_hint=(1, .10),
                                                     font_size=24, font_name="Lucida Console", background_color=(3/255, 168/255, 98/255, 0.8),
                                                     markup=True, background_normal="")
        self.back_button.bind(on_press=self.back)
        self.grid.add_widget(self.back_button)



        self.grid.add_widget(Label(text="Здесь будет информация по конкретному клиенту", size_hint=(1, 1),
                                   max_lines=10, halign="center", valign="top", text_size=(200, self.height*5)))

        self.add_widget(self.grid)


    def back(self, *args):
        pass
