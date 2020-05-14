import jupyter_manim
from manimlib.imports import *
from math import cos, sin, pi
import statistics
from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Circle
from manimlib.animation.creation import ShowCreation
from manimlib.imports import *


# SQUARE WAVE
class SquareWave(GraphScene):
    CONFIG = {
    "x_min" : -3,
    "x_max" : 3,
    "y_min" : -1.5,
    "y_max" : 1.5,
    "graph_origin" : ORIGIN ,
    "function_color" : RED ,

    }
    def construct(self):
        self.setup_axes(animate=False)
        graph1=self.get_graph(self.func_to_graph1, color=RED)
        graph2=self.get_graph(self.func_to_graph2, color=WHITE)
        graph3=self.get_graph(self.func_to_graph3, color=BLUE)
        graph4=self.get_graph(self.func_to_graph4, color=PINK)
        graph5=self.get_graph(self.func_to_graph5, color=PURPLE)
        
        label1 = self.get_graph_label(graph1, label = "\\sin(\\pi x)", direction= 2*DOWN)
        label2 = self.get_graph_label(graph2, label = "\\frac{1}{3}\\sin(3 \\pi x)",direction= 2*DOWN)
        label3 = self.get_graph_label(graph3, label = "\\frac{1}{5}\\sin(5 \\pi x)",direction= 2*DOWN)
        label4 = self.get_graph_label(graph4,label = "\\frac{1}{7}\\sin(7 \\pi x)",direction= 2*DOWN)

        self.play(ShowCreation(graph1), ShowCreation(label1))
        self.play(ShowCreation(graph2), ShowCreation(label2), FadeOut(label1))
        self.play(ShowCreation(graph3), ShowCreation(label3), FadeOut(label2))
        self.play(ShowCreation(graph4), ShowCreation(label4), FadeOut(label3))
        self.play(Transform(graph1, graph5),FadeOut(label4), FadeOut(graph2),FadeOut(graph3),FadeOut(graph4))


    def func_to_graph1(self,x):
        return np.sin(pi*x)

    def func_to_graph2(self,x):
        return 1/3*np.sin(3*pi*x)
    
    def func_to_graph3(self,x):
        return 1/5*np.sin(5*pi*x)
    
    def func_to_graph4(self,x):
        return 1/7*np.sin(7*pi*x)
    
    def func_to_graph5(self,x):
        return np.sin(pi*x)+1/3*np.sin(3*pi*x)+1/5*np.sin(5*pi*x)+1/7*np.sin(7*pi*x)