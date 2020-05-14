import jupyter_manim
from manimlib.imports import *
from math import cos, sin, pi
import statistics
from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Circle
from manimlib.animation.creation import ShowCreation
from manimlib.imports import *


#three sine waves
class PlotFunctions(GraphScene):
    CONFIG = {
    "x_min" : -5,
    "x_max" : 5,
    "y_min" : -1.5,
    "y_max" : 1.5,
    "graph_origin" : ORIGIN ,
    "function_color" : RED ,

    }
    def construct(self):
        self.setup_axes(animate=False)
        func_graph1=self.get_graph(self.func_to_graph1, color=RED)
        func_graph2=self.get_graph(self.func_to_graph2, color=WHITE)
        func_graph3=self.get_graph(self.func_to_graph3, color= BLUE)
        func_graph4=self.get_graph(self.func_to_graph4, color=PINK)
        
        label1 = self.get_graph_label(func_graph1, label = "\\sin(x)")
        label2 = self.get_graph_label(func_graph2, label = "\\sin(2x)")
        label3 = self.get_graph_label(func_graph3, label = "\\sin(.5x+2)", direction=UP)
        label4 = self.get_graph_label(func_graph4,label = "\\sin(x)+\\sin(2x) + sin(.5x+2)", x_val = -2,direction=15*DOWN)


        self.play(ShowCreation(func_graph1),ShowCreation(func_graph2), ShowCreation(func_graph3))
        self.play(ShowCreation(label1), ShowCreation(label2), ShowCreation(label3))
        
        self.play(Transform(func_graph1, func_graph4), FadeOut(func_graph2),FadeOut(label1),FadeOut(label2), FadeOut(func_graph3), FadeOut(label3))
#         self.play(ShowCreation(label4))

    def func_to_graph1(self,x):
        return np.sin(x)

    def func_to_graph2(self,x):
        return np.sin(2*x)
    
    def func_to_graph3(self,x):
        return np.sin(.5*x+2)
    def func_to_graph4(self,x):
        return np.sin(x)+np.sin(2*x)+ np.sin(.5*x+2)