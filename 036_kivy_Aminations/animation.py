from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.animation import Animation

#Design Our .kv design file
Builder.load_file('design_animation.kv')

class MyLayout(Widget):
    def animate_it(self, widget, *args):
        #define animation you want to do
        animate = Animation(
                background_color = (0,0,1,1),
                duration=2) # 2 seconds
        #changing size
        animate += Animation(
                size_hint = (1,1))
        animate += Animation(
                size_hint = (.5,.5))
        animate += Animation(
                pos_hint = {'center_x': .1})
        animate += Animation(
                pos_hint = {'center_x': .5})
        # Do second animation
        animate += Animation(opacity=1,
                duration=3)

        #

        
        #start the Animation
        animate.start(widget)

        # Create a callback
        animate.bind(on_complete = self.my_callback)

    def my_callback(self, *args):
        self.ids.my_label.text = "callback executed"

class AnimateApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AnimateApp().run()
