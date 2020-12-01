import sqlite3 as lite

from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

from LabelB import LabelB
from Currency import Currency

Window.size = (1000, 700)


class UserGroup(Screen):
    drop_down = ObjectProperty(None)


class CustomDropDown(DropDown):
    pass


class CustomTextInput(TextInput):
    pass


class GUI(App):
    def build(self):
        main_window = GridLayout()
        main_window.cols = 1
        main_window.rows = 3

        name = LabelB(text='Team De Soto Currency Converter', bcolor=[0.2, 0.3, 0.1, 1], font_size=60, italic=True)
        main_window.add_widget(name)

        second_window = GridLayout()
        second_window.cols = 3
        second_window.rows = 1
        dropdown = CustomDropDown()
        mainbutton = Button(text='Starting Currency', font_size=30)
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        second_window.add_widget(mainbutton)

        # value = LabelB(text='Enter value here: ', bcolor=[0.2, 0.3, 0.1, 1])
        inside_window = GridLayout()
        inside_window.cols = 1
        inside_window.rows = 3
        inside_blank1 = LabelB(text='', bcolor=[0.2, 0.3, 0.1, 1])
        inside_blank2 = LabelB(text='', bcolor=[0.2, 0.3, 0.1, 1])
        value = CustomTextInput()
        inside_window.add_widget(inside_blank1)
        inside_window.add_widget(value)
        inside_window.add_widget(inside_blank2)
        second_window.add_widget(inside_window)

        dropdown2 = CustomDropDown()
        twobutton = Button(text='Convert to:', font_size=30)
        twobutton.bind(on_release=dropdown2.open)
        dropdown2.bind(on_select=lambda instance, x: setattr(twobutton, 'text', x))
        second_window.add_widget(twobutton)

        main_window.add_widget(second_window)

        third_window = GridLayout()
        third_window.cols = 2
        third_window.rows = 3
        blank1 = LabelB(text='', bcolor=[0.2, 0.3, 0.1, 1])
        blank2 = LabelB(text='', bcolor=[0.2, 0.3, 0.1, 1])
        calc_button = Button(text='Press here to convert')

        # insert when pressed code here
        def callback(instance):
            amount = float(value.text)
            original = mainbutton.text
            convert_to = twobutton.text
            money = Currency(original, convert_to, amount)
            number = money.convert()
            # number = float(value.text) * 2.5
            results.text = "{:,.2f} {}s".format(number, convert_to)

        calc_button.bind(on_press=callback)
        results = LabelB(text='Results will show up here', bcolor=[0.2, 0.3, 0.1, 1], font_size=30)
        blank3 = LabelB(text='', bcolor=[0.2, 0.3, 0.1, 1])
        blank4 = LabelB(text='', bcolor=[0.2, 0.3, 0.1, 1])

        third_window.add_widget(blank1)
        third_window.add_widget(blank2)
        third_window.add_widget(calc_button)
        third_window.add_widget(results)
        third_window.add_widget(blank3)
        third_window.add_widget(blank4)
        main_window.add_widget(third_window)
        return main_window


# if __name__ == '__main__':
   # GUI().run()
