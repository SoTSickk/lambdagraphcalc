from manim import *

f_x = list(open("rendering_queue.txt"))[0][2:]
f = eval(f"lambda x: {f_x}")


class rendering(Scene):
    def construct(self):
        axes = Axes(x_range = (-15, 15), y_range = (-15, 15), tips = False)
        graph = FunctionGraph(eval(f"lambda x: {f_x}"))
        self.play(Write(axes))
        self.play(Write(graph))

