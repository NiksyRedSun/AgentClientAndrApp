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



Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "585")


LabelBase.register(name='Lucida Console',
                      fn_regular='C:\\repos\\AgentClientAndrApp\\lucida-console.ttf')



class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)



class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)


        self.grid = GridLayout(cols=1)
        self.grid.add_widget(Label(text="[color=03A062]Добро пожаловать в наше приложение про клиентов и агентов[/color]",
                                   size_hint=(1, 3.5), max_lines=10, text_size=(Window.width*0.8, None), halign="center",
                                   font_size=28, markup=True, font_name="Lucida Console"))

        self.agents_button = Button(text="[color=black]Агенты[/color]", font_size=32, font_name="Lucida Console",
                                    background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="")
        self.clients_button = Button(text="[color=black]Клиенты[/color]", font_size=32, font_name="Lucida Console",
                                     background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="")
        self.events_button = Button(text="[color=black]События[/color]", font_size=32, font_name="Lucida Console",
                                    background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="")
        self.exit_button = Button(text="[color=black]Выход[/color]", font_size=32, font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="")

        self.agents_button.bind(on_press=self.screen_transition_to_agents)
        self.clients_button.bind(on_press=self.screen_transition_to_clients)
        self.events_button.bind(on_press=self.screen_transition_to_events)
        self.exit_button.bind(on_press=self.exit)

        self.grid.add_widget(self.agents_button)
        self.grid.add_widget(self.clients_button)
        self.grid.add_widget(self.events_button)
        self.grid.add_widget(self.exit_button)


        self.add_widget(self.grid)


    def screen_transition_to_agents(self, *args):
        self.manager.current = "AgentsScreen"

    def screen_transition_to_clients(self, *args):
        self.manager.current = "ClientsScreen"

    def screen_transition_to_events(self, *args):
        self.manager.current = "EventsScreen"

    def exit(self, *args):
        App.get_running_app().stop()





class AgentsScreen(Screen):
    def __init__(self, **kwargs):
        super(AgentsScreen, self).__init__(**kwargs)


        self.grid = GridLayout(cols=1)

        self.scroll_view = ScrollView(size_hint=(1, 0.75), pos=(0, 0))

        self.back_button = Button(text="[color=black]Вернуться[/color]", size_hint=(1, .10), font_size=24, font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal="")
        self.back_button.bind(on_press=self.back)
        self.grid.add_widget(self.back_button)

        self.grid.add_widget(Label(text="[color=03A062]Наши агенты[/color]", size_hint=(1, .10), max_lines=10,
                                   text_size=(Window.width*0.8, None), halign="center",
                                   font_size=28, markup=True, font_name="Lucida Console"))

        #Здесь будет сетка для объектов
        self.agents_grid = GridLayout(cols=2, size_hint=(1, None), row_force_default=True, row_default_height=50)
        self.agents_grid.bind(minimum_height=self.agents_grid.setter("height"))

        for i in range(20):
            self.agents_grid.add_widget(Label(text=f"[color=03A062]Краткая информация об агенте с id: {i}[/color]", size_hint=(0.85, 1),
                                              text_size=(Window.width*0.75, None), halign="left", markup=True, font_name="Lucida Console"))

            self.agents_grid.add_widget(Button(text="[color=black]Инфо[/color]", size_hint=(0.15, 1), font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal=""))

        self.scroll_view.add_widget(self.agents_grid)
        self.grid.add_widget(self.scroll_view)
        self.add_widget(self.grid)



    def back(self, *args):
        self.manager.current = "MenuScreen"




class ClientsScreen(Screen):
    def __init__(self, **kwargs):
        super(ClientsScreen, self).__init__(**kwargs)

        self.grid = GridLayout(cols=1)

        self.scroll_view = ScrollView(size_hint=(1, 0.75), pos=(0, 0))

        self.back_button = Button(text="[color=black]Вернуться[/color]", size_hint=(1, .10), font_size=24,
                                  font_name="Lucida Console", background_color=(3/255, 168/255, 98/255, 0.8),
                                  markup=True, background_normal="")

        self.back_button.bind(on_press=self.back)
        self.grid.add_widget(self.back_button)

        self.grid.add_widget(Label(text="[color=03A062]Наши клиенты[/color]", size_hint=(1, .10), max_lines=10,
                                   text_size=(Window.width*0.8, None), halign="center",
                                   font_size=28, markup=True, font_name="Lucida Console"))

        #Здесь будет сетка для объектов
        self.clients_grid = GridLayout(cols=2, size_hint=(1, None), row_force_default=True, row_default_height=50)
        self.clients_grid.bind(minimum_height=self.clients_grid.setter("height"))

        for i in range(20):
            self.clients_grid.add_widget(Label(text=f"[color=03A062]Краткая информация о клиенте с id: {i}[/color]", size_hint=(0.85, 1),
                      text_size=(Window.width * 0.75, None), halign="left", markup=True, font_name="Lucida Console"))

            self.clients_grid.add_widget(Button(text="[color=black]Контракт[/color]", size_hint=(0.15, 1), font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal=""))

        self.scroll_view.add_widget(self.clients_grid)
        self.grid.add_widget(self.scroll_view)
        self.add_widget(self.grid)


    def back(self, *args):
        self.manager.current = "MenuScreen"




class AgentScreen(Screen):
    def __init__(self, **kwargs):
        super(AgentScreen, self).__init__(**kwargs)


        self.grid = GridLayout(cols=1)

        self.back_button = self.back_button = Button(text="[color=black]Вернуться[/color]", size_hint=(1, .10), font_size=24,
                                                     font_name="Lucida Console", background_color=(3/255, 168/255, 98/255, 0.8),
                                                     markup=True, background_normal="")
        self.back_button.bind(on_press=self.back)
        self.grid.add_widget(self.back_button)

        self.grid.add_widget(Label(text="Здесь будет информация по конкретному агенту", size_hint=(1, 1), max_lines=10,
                                   halign="center", valign="top", text_size=(200, self.height*5)))

        self.add_widget(self.grid)


    def back(self, *args):
        pass





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



class EventsScreen(Screen):
    def __init__(self, **kwargs):
        super(EventsScreen, self).__init__(**kwargs)

        self.grid = GridLayout(cols=1)

        self.scroll_view = ScrollView(size_hint=(1, 0.75), pos=(0, 0))

        self.back_button = self.back_button = Button(text="[color=black]Вернуться[/color]", size_hint=(1, .10),
                                                     font_size=24, font_name="Lucida Console", background_color=(3/255, 168/255, 98/255, 0.8),
                                                     markup=True, background_normal="")
        self.back_button.bind(on_press=self.back)
        self.grid.add_widget(self.back_button)

        self.grid.add_widget(Label(text="[color=03A062]События[/color]", size_hint=(1, .10), max_lines=10,
                                   text_size=(Window.width*0.8, None), halign="center",
                                   font_size=28, markup=True, font_name="Lucida Console"))

        # Здесь будет сетка для объектов
        self.events_grid = GridLayout(cols=2, size_hint=(1, None), row_force_default=True, row_default_height=50)
        self.events_grid.bind(minimum_height=self.events_grid.setter("height"))

        for i in range(20):
            self.events_grid.add_widget(Label(text=f"[color=03A062]Краткая информация о событии с id: {i}[/color]", size_hint=(0.85, 1),
                      text_size=(Window.width * 0.75, None), halign="left", markup=True, font_name="Lucida Console"))

            self.events_grid.add_widget(Button(text="[color=black]Отчет[/color]", size_hint=(0.15, 1), font_name="Lucida Console",
                                  background_color=(3/255, 168/255, 98/255, 0.8), markup=True, background_normal=""))

        self.scroll_view.add_widget(self.events_grid)
        self.grid.add_widget(self.scroll_view)
        self.add_widget(self.grid)


    def back(self, *args):
        self.manager.current = "MenuScreen"




class Application(App):
    def build(self):
        sm = ScreenManagement(transition=SlideTransition())

        sm.add_widget(MenuScreen(name="MenuScreen"))
        sm.add_widget(AgentsScreen(name="AgentsScreen"))
        sm.add_widget(AgentScreen(name="AgentScreen"))
        sm.add_widget(ClientsScreen(name="ClientsScreen"))
        sm.add_widget(ClientScreen(name="ClientScreen"))
        sm.add_widget(EventsScreen(name="EventsScreen"))

        return sm









if __name__ == "__main__":
    Application().run()
