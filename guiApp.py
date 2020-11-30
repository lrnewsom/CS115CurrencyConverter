
from kivy.uix.dropdown import DropDown
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
# imports Text Input
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout


Config.set('graphics', 'resizable', True)


class Pos_Size_App(App):
    def hide_widget(self, wid, dohide=True):
        if hasattr(wid, 'saved_attrs'):
            if not dohide:
                wid.height, wid.size_hint_y, wid.opacity, wid.disabled = wid.saved_attrs
                del wid.saved_attrs
        elif dohide:
            wid.saved_attrs = wid.height, wid.size_hint_y, wid.opacity, wid.disabled
            wid.height, wid.size_hint_y, wid.opacity, wid.disabled = 0, None, 0, True

    def on_enter(self, instance, value):
        print('The widget', instance, 'have', value)
        # creating button
        # size of button is 20 % by height and width of layout
        # position is 200, 200 from bottom left



    def build(self):
        rl = RelativeLayout(size=(300, 300))
        currencies = ["Dollar", "Euro", "Robux", "Dong"]

        results = Label(text="Fuck", pos=(352, 135), size_hint=(.2, .1))

        #self.hide_widget(results)
        b5 = Button(text="Convert", pos=(352, 235), size_hint=(.2, .1))




        b2 = DropDown()
        for i in currencies:
            btn = Button(text=i, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: b2.select(btn.text))
            b2.add_widget(btn)
            # create a big main button
        mainbutton = Button(text='Currency 1', size_hint=(.2, .2), pos_hint={'center_x': .27, 'center_y': .6})
        mainbutton.bind(on_release=b2.open)
        b2.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        b3 = DropDown()
        for z in currencies:
            btn1 = Button(text=z, size_hint_y=None, height=44)
            btn1.bind(on_release=lambda btn1: b3.select(btn1.text))
            b3.add_widget(btn1)
            # create a big main button
        mainbutton2 = Button(text='Currency 2', size_hint=(.2, .2), pos_hint={'center_x': .81, 'center_y': .6})
        mainbutton2.bind(on_release=b3.open)
        b3.bind(on_select=lambda instance, x: setattr(mainbutton2, 'text', x))
        b4 = TextInput(size_hint=(.2, .1),
                       pos=(352, 335),
                       text="Enter Value", multiline=False)

        def callback(instance):
            value = float(b4.text) * 2.5
            results.text = str(value)

        b5.bind(on_press=callback)
        rl.add_widget(mainbutton)
        rl.add_widget(mainbutton2)
        rl.add_widget(b4)
        rl.add_widget(results)
        rl.add_widget(b5)

        return rl


if __name__ == "__main__":
    Pos_Size_App().run()
