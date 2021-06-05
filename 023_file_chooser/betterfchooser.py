# You will need the following line in order to fix dependency requirements
#python3 -m pip install git+http://github.com/kivy/pyobjus/
# on ios you will need to install the plyer module with the following command
#  python3 -m pip install plyer
# after that is done you will need pyobjus which is used as an api middleware for calling native functionalities on the ios platform

# run line 2 and once you are done we can check out the following code....
# Be free to pause the video while you get your environment set up.

#.... 

# Lets Begin ....

'''
Example of an Android filechooser. 
This also works on other platforms such as ios and windows but remember you require the pyobjus module for it to work on ios 
'''

from textwrap import dedent

from plyer import filechooser

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.button import Button


class FileChoose(Button):
    # This is the entry point of the program called as alias: entry event 
    '''
    Button that triggers 'filechooser.open_file()' and processes
    the data response from filechooser Activity.
    '''

    selection = ListProperty([])

    def choose(self):
        # As you can see the plyer module is called within this choose method
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):
        '''
        Callback function for handling the selection response from Activity.
        '''
        self.selection = selection
        # From here
        # The self.selection on line 60 is referenced from here

    def on_selection(self, *a, **k):
        '''
        Update TextInput.text after FileChoose.selection is changed
        via FileChoose.handle_selection.
        '''
        App.get_running_app().root.ids.result.text = str(self.selection)
        # On successful selection we will need to set the image through its defined id

        # Take note of the following line.
        App.get_running_app().root.ids.image.source = str(self.selection[0])

        
        #from line 62 we see that the str(self.selection[0]) is used to feed the image path to the source: attribute of the Image: widget..

        # Thanks For Watching Subscribe and hit the like button..
        # 

class ChooserApp(App):
    '''
    Application class with root built in KV.
    '''

    def build(self):
        return Builder.load_string(dedent('''
            <FileChoose>:
            BoxLayout:
                BoxLayout:
                    orientation: 'vertical'
                    TextInput:
                        id: result
                        text: ''
                        hint_text: 'selected path'
                    Image:
                        id: image # Take note of the id that is reference here
                        # you will need to upload the name to be set to a db
                        source: ''
                        
                    FileChoose:
                        size_hint_y: 0.1
                        on_release: self.choose()
                        text: 'Select a file'
        '''))


if __name__ == '__main__':
    # Lets run 
    ChooserApp().run()
