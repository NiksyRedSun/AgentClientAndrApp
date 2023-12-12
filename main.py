from kivy.app import App
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



class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)



class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)


        self.grid = GridLayout(cols=1)
        self.grid.add_widget(Label(text="Добро пожаловать в наше приложение про клиентов и агентов", size_hint=(1, 3.5), max_lines=10, text_size=(200, None), halign="center"))

        self.agents_button = Button(text="Агенты", font_size=32)
        self.clients_button = Button(text="Клиенты", font_size=32)
        self.events_button = Button(text="События", font_size=32)
        self.exit_button = Button(text="Выход", font_size=32)

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


        self.back_button = Button(text="Вернуться", font_size=32, size_hint=(1, .5))
        self.back_button.bind(on_press=self.back)
        self.grid.add_widget(self.back_button)


        self.grid.add_widget(Label(text="Здесь будет список агентов", size_hint=(1, 3.5), max_lines=10, halign="center", valign="top", text_size=(200, 500)))

        self.add_widget(self.grid)


    def back(self, *args):
        self.manager.current = "MenuScreen"




class ClientsScreen(Screen):
    def __init__(self, **kwargs):
        super(ClientsScreen, self).__init__(**kwargs)

        self.grid = GridLayout(cols=1)

        self.back_button = Button(text="Вернуться", font_size=32, size_hint=(1, .5))
        self.back_button.bind(on_press=self.back)
        self.grid.add_widget(self.back_button)

        self.grid.add_widget(Label(text="Здесь будет список клиентов", size_hint=(1, 3.5), max_lines=10, halign="center", valign="top", text_size=(200, 500)))

        self.add_widget(self.grid)


    def back(self, *args):
        self.manager.current = "MenuScreen"




class AgentScreen(Screen):
    def __init__(self, **kwargs):
        super(AgentScreen, self).__init__(**kwargs)




        self.grid = GridLayout(cols=1)

        self.back_button = Button(text="Вернуться", font_size=32, size_hint=(1, .5))
        self.back_button.bind(on_press=self.back)
        self.grid.add_widget(self.back_button)

        self.grid.add_widget(Label(text="Здесь будет информация по конкретному агенту", size_hint=(1, 3.5), max_lines=10, halign="center", valign="top", text_size=(200, 500)))

        self.add_widget(self.grid)


    def back(self, *args):
        pass





class ClientScreen(Screen):
    def __init__(self, **kwargs):
        super(ClientScreen, self).__init__(**kwargs)

        self.grid = GridLayout(cols=1)

        self.back_button = Button(text="Вернуться", font_size=32, size_hint=(1, .5))
        self.back_button.bind(on_press=self.back)
        self.grid.add_widget(self.back_button)

        self.grid.add_widget(Label(text="Здесь будет информация по конкретному клиенту", size_hint=(1, 3.5), max_lines=10, halign="center", valign="top", text_size=(200, 500)))

        self.add_widget(self.grid)


    def back(self, *args):
        pass



class EventsScreen(Screen):
    def __init__(self, **kwargs):
        super(EventsScreen, self).__init__(**kwargs)

        self.grid = GridLayout(cols=1)

        self.back_button = Button(text="Вернуться", font_size=32, size_hint=(1, .5))
        self.back_button.bind(on_press=self.back)
        self.grid.add_widget(self.back_button)

        self.grid.add_widget(Label(text="Здесь будет информация по всем событиям", size_hint=(1, 3.5), max_lines=10, halign="center", valign="top", text_size=(200, 500)))

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
