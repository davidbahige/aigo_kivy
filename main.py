from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyBox(Widget):
    myInput = ObjectProperty(None)
    myLabel = ObjectProperty(None)

    def printOut(self):
        self.myLabel.text = self.myInput.text

class MyApp(App):
    def build(self):
        return MyBox()

MyApp().run()