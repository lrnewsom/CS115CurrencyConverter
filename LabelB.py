"""
This class was not made by anyone of us at all. This is entirely from:
http://robertour.com/2015/07/15/kivy-label-or-widget-with-background-color-property/

We used this to implement a background color for our GUI because default Kivy has this property missing for the majority
of their widgets.
"""

from kivy.uix.label import Label
from kivy.properties import ListProperty

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<LabelB>:
  bcolor: 1, 1, 1, 1
  canvas.before:
    Color:
      rgba: self.bcolor
    Rectangle:
      pos: self.pos
      size: self.size
""")


class LabelB(Label):
    bcolor = ListProperty([1, 1, 1, 1])


Factory.register('KivyB', module='LabelB')
