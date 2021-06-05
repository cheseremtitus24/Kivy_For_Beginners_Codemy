import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.properties import StringProperty

Builder.load_file('design_yes_no.kv')

class ConfirmPopup(GridLayout):
	text = StringProperty()
	
	def __init__(self,**kwargs):
		self.register_event_type('on_answer')
		super(ConfirmPopup,self).__init__(**kwargs)
		
	def on_answer(self, *args):
		pass	
	

class PopupTest(App):
	def build(self):
		content = ConfirmPopup(text='Do You Love Kivy?')
		content.bind(on_answer=self._on_answer)
		self.popup = Popup(title="Answer Question",
							content=content,
							size_hint=(None, None),
							size=(480,400),
							auto_dismiss= False)
		self.popup.open()
		
	def _on_answer(self, instance, answer):
		print ("USER ANSWER: ") , repr(answer)
		self.popup.dismiss()
		
if __name__ == '__main__':
	PopupTest().run()
