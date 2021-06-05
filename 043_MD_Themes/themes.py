from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivymd.app import MDApp

#Design Our .kv design file
design= Builder.load_file('design_md_theme.kv')

class MyLayout(Widget):
    pass

    '''
    Red,Pink, Purple, DeepPurple
    Indigo, Blue, LightBlue, Cyan
    Teal, Green, LightGreen, Lime
    Yellow, Amber, Orange, DeepOrange
    Brown, Gray, BlueGray
    Dark
    '''
class MdthemesApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Green"
        return MyLayout()


if __name__ == '__main__':
    MdthemesApp().run()
