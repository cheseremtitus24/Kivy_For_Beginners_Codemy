from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory

Builder.load_string('''
<MyPopup@Popup>:
    size_hint: .5, .5
    BoxLayout:
        Label:
            text: '<default>'
            id: lbl
        Button:
            text: '<default>'
            id: btn
            on_press: root.dismiss()
''')

KV = '''
BoxLayout:
    Button:
        on_press: app.open_popup(btn='A', lbl='B')
    Button:
        on_press: app.open_popup(lbl='Hello')
    Button:
        on_press: app.open_popup(btn='World')
'''

class TestApp(App):
    def build(self):
        # Create an instance of the Popup once
        self._popup = Factory.MyPopup()
        return Builder.load_string(KV)
        
    def open_popup(self, **kwargs):
        for id, val in kwargs.items():
            print(id)
            print(val)
            self._popup.ids[id].text = val
        self._popup.open()
        
TestApp().run()
