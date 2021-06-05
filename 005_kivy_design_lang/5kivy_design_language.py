from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press_func(self):  # same as in tkinter when you pass in event
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        # displaying the contents on Screen

        # Adding a label widget and ensuring that the input fields are not empty
        # if not (name == "") and not (pizza == "") and not (color == ""):
        #     self.add_widget(Label(
        #         text="My name is {name} and i like {pizza} with a favorite color of {color}".format(name=name, pizza=pizza,color=color)))

        print("My name is {name} and i like {pizza} with a favorite color of {color}".format(name=name, pizza=pizza,color=color))
        # Since there will be residual values in the name, pizza and color variables we need to reset
        # the values to empty strings
        # clearing the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""
#You should call you kivy design file as my.kv the A/app throws an error
class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()


