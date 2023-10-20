from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import faz2

class MyGridLayout(GridLayout):
    def press(self, instance):
        name = self.name.text
        
        str2 = faz2.runi(name)
        self.add_widget(Label(text=str2, font_size=10))

    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2

        self.name = TextInput(multiline=True, text="Name=")
        self.add_widget(self.name)

        self.submit = Button(text="Submit", font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

class BasicApp(App):
    def build(self):
        return MyGridLayout()

app = BasicApp()
app.run()