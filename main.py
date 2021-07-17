from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import sarcasmyfier

class MainApp(App):
    def build(self):
        self.mainLayout = BoxLayout(padding=7, spacing=40, orientation="vertical")
        
        self.inputField = TextInput(multiline=True)
        self.mainLayout.add_widget(self.inputField)


        activate = Button(text="Convert", size_hint=(.5, .5), align="center")
        activate.bind(on_press=self.on_press_button)
        self.mainLayout.add_widget(activate)

        self.outputText = TextInput(text="", readonly=True)
        self.mainLayout.add_widget(self.outputText)

        return self.mainLayout

    def on_press_button(self, instance):
        self.outputText.text = sarcasmyfier.sarcasmify(str(self.inputField.text))


# TODO: implement the convertion by adding the sarcasmyfier script

if __name__ == "__main__":
    app = MainApp()
    app.run()