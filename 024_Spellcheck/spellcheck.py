from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.spelling import Spelling # run pip3 install PyEnchant && brew install enchant

#Design Our .kv design file
Builder.load_file('design_spellcheck.kv')

class MyLayout(Widget):
    def press(self):
        #create instance of spelling
        s = Spelling() # spelling i

        #select the language
        s.select_language('en_US')

        #see language options
        #print(s.list_langauage())

        # Grab word from Input Tex
        word = self.ids.word_input.text

        options = s.suggest(word) # will suggest the correct spelling
        x = ''

        for item in options:
            x = '{x} {item}'.format(x=x,item=item)

        #update our label
        self.ids.word_label.text = '{suggestion}'.format(suggestion=x)




class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()
