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
from reqs import get_all_active_agents, get_all_clients, get_all_events, get_agent, get_agent_contracts, get_client
import datetime
from functools import partial

class ContractAgentsScreen(Screen):
    def __init__(self, **kwargs):
        super(ContractAgentsScreen, self).__init__(**kwargs)


        self.grid = GridLayout(cols=1)

        self.scroll_view = ScrollView(size_hint=(1, 0.75), pos=(0, 0))


        self.grid.add_widget(Button(text="[color=black]Вернуться[/color]", size_hint=(1, .10), font_size=24, font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="", on_press=self.back))


        self.grid.add_widget(Label(text="[color=03A062]Исполнитель контракта[/color]", size_hint=(1, .10), max_lines=10,
                                   text_size=(Window.width*0.8, None), halign="center",
                                   font_size=24, markup=True, font_name="Lucida Console"))

        #Здесь будет сетка для объектов
        self.agents_grid = GridLayout(cols=2, size_hint=(1, None), row_force_default=True, row_default_height=70)
        self.agents_grid.bind(minimum_height=self.agents_grid.setter("height"))



        self.scroll_view.add_widget(self.agents_grid)
        self.grid.add_widget(self.scroll_view)
        self.add_widget(self.grid)



    def back(self, *args):
        self.manager.current = "ClientScreen"


    def on_pre_enter(self, *args):
        self.new_agents_list()


    def new_agents_list(self):
        self.agents_grid.clear_widgets()

        self.active_agents = get_all_active_agents()

        for agent in self.active_agents:
            self.agents_grid.add_widget(Label(text=f"[color=03A062]{agent['first_name']} \"{agent['nickname']}\" {agent['last_name']}\n"
                                                   f"Уровень снаряжения: {agent['equipment_level']}, опыт: {agent['exp']}[/color]", size_hint=(0.80, 1),
                                              text_size=(Window.width*0.75, None), halign="left", markup=True, font_name="Lucida Console"))

            self.agents_grid.add_widget(Button(text="[color=black]Контракт[/color]", size_hint=(0.20, 1), font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="",
                                on_press=partial(self.screen_transition_to_contract, agent["id"]), font_size=12))


    def screen_transition_to_contract(self, *args):
        pass
        agent = get_agent(args[0])
        client = get_client(self.manager.get_screen("ContractScreen").client)
        kills = get_agent_contracts(args[0])

        info = f"[color=03A062]Агент: {agent['nickname']}\n" \
               f"Имя: {agent['first_name']} {agent['last_name']}\n" \
               f"Опыт: {agent['exp']}\n" \
               f"Уровень снаряжения: {agent['equipment_level']}\n" \
               f"Предшествующих контрактов: {len(kills)}\n\n" \
               f"Клиент: {client['first_name']} {client['last_name']}\n" \
               f"Опыт за убийство: {client['exp']}\n" \
               f"Награда за убийство: {client['price']}\n" \
               f"Уровень защиты: {client['security_level']}[/color]"


        self.manager.get_screen("ContractScreen").info_label.text = info
        self.manager.get_screen("ContractScreen").agent = args[0]
        self.manager.current = "ContractScreen"



