from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.app import MDApp

#Design Our .kv design file
design= Builder.load_file('design_md_Login.kv')

class MyLayout(Widget):
    def logger(self):
        self.ids.welcome_label.text = 'sup'
    def clear(self):
        self.ids.welcome_label.text = "WELCOME"

    '''
    Red,Pink, Purple, DeepPurple
    Indigo, Blue, LightBlue, Cyan
    Teal, Green, LightGreen, Lime
    Yellow, Amber, Orange, DeepOrange
    Brown, Gray, BlueGray
    Dark
    '''
class MdLoginApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Green"
        return MyLayout()


if __name__ == '__main__':
    MdLoginApp().run()
