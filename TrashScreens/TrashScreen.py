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
from reqs import get_all_active_agents, get_all_clients, get_all_events, get_client, get_all_trash, get_agent, \
    get_agent_contracts, get_uncover_event
import datetime
from functools import partial




class TrashScreen(Screen):
    def __init__(self, **kwargs):
        super(TrashScreen, self).__init__(**kwargs)

        self.grid = GridLayout(cols=1)

        self.scroll_view = ScrollView(size_hint=(1, 0.75), pos=(0, 0))


        self.grid.add_widget(Button(text="[color=black]Вернуться[/color]", size_hint=(1, .10), font_size=24,
                                  font_name="Lucida Console", background_color=(3/255, 168/255, 98/255, 0.8),
                                  markup=True, background_normal="", on_press=self.back))

        self.grid.add_widget(Label(text="[color=03A062]Претенденты[/color]", size_hint=(1, .10), max_lines=10,
                                   text_size=(Window.width*0.8, None), halign="center",
                                   font_size=28, markup=True, font_name="Lucida Console"))

        #Здесь будет сетка для объектов
        self.trash_grid = GridLayout(cols=2, size_hint=(1, None), row_force_default=True, row_default_height=70)
        self.trash_grid.bind(minimum_height=self.trash_grid.setter("height"))



        self.scroll_view.add_widget(self.trash_grid)
        self.grid.add_widget(self.scroll_view)
        self.add_widget(self.grid)


    def back(self, *args):
        self.manager.current = "MenuScreen"


    def on_pre_enter(self, *args):
        self.new_trash_list()


    def new_trash_list(self):
        self.trash_grid.clear_widgets()

        self.trash = get_all_trash()

        for trash in self.trash:
            self.trash_grid.add_widget(Label(text=f"[color=03A062]{trash['first_name']} \"{trash['nickname']}\" {trash['last_name']}\n"
                                                   f"Уровень снаряжения: {trash['equipment_level']}, опыт: {trash['exp']}[/color]", size_hint=(0.80, 1),
                                              text_size=(Window.width*0.75, None), halign="left", markup=True, font_name="Lucida Console"))

            self.trash_grid.add_widget(Button(text="[color=black]Убрать[/color]", size_hint=(0.20, 1), font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="", font_size=12,
                                                on_press=partial(self.screen_transition_to_trash_cleaning, trash["id"])))


    def screen_transition_to_trash_cleaning(self, *args):
        pass
        target = get_agent(args[0])
        kills = get_agent_contracts(args[0])
        uncover_event = get_uncover_event(args[0])
        print(uncover_event)
        uncov_target = get_client(uncover_event["client"])

        info = f"[color=03A062]Имя: {target['first_name']} {target['last_name']}\n" \
                f"Возраст: {target['age']}, статус: {int(target['status'])}\n" \
               f"Опыт: {target['exp']}, деньги: {target['money']}\n" \
               f"Уровень снаряжения: {target['equipment_level']}\n" \
               f"Контрактов: {len(kills)}\n\n" \
               f"Окончание членства: {datetime.datetime.fromtimestamp(uncover_event['time'])}\n\n" \
               f"{target['nickname']} был раскрыт пытаясь избавиться от {uncov_target['first_name']} {uncov_target['last_name']}\n\n" \
               f"Теперь нам нужно избавиться от него самого[/color]"


        self.manager.get_screen("TrashContractScreen").target = args[0]
        self.manager.get_screen("TrashCleaningScreen").nickname_label.text = f"[color=03A062]{target['nickname']}[/color]"
        self.manager.get_screen("TrashCleaningScreen").info_label.text = info
        self.manager.current = "TrashCleaningScreen"
