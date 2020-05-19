from manimlib.imports import *

class HelloWorld(Scene):
    def construct(self):
        title = TextMobject("Hello World, I am manim!")
        title.fade()
        self.play(ShowCreation(title))