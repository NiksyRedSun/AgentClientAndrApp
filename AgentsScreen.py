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
from reqs import get_all_active_agents, get_all_clients, get_all_events, get_agent, get_agent_contracts
import datetime
from functools import partial

info_dict = {1: 'ножи, дубинки и скрытое огнестрельное оружие',
    2: 'пистолеты, кастеты и компактные пистолеты-пулеметы',
    3: 'полуавтоматические винтовки, топоры и дымовые гранаты',
    4: 'снайперские винтовки, широкие клинки и метательные ножи',
    5: 'штурмовые винтовки, бронебойные дротики и дробовики',
    6: 'специальные винтовки с подавлением звука, ядовитые стрелы и технологически продвинутые маскировочные устройства'}





class AgentsScreen(Screen):
    def __init__(self, **kwargs):
        super(AgentsScreen, self).__init__(**kwargs)


        self.grid = GridLayout(cols=1)

        self.scroll_view = ScrollView(size_hint=(1, 0.75), pos=(0, 0))


        self.grid.add_widget(Button(text="[color=black]Вернуться[/color]", size_hint=(1, .10), font_size=24, font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="", on_press=self.back))


        self.grid.add_widget(Label(text="[color=03A062]Наши агенты[/color]", size_hint=(1, .10), max_lines=10,
                                   text_size=(Window.width*0.8, None), halign="center",
                                   font_size=28, markup=True, font_name="Lucida Console"))

        #Здесь будет сетка для объектов
        self.agents_grid = GridLayout(cols=2, size_hint=(1, None), row_force_default=True, row_default_height=70)
        self.agents_grid.bind(minimum_height=self.agents_grid.setter("height"))

        self.new_agents_list()

        self.scroll_view.add_widget(self.agents_grid)
        self.grid.add_widget(self.scroll_view)
        self.add_widget(self.grid)



    def back(self, *args):
        self.manager.current = "MenuScreen"


    def on_pre_enter(self, *args):
        self.new_agents_list()


    def new_agents_list(self):
        self.agents_grid.clear_widgets()

        self.active_agents = get_all_active_agents()

        for agent in self.active_agents:
            self.agents_grid.add_widget(Label(text=f"[color=03A062]{agent['first_name']} \"{agent['nickname']}\" {agent['last_name']}\n"
                                                   f"Уровень снаряжения: {agent['equipment_level']}, опыт: {agent['exp']}[/color]", size_hint=(0.80, 1),
                                              text_size=(Window.width*0.75, None), halign="left", markup=True, font_name="Lucida Console"))

            self.agents_grid.add_widget(Button(text="[color=black]Инфо[/color]", size_hint=(0.20, 1), font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="",
                                               on_press=partial(self.screen_transition_to_agent, agent["id"]), font_size=14))



    def screen_transition_to_agent(self, *args):
        agent = get_agent(args[0])
        kills = get_agent_contracts(args[0])

        info = f"[color=03A062]{agent['first_name']} {agent['last_name']}\n" \
                f"Возраст: {agent['age']}, статус: {int(agent['status'])},\n" \
               f"опыт: {agent['exp']}, деньги: {agent['money']},\n\n" \
               f"Уровень снаряжения:\n" \
               f"{info_dict[agent['equipment_level']]}\n\n" \
               f"Контрактов: {len(kills)}\n\n" \
               f"Начало членства: {datetime.datetime.fromtimestamp(agent['start_membership'])}[/color]"


        self.manager.get_screen("AgentScreen").nickname_label.text = f"[color=03A062]{agent['nickname']}[/color]"
        self.manager.get_screen("AgentScreen").info_label.text = info
        self.manager.current = "AgentScreen"

