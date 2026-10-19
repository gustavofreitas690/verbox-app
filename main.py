from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Main(App):
    def build(self):
        self.n = 0
        box = BoxLayout(orientation="vertical", padding=20, spacing=10)
        self.lb = Label(text="ver_box - 0", font_size=32)
        box.add_widget(self.lb)
        box.add_widget(Button(text="+1", size_hint=(1, .3), on_press=self.mais))
        return box

    def mais(self, *a):
        self.n += 1
        self.lb.text = "ver_box - " + str(self.n)

Main().run()
