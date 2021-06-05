from kivy.app import App
from kivy.uix.widget import Widget
from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_file('design_pop.kv')
class MyLayout(Widget):
    
    #create an instance of the Popup once
    login_popup = Factory.MyPopup()
    
    def modify(self, value):
        self.login_popup.ids['lbl'].text = 'val'

    def open_popup(self, **kwargs):
        #for id, val in kwargs.items():
         #   self.login_popup.ids['lbl'].text = val
        #self.login_popup.ids['lbl'].text = 'val'
        self.login_popup.open()


class TestApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    TestApp().run()



    
