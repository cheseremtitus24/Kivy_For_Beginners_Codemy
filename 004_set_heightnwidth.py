import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns
        self.cols = 1
        #Setting global explicit values for the height and width of the parent grid layout

        #Note that the Default values are overriden by inline specifiers for width and height

        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        #create another secondary grid layout

        #Global Explicit set of the column height and width
        self.top_grid = GridLayout(row_force_default = True,
                                   row_default_height = 40,
                                   col_force_default=True,
                                   col_default_width=100)
        self.top_grid.cols = 2


        # Add widgets # Below we have defined and added it in one line
        self.top_grid.add_widget(Label(text="Name: "))

        # Add INput Box
        # below we are defining the properties of var name self.name which is a text input

        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        # Add Input Box
        self.top_grid.add_widget(Label(text="Favorite Pizza: "))
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        #Add label
        self.top_grid.add_widget(Label(text="Favorite Color"))
        self.color = TextInput(multiline=True)
        self.top_grid.add_widget(self.color)

        #add the top_grid layout into the master grid_layout
        self.add_widget(self.top_grid)

        #adding a button
        #Inline setting of height and width
        self.button = Button(text="Submit",
                             font_size=32,
                             size_hint_y=None,
                             height = 30,
                             size_hint_x=None,
                             width= 600 )
        self.button.bind(on_press=self.press_func)
        #adding the button to the kivy window
        self.add_widget(self.button)
    def press_func(self,instance): # same as in tkinter when you pass in event
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        #displaying the contents on Screen

        # Adding a label widget and ensuring that the input fields are not empty
        if not (name == "") and not(pizza == "") and not(color == ""):
            self.add_widget(Label(text="My name is {name} and i like {pizza} with a favorite color of {color}".format(name=name, pizza=pizza,color=color)))

        #Since there will be residual values in the name, pizza and color variables we need to reset
        # the values to empty strings
        #clearing the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()

