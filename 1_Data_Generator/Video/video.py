from manim import *
import itertools as it

"""
class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"This is some \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid", font_size=72)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid

        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()
"""

import itertools as it

class myNN(Scene):
    def construct(self):
        """
        title_1 = Tex(r"Hey, I'm Reed Graff")
        binaries_1 = VGroup(Tex("01010010"), Tex("01100101"), Tex("01100101"), Tex("01100100")).arrange(RIGHT)
        VGroup(title_1, binaries_1).arrange(DOWN)
        self.play(
            Write(title_1),
            FadeIn(binaries_1, shift=DOWN),
        )
        self.wait()

        title_2 = Tex(r"Hey, I'm Reed Graff")
        binaries_2 = VGroup(Tex("01010010"), Tex("01100101"), Tex("01100101"), Tex("01100100")).arrange(DOWN)
        VGroup(title_2, binaries_2).arrange(DOWN)
        self.play(
            ReplacementTransform(title_1, title_2, run_time=2),
            ReplacementTransform(binaries_1, binaries_2, run_time=2),
        )
        self.wait()

        binaries_3 = binaries_2.copy()
        binaries_3[0] = Tex(binaries_3[0].tex_string, " = R").match_y(binaries_3[0])
        binaries_3[1] = Tex(binaries_3[1].tex_string, " = e").match_y(binaries_3[1])
        binaries_3[2] = Tex(binaries_3[2].tex_string, " = e").match_y(binaries_3[2])
        binaries_3[3] = Tex(binaries_3[3].tex_string, " = d").match_y(binaries_3[3])

        self.play(
            ReplacementTransform(binaries_2, binaries_3, run_time=2),
        )
        self.wait()
        """
        title_1 = Tex(r"So")
        title_2 = Tex(r"what")
        title_3 = Tex(r"are")
        title_4 = Tex(r"Similarity Learning")
        title_5 = Tex(r"and")
        title_6 = Tex(r"Data Generators?")
        section_title = VGroup(title_1, title_2, title_3, title_4, title_5, title_6).arrange(RIGHT)
        self.play(
            LaggedStart(
                *[
                    Write(title_1, run_time=2),
                    Write(title_2, run_time=0.5),
                    Write(title_3, run_time=0.5),
                    Write(title_4, run_time=2),
                    Write(title_5, run_time=1),
                    Write(title_6, run_time=2)
                ], 
                lag_ratio=0.5
            ),
        )
        self.wait()



        Background = Tex("1. Background")
        Introduction = Tex("2. Introduction")
        Permutation = Tex("3. Permutation Approach")
        Combination = Tex("4. Combination Approach")
        Tensorflow = Tex("5. Tensorflow Integration")
        index = VGroup(Background, Introduction, Permutation, Combination, Tensorflow).arrange(DOWN, center=False, aligned_edge=LEFT)
        section_title_2 = section_title.copy()
        title_group = VGroup(section_title_2, index).arrange(DOWN).move_to(ORIGIN)
        self.play(
            ReplacementTransform(section_title, title_group, run_time=2),
        )
        self.wait()



        Background_2 = Tex("Background")
        Background_2.to_corner(UL, buff=0.15)
        self.play(
            ReplacementTransform(title_group, Background_2, run_time=2),
        )
        self.wait()



        # defines the axes and linear function
        axes = Axes(x_range=[-1, 10], y_range=[-1, 10], x_length=9, y_length=6)
        func = axes.plot(lambda x: x, color=BLUE)
        # creates the T_label
        t_label = axes.get_T_label(x_val=4, graph=func, label=Tex("x-value"))
        self.play(
            Write(axes, run_time=1),
            Write(func, run_time=2),
            Write(t_label, run_time=1),
        )
        self.wait()

        point = axes.coords_to_point(2, 3)
        dot = Dot(point)
        line = axes.get_vertical_line(point, line_config={"dashed_ratio": 0.85})
        self.play(
            Write(dot, run_time=1),
            Write(line, run_time=1),
        )
        self.wait()


        """
        section_title_2 = section_title.copy()
        section_title_2.to_corner(UL, buff=0.25)
        self.play(
            Transform(section_title, section_title_2, run_time=2),
        )
        self.wait()
        """





        
        """
        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()
        
        NN = NeuralNetworkMobject([1000, 5, 1])
        NN.label_inputs("x")
        NN.label_outputs("\hat{y}")
        NN.label_outputs_text("Output")

        NN.scale(0.75)
        self.play(Write(NN))
        self.wait()
        """

# A customizable Sequential Neural Network
class NeuralNetworkMobject(VGroup):
    CONFIG = {
        "neuron_radius": 0.15,
        "neuron_to_neuron_buff": MED_SMALL_BUFF,
        "layer_to_layer_buff": LARGE_BUFF,
        "output_neuron_color": WHITE,
        "input_neuron_color": WHITE,
        "hidden_layer_neuron_color": WHITE,
        "neuron_stroke_width": 2,
        "neuron_fill_color": GREEN,
        "edge_color": LIGHT_GREY,
        "edge_stroke_width": 2,
        "edge_propogation_color": YELLOW,
        "edge_propogation_time": 1,
        "max_shown_neurons": 16,
        "brace_for_large_layers": True,
        "average_shown_activation_of_large_layer": True,
        "include_output_labels": False,
        "arrow": False,
        "arrow_tip_size": 0.1,
        "left_size": 1,
        "neuron_fill_opacity": 1
    }
    # Constructor with parameters of the neurons in a list
    def __init__(self, neural_network, *args, **kwargs):
        VGroup.__init__(self, *args, **kwargs)
        
        for key in self.CONFIG.keys():
            setattr(self, key, self.CONFIG[key])

        self.layer_sizes = neural_network
        self.add_neurons()
        self.add_edges()
        self.add_to_back(self.layers)
    # Helper method for constructor
    def add_neurons(self):
        layers = VGroup(*[
            self.get_layer(size, index)
            for index, size in enumerate(self.layer_sizes)
        ])
        layers.arrange_submobjects(RIGHT, buff=self.layer_to_layer_buff)
        self.layers = layers
        if self.include_output_labels:
            self.label_outputs_text()
    # Helper method for constructor
    def get_nn_fill_color(self, index):
        if index == -1 or index == len(self.layer_sizes) - 1:
            return self.output_neuron_color
        if index == 0:
            return self.input_neuron_color
        else:
            return self.hidden_layer_neuron_color
    # Helper method for constructor
    def get_layer(self, size, index=-1):
        layer = VGroup()
        n_neurons = size
        if n_neurons > self.max_shown_neurons:
            n_neurons = self.max_shown_neurons
        neurons = VGroup(*[
            Circle(
                radius=self.neuron_radius,
                stroke_color=self.get_nn_fill_color(index),
                stroke_width=self.neuron_stroke_width,
                fill_color=BLACK,
                fill_opacity=self.neuron_fill_opacity,
            )
            for x in range(n_neurons)
        ])
        neurons.arrange_submobjects(
            DOWN, buff=self.neuron_to_neuron_buff
        )
        for neuron in neurons:
            neuron.edges_in = VGroup()
            neuron.edges_out = VGroup()
        layer.neurons = neurons
        layer.add(neurons)

        if size > n_neurons:
            dots = MathTex("\\vdots")
            dots.move_to(neurons)
            VGroup(*neurons[:len(neurons) // 2]).next_to(
                dots, UP, MED_SMALL_BUFF
            )
            VGroup(*neurons[len(neurons) // 2:]).next_to(
                dots, DOWN, MED_SMALL_BUFF
            )
            layer.dots = dots
            layer.add(dots)
            if self.brace_for_large_layers:
                brace = Brace(layer, LEFT)
                brace_label = brace.get_tex(str(size))
                layer.brace = brace
                layer.brace_label = brace_label
                layer.add(brace, brace_label)

        return layer
    # Helper method for constructor
    def add_edges(self):
        self.edge_groups = VGroup()
        for l1, l2 in zip(self.layers[:-1], self.layers[1:]):
            edge_group = VGroup()
            for n1, n2 in it.product(l1.neurons, l2.neurons):
                edge = self.get_edge(n1, n2)
                edge_group.add(edge)
                n1.edges_out.add(edge)
                n2.edges_in.add(edge)
            self.edge_groups.add(edge_group)
        self.add_to_back(self.edge_groups)
    # Helper method for constructor
    def get_edge(self, neuron1, neuron2):
        if self.arrow:
            return Arrow(
                neuron1.get_center(),
                neuron2.get_center(),
                buff=self.neuron_radius,
                stroke_color=self.edge_color,
                stroke_width=self.edge_stroke_width,
                tip_length=self.arrow_tip_size
            )
        return Line(
            neuron1.get_center(),
            neuron2.get_center(),
            buff=self.neuron_radius,
            stroke_color=self.edge_color,
            stroke_width=self.edge_stroke_width,
        )
    
    # Labels each input neuron with a char l or a LaTeX character
    def label_inputs(self, l):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[0].neurons):
            label = MathTex(f"{l}_"+"{"+f"{n + 1}"+"}")
            label.set_height(0.3 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    # Labels each output neuron with a char l or a LaTeX character
    def label_outputs(self, l):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[-1].neurons):
            label = MathTex(f"{l}_"+"{"+f"{n + 1}"+"}")
            label.set_height(0.4 * neuron.get_height())
            label.move_to(neuron)
            self.output_labels.add(label)
        self.add(self.output_labels)

    # Labels each neuron in the output layer with text according to an output list
    def label_outputs_text(self, outputs):
        self.output_labels = VGroup()
        for n, neuron in enumerate(self.layers[-1].neurons):
            label = Tex(outputs[n])
            label.set_height(0.75*neuron.get_height())
            label.move_to(neuron)
            label.shift((neuron.get_width() + label.get_width()/2)*RIGHT)
            self.output_labels.add(label)
        self.add(self.output_labels)

    # Labels the hidden layers with a char l or a LaTeX character
    def label_hidden_layers(self, l):
        self.output_labels = VGroup()
        for layer in self.layers[1:-1]:
            for n, neuron in enumerate(layer.neurons):
                label = MathTex(f"{l}_{n + 1}")
                label.set_height(0.4 * neuron.get_height())
                label.move_to(neuron)
                self.output_labels.add(label)
        self.add(self.output_labels)