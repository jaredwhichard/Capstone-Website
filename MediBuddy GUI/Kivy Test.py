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

        # Set columns
        self.cols = 2

        # Create Temperature Button
        self.submit = Button(text="Temperature", font_size=32)
        self.add_widget(self.submit)

        # Create Temperature Button
        self.submit = Button(text="Pulse", font_size=32)
        self.add_widget(self.submit)

        # Create Temperature Button
        self.submit = Button(text="SP02", font_size=32)
        self.add_widget(self.submit)


class MediBuddy(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MediBuddy().run()


