from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import ButtonBehavior
from kivymd.utils.fitimage import FitImage
Window.size = 360, 640


class RoundIcon(ButtonBehavior, FitImage):
    pass


class UI(FloatLayout):
    def switch_actv(self):
        self.ids.stry.text_color = 0, 0, 0, .5
        self.ids.actv.text_color = 0, 0, 0, 1
        self.ids.crsl.load_previous()

    def switch_stry(self):
        self.ids.actv.text_color = 0, 0, 0, .5
        self.ids.stry.text_color = 0, 0, 0, 1
        self.ids.crsl.load_next(mode="next")


class Main(MDApp):
    def build(self):
        Builder.load_file("layout/chats.kv")
        return UI()

Main().run()