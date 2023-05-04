from manim import *
import itertools as it
import pandas as pd

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



        #Data Frame
        #df = pd.read_csv('C:/Users/range/CodingProjects/Python Projects/Data science/ML/Siamese_Studies/Data/Instagram_Spam/whole.csv', sep=',', header=None)
        #followers = [int(x) for x in df[9].tolist()[1:11]]
        #following = [int(x) for x in df[10].tolist()[1:11]]
        followers = [1000, 2740, 159, 414, 151, 669987, 122, 1078, 1824, 12945, 9884, 1188, 945, 12033, 1962, 50374, 7007, 1128, 34670, 2338, 3516, 1809, 427, 759, 15338538, 109, 536, 121354, 2284, 186, 687, 966, 177, 744, 542073, 5315651, 267, 691, 120, 105, 890969, 361853, 3678, 92192, 12397719, 380510, 132, 162, 369, 1476, 1798, 2118, 812, 7217, 313, 64, 1759, 404, 1843, 320377, 108, 384, 60, 802, 51145, 1582, 223, 18842, 10240, 539, 399, 581, 166, 417, 266, 33, 494, 178, 470, 807, 162, 417, 17303, 1439, 91446, 824, 741, 1267, 4594, 1135, 1926, 1068, 815, 565, 2556, 1312, 699, 4328, 2487, 673, 730, 59, 289, 19, 3551, 19512, 2756, 5406, 459, 218, 796, 1113, 138, 205, 331, 748, 490, 456, 971, 497, 99, 193, 492, 167, 99, 916, 196, 765, 45, 634, 1383, 650, 484, 200, 192, 553, 27477, 464, 1057, 413, 389, 505, 941, 2598, 59, 622, 2719, 216, 881, 870, 265, 1204, 655, 1662, 14222, 483, 1204, 408, 303, 125, 229, 357, 137, 255, 87, 326946, 114, 167, 1247, 585, 135, 722, 714, 39867, 533, 1158, 45834, 876, 3003, 1298, 3800, 1358, 6741307, 791, 732075, 373, 162, 309, 135, 244, 67, 984, 751, 781, 1761, 318, 5282, 5282, 228, 393, 875, 173, 3896490, 106, 206, 259, 1013, 738, 1008, 2441, 416, 516, 8711, 433, 18515, 70, 5863, 1677, 617, 31182, 1152, 8578, 4347, 319, 189, 743, 11204, 419, 81, 947, 206, 541, 392, 4177, 265, 272, 425, 150, 711, 89, 742, 96, 77, 195, 9, 10794, 104, 318, 355, 99, 300, 139, 13, 606, 428, 494, 1261, 68, 205558, 668, 1456, 410, 298, 254, 1070, 1167, 335, 346, 1746, 268, 537, 805, 1504, 104, 380, 257, 1775, 1456, 265, 1051, 77, 220, 178, 728, 668, 406, 37, 56, 90, 60, 271, 1, 158, 39, 0, 0, 0, 12, 10, 1, 1, 0, 31, 5, 18, 12, 6, 47, 33, 4, 5, 0, 5, 107, 8, 48, 2, 51, 5, 0, 26, 0, 76, 165, 115, 6, 24, 40, 32, 0, 21, 79, 8, 49, 31, 15, 4, 0, 316, 0, 3, 2, 221, 181, 9, 2, 25, 26, 15, 59, 7, 40, 51, 133, 25, 864, 73, 184, 161, 42, 279, 219, 18, 106, 34, 42, 1, 38, 34, 23, 23, 83, 25, 13, 64, 90, 82, 140, 0, 51, 38, 21, 5, 21, 124, 5, 2, 42, 48, 32, 0, 0, 10, 19, 138, 11, 1, 39, 446, 9, 589, 27, 143, 0, 0, 124, 12, 16, 1, 120, 0, 26, 57, 13, 1031, 42, 70, 0, 46, 834, 389, 43, 23, 5, 4, 17, 182, 108, 43, 77, 32, 0, 40, 53, 67, 122, 18, 24, 35, 119, 6, 34, 272, 53, 818, 82, 40, 21, 59, 102, 576, 19, 66, 310, 16, 15, 47, 88, 51, 505, 159, 77, 61, 7, 11, 49, 15, 1, 17, 15, 358, 20, 50, 57, 12, 218, 78, 16, 39, 15, 30, 85, 77, 49, 16, 8, 34, 45, 49, 15, 92, 75, 10, 23, 22, 55, 16, 7, 86, 3, 12, 14, 24, 52, 16, 17, 50, 136, 178, 50, 207, 178, 16, 49, 49, 37, 21, 356, 46, 49, 49, 44, 42, 47, 48, 75, 115, 53, 32, 39, 3033, 3003, 34, 218, 210, 1489, 10, 201, 351, 52, 156, 85, 35, 55, 16, 43, 97, 34, 2346, 49, 2, 40, 332, 14, 65, 20, 26, 72, 55, 77, 31, 57, 58, 47, 31, 96, 126, 39, 66, 87, 15, 166, 66, 96, 57, 150, 488, 35, 328, 14890, 225, 362, 213, 552, 122, 834, 229, 1913, 200, 130, 192, 498, 96, 202, 175, 223, 189, 486, 464, 150, 2983, 116, 155537, 248, 348, 4021842, 366, 1064, 81267, 400, 361, 228, 855, 777, 264, 1572, 510, 1027419, 710, 2267, 2055, 814, 668, 87, 461, 602517, 62, 341, 717, 386, 673, 654, 751, 209, 573, 284, 0, 45, 19, 69, 22, 31, 9, 69, 23, 17, 46, 16, 0, 21, 52, 24, 13, 227, 10, 46, 57, 341, 1789, 45, 21, 309, 1742, 1906, 39, 17, 62, 119, 2997, 772, 129, 94, 37, 75, 42, 145, 128, 88, 1987, 100, 214, 227, 192, 415, 926, 238, 193, 49, 13, 74, 88, 114, 150, 833, 219, 39]
        following = [955, 533, 98, 651, 126, 150, 177, 76, 2713, 813, 1173, 365, 583, 248, 2701, 900, 289, 694, 1878, 776, 999, 416, 470, 956, 61, 179, 665, 176, 130, 174, 1517, 952, 170, 967, 674, 2703, 328, 680, 112, 98, 11, 583, 1359, 16, 8, 0, 183, 208, 546, 666, 461, 1109, 432, 761, 376, 261, 643, 283, 598, 228, 97, 447, 100, 151, 528, 1882, 266, 744, 1255, 639, 452, 568, 163, 362, 324, 37, 998, 245, 288, 675, 256, 395, 360, 629, 526, 489, 1440, 899, 1713, 899, 1410, 1925, 748, 469, 1074, 935, 599, 418, 999, 438, 413, 55, 222, 20, 173, 591, 638, 589, 390, 75, 1155, 1854, 208, 164, 333, 4659, 1093, 413, 2047, 438, 132, 413, 689, 164, 178, 1142, 209, 424, 80, 719, 7500, 703, 3296, 270, 65, 610, 7202, 1039, 524, 138, 806, 503, 1208, 802, 111, 475, 1061, 305, 375, 72, 371, 633, 1016, 1065, 7399, 1216, 2928, 635, 417, 101, 383, 489, 96, 535, 399, 3, 446, 387, 1196, 1364, 232, 261, 1159, 4664, 1060, 3932, 280, 529, 455, 407, 278, 127, 111, 456, 363, 360, 311, 364, 176, 172, 149, 76, 1223, 529, 905, 523, 652, 652, 238, 502, 754, 373, 351, 133, 32, 1371, 996, 544, 517, 396, 292, 463, 345, 584, 1000, 67, 157, 716, 272, 414, 292, 164, 748, 335, 177, 331, 124, 271, 268, 582, 333, 701, 237, 3678, 321, 1486, 917, 178, 673, 121, 653, 50, 107, 395, 13, 3164, 15, 569, 137, 488, 372, 61, 77, 430, 333, 545, 2187, 87, 53, 609, 555, 387, 555, 345, 1072, 618, 300, 426, 1631, 370, 1002, 488, 52, 119, 462, 346, 7500, 1200, 264, 694, 34, 323, 81, 1213, 294, 408, 22, 114, 333, 31, 445, 80, 309, 64, 11, 853, 23, 5, 18, 34, 8, 0, 213, 10, 58, 77, 37, 10, 4, 279, 15, 44, 17, 42, 60, 6, 215, 126, 48, 802, 46, 601, 168, 689, 230, 15, 49, 236, 52, 35, 44, 767, 37, 79, 91, 41, 3, 229, 1165, 0, 1, 30, 244, 935, 167, 0, 86, 129, 305, 48, 47, 179, 41, 750, 39, 3646, 35, 170, 333, 694, 1124, 155, 106, 171, 108, 26, 13, 68, 44, 151, 37, 139, 28, 38, 60, 69, 6, 319, 29, 420, 87, 733, 121, 45, 249, 56, 16, 46, 45, 25, 71, 0, 104, 31, 99, 157, 64, 40, 1762, 82, 2980, 63, 500, 177, 130, 135, 192, 36, 2, 181, 71, 8, 167, 22, 208, 146, 64, 8, 92, 4118, 392, 221, 40, 82, 25, 44, 227, 304, 123, 8, 87, 11, 66, 303, 90, 336, 49, 88, 136, 151, 24, 26, 295, 137, 618, 74, 233, 76, 38, 109, 474, 16, 161, 894, 17, 4, 98, 61, 59, 2330, 433, 1269, 76, 14, 60, 22, 595, 9, 1, 1, 1990, 7, 32, 76, 15, 792, 98, 23, 17, 1, 48, 638, 747, 82, 24, 6, 22, 83, 0, 5, 403, 26, 0, 26, 11, 46, 0, 20, 0, 11, 30, 56, 22, 1, 27, 20, 49, 1029, 1417, 39, 2426, 828, 26, 2, 12, 4, 0, 2176, 4, 0, 58, 45, 240, 9, 1, 26, 289, 66, 23, 153, 1155, 825, 36, 1528, 1543, 3715, 2, 812, 2663, 16, 423, 477, 38, 28, 51, 88, 408, 112, 7272, 95, 55, 19, 1333, 542, 162, 52, 27, 434, 2, 108, 215, 130, 347, 139, 37, 242, 860, 229, 161, 698, 64, 596, 75, 339, 73, 487, 604, 6, 668, 7369, 356, 424, 254, 521, 143, 358, 492, 436, 437, 622, 141, 337, 499, 605, 199, 694, 276, 862, 367, 157, 545, 138, 1395, 490, 347, 5514, 552, 573, 963, 449, 562, 346, 151, 148, 151, 3504, 185, 293, 549, 466, 993, 1111, 605, 40, 1055, 482, 47, 274, 223, 363, 568, 535, 577, 276, 474, 505, 2, 64, 30, 694, 82, 124, 25, 694, 33, 34, 38, 2, 18, 1, 15, 2, 22, 353, 24, 18, 22, 2287, 6153, 64, 31, 250, 6172, 2129, 324, 33, 126, 350, 764, 3239, 920, 105, 58, 55, 175, 202, 636, 72, 7453, 162, 829, 776, 942, 1445, 4239, 1381, 669, 235, 7, 270, 76, 811, 164, 3572, 1695, 68]
        # 0: [:637], 1: [637:]


        # defines the axes and linear function
        axes = Axes(
            x_range=[min(followers), max(followers), 5000000],
            y_range=[min(following), max(following), 1000], 
            x_length=9, 
            y_length=6,
            axis_config={
                "numbers_to_include": np.arange(0, 10000000 + 5000000, 5000000),
                "font_size": 24,
            },
            tips=False,
        ).add_coordinates()
        #axes = Axes(x_range=[0, 5], y_range=[0, 3], x_length=5, y_length=3).add_coordinates()
        func = axes.plot(lambda x: x, color=BLUE)
        # creates the T_label
        # t_label = axes.get_T_label(x_val=4, graph=func, label=Tex("x-value"))
        self.play(
            Write(axes, run_time=1),
            Write(func, run_time=2),
            #Write(t_label, run_time=1),
        )
        self.wait()



        zipped = list(zip(followers, following))
        dots = VGroup(*[Dot(axes.c2p(x, y)) for x,y in zipped])
        #lines = VGroup(*[axes.get_vertical_line(axes.coords_to_point(x, y), line_config={"dashed_ratio": 0.85}) for x,y in zipped])
        self.play(
            Write(dots),
            #lines
        )
        self.wait()


        new_axes = Axes(
            x_range=[0, 10000, 1000],
            y_range=[0, 5000, 1000], 
            x_length=9, 
            y_length=6,
            axis_config={
                "numbers_to_include": np.arange(0, 10000000 + 5000000, 5000000),
                "font_size": 24,
            },
            tips=False,
        ).add_coordinates()
        new_dots = VGroup(*[Dot(new_axes.c2p(x, y)) for x,y in zipped if x <= 10000])
        self.play(
            ReplacementTransform(axes, new_axes),
            ReplacementTransform(dots, new_dots),
        )
        self.wait()



class GetAxisLabelsExample(ThreeDScene):
    def construct(self):
        followers = [1000, 2740, 159, 414, 151, 669987, 122, 1078, 1824, 12945, 9884, 1188, 945, 12033, 1962, 50374, 7007, 1128, 34670, 2338, 3516, 1809, 427, 759, 15338538, 109, 536, 121354, 2284, 186, 687, 966, 177, 744, 542073, 5315651, 267, 691, 120, 105, 890969, 361853, 3678, 92192, 12397719, 380510, 132, 162, 369, 1476, 1798, 2118, 812, 7217, 313, 64, 1759, 404, 1843, 320377, 108, 384, 60, 802, 51145, 1582, 223, 18842, 10240, 539, 399, 581, 166, 417, 266, 33, 494, 178, 470, 807, 162, 417, 17303, 1439, 91446, 824, 741, 1267, 4594, 1135, 1926, 1068, 815, 565, 2556, 1312, 699, 4328, 2487, 673, 730, 59, 289, 19, 3551, 19512, 2756, 5406, 459, 218, 796, 1113, 138, 205, 331, 748, 490, 456, 971, 497, 99, 193, 492, 167, 99, 916, 196, 765, 45, 634, 1383, 650, 484, 200, 192, 553, 27477, 464, 1057, 413, 389, 505, 941, 2598, 59, 622, 2719, 216, 881, 870, 265, 1204, 655, 1662, 14222, 483, 1204, 408, 303, 125, 229, 357, 137, 255, 87, 326946, 114, 167, 1247, 585, 135, 722, 714, 39867, 533, 1158, 45834, 876, 3003, 1298, 3800, 1358, 6741307, 791, 732075, 373, 162, 309, 135, 244, 67, 984, 751, 781, 1761, 318, 5282, 5282, 228, 393, 875, 173, 3896490, 106, 206, 259, 1013, 738, 1008, 2441, 416, 516, 8711, 433, 18515, 70, 5863, 1677, 617, 31182, 1152, 8578, 4347, 319, 189, 743, 11204, 419, 81, 947, 206, 541, 392, 4177, 265, 272, 425, 150, 711, 89, 742, 96, 77, 195, 9, 10794, 104, 318, 355, 99, 300, 139, 13, 606, 428, 494, 1261, 68, 205558, 668, 1456, 410, 298, 254, 1070, 1167, 335, 346, 1746, 268, 537, 805, 1504, 104, 380, 257, 1775, 1456, 265, 1051, 77, 220, 178, 728, 668, 406, 37, 56, 90, 60, 271, 1, 158, 39, 0, 0, 0, 12, 10, 1, 1, 0, 31, 5, 18, 12, 6, 47, 33, 4, 5, 0, 5, 107, 8, 48, 2, 51, 5, 0, 26, 0, 76, 165, 115, 6, 24, 40, 32, 0, 21, 79, 8, 49, 31, 15, 4, 0, 316, 0, 3, 2, 221, 181, 9, 2, 25, 26, 15, 59, 7, 40, 51, 133, 25, 864, 73, 184, 161, 42, 279, 219, 18, 106, 34, 42, 1, 38, 34, 23, 23, 83, 25, 13, 64, 90, 82, 140, 0, 51, 38, 21, 5, 21, 124, 5, 2, 42, 48, 32, 0, 0, 10, 19, 138, 11, 1, 39, 446, 9, 589, 27, 143, 0, 0, 124, 12, 16, 1, 120, 0, 26, 57, 13, 1031, 42, 70, 0, 46, 834, 389, 43, 23, 5, 4, 17, 182, 108, 43, 77, 32, 0, 40, 53, 67, 122, 18, 24, 35, 119, 6, 34, 272, 53, 818, 82, 40, 21, 59, 102, 576, 19, 66, 310, 16, 15, 47, 88, 51, 505, 159, 77, 61, 7, 11, 49, 15, 1, 17, 15, 358, 20, 50, 57, 12, 218, 78, 16, 39, 15, 30, 85, 77, 49, 16, 8, 34, 45, 49, 15, 92, 75, 10, 23, 22, 55, 16, 7, 86, 3, 12, 14, 24, 52, 16, 17, 50, 136, 178, 50, 207, 178, 16, 49, 49, 37, 21, 356, 46, 49, 49, 44, 42, 47, 48, 75, 115, 53, 32, 39, 3033, 3003, 34, 218, 210, 1489, 10, 201, 351, 52, 156, 85, 35, 55, 16, 43, 97, 34, 2346, 49, 2, 40, 332, 14, 65, 20, 26, 72, 55, 77, 31, 57, 58, 47, 31, 96, 126, 39, 66, 87, 15, 166, 66, 96, 57, 150, 488, 35, 328, 14890, 225, 362, 213, 552, 122, 834, 229, 1913, 200, 130, 192, 498, 96, 202, 175, 223, 189, 486, 464, 150, 2983, 116, 155537, 248, 348, 4021842, 366, 1064, 81267, 400, 361, 228, 855, 777, 264, 1572, 510, 1027419, 710, 2267, 2055, 814, 668, 87, 461, 602517, 62, 341, 717, 386, 673, 654, 751, 209, 573, 284, 0, 45, 19, 69, 22, 31, 9, 69, 23, 17, 46, 16, 0, 21, 52, 24, 13, 227, 10, 46, 57, 341, 1789, 45, 21, 309, 1742, 1906, 39, 17, 62, 119, 2997, 772, 129, 94, 37, 75, 42, 145, 128, 88, 1987, 100, 214, 227, 192, 415, 926, 238, 193, 49, 13, 74, 88, 114, 150, 833, 219, 39]
        following = [955, 533, 98, 651, 126, 150, 177, 76, 2713, 813, 1173, 365, 583, 248, 2701, 900, 289, 694, 1878, 776, 999, 416, 470, 956, 61, 179, 665, 176, 130, 174, 1517, 952, 170, 967, 674, 2703, 328, 680, 112, 98, 11, 583, 1359, 16, 8, 0, 183, 208, 546, 666, 461, 1109, 432, 761, 376, 261, 643, 283, 598, 228, 97, 447, 100, 151, 528, 1882, 266, 744, 1255, 639, 452, 568, 163, 362, 324, 37, 998, 245, 288, 675, 256, 395, 360, 629, 526, 489, 1440, 899, 1713, 899, 1410, 1925, 748, 469, 1074, 935, 599, 418, 999, 438, 413, 55, 222, 20, 173, 591, 638, 589, 390, 75, 1155, 1854, 208, 164, 333, 4659, 1093, 413, 2047, 438, 132, 413, 689, 164, 178, 1142, 209, 424, 80, 719, 7500, 703, 3296, 270, 65, 610, 7202, 1039, 524, 138, 806, 503, 1208, 802, 111, 475, 1061, 305, 375, 72, 371, 633, 1016, 1065, 7399, 1216, 2928, 635, 417, 101, 383, 489, 96, 535, 399, 3, 446, 387, 1196, 1364, 232, 261, 1159, 4664, 1060, 3932, 280, 529, 455, 407, 278, 127, 111, 456, 363, 360, 311, 364, 176, 172, 149, 76, 1223, 529, 905, 523, 652, 652, 238, 502, 754, 373, 351, 133, 32, 1371, 996, 544, 517, 396, 292, 463, 345, 584, 1000, 67, 157, 716, 272, 414, 292, 164, 748, 335, 177, 331, 124, 271, 268, 582, 333, 701, 237, 3678, 321, 1486, 917, 178, 673, 121, 653, 50, 107, 395, 13, 3164, 15, 569, 137, 488, 372, 61, 77, 430, 333, 545, 2187, 87, 53, 609, 555, 387, 555, 345, 1072, 618, 300, 426, 1631, 370, 1002, 488, 52, 119, 462, 346, 7500, 1200, 264, 694, 34, 323, 81, 1213, 294, 408, 22, 114, 333, 31, 445, 80, 309, 64, 11, 853, 23, 5, 18, 34, 8, 0, 213, 10, 58, 77, 37, 10, 4, 279, 15, 44, 17, 42, 60, 6, 215, 126, 48, 802, 46, 601, 168, 689, 230, 15, 49, 236, 52, 35, 44, 767, 37, 79, 91, 41, 3, 229, 1165, 0, 1, 30, 244, 935, 167, 0, 86, 129, 305, 48, 47, 179, 41, 750, 39, 3646, 35, 170, 333, 694, 1124, 155, 106, 171, 108, 26, 13, 68, 44, 151, 37, 139, 28, 38, 60, 69, 6, 319, 29, 420, 87, 733, 121, 45, 249, 56, 16, 46, 45, 25, 71, 0, 104, 31, 99, 157, 64, 40, 1762, 82, 2980, 63, 500, 177, 130, 135, 192, 36, 2, 181, 71, 8, 167, 22, 208, 146, 64, 8, 92, 4118, 392, 221, 40, 82, 25, 44, 227, 304, 123, 8, 87, 11, 66, 303, 90, 336, 49, 88, 136, 151, 24, 26, 295, 137, 618, 74, 233, 76, 38, 109, 474, 16, 161, 894, 17, 4, 98, 61, 59, 2330, 433, 1269, 76, 14, 60, 22, 595, 9, 1, 1, 1990, 7, 32, 76, 15, 792, 98, 23, 17, 1, 48, 638, 747, 82, 24, 6, 22, 83, 0, 5, 403, 26, 0, 26, 11, 46, 0, 20, 0, 11, 30, 56, 22, 1, 27, 20, 49, 1029, 1417, 39, 2426, 828, 26, 2, 12, 4, 0, 2176, 4, 0, 58, 45, 240, 9, 1, 26, 289, 66, 23, 153, 1155, 825, 36, 1528, 1543, 3715, 2, 812, 2663, 16, 423, 477, 38, 28, 51, 88, 408, 112, 7272, 95, 55, 19, 1333, 542, 162, 52, 27, 434, 2, 108, 215, 130, 347, 139, 37, 242, 860, 229, 161, 698, 64, 596, 75, 339, 73, 487, 604, 6, 668, 7369, 356, 424, 254, 521, 143, 358, 492, 436, 437, 622, 141, 337, 499, 605, 199, 694, 276, 862, 367, 157, 545, 138, 1395, 490, 347, 5514, 552, 573, 963, 449, 562, 346, 151, 148, 151, 3504, 185, 293, 549, 466, 993, 1111, 605, 40, 1055, 482, 47, 274, 223, 363, 568, 535, 577, 276, 474, 505, 2, 64, 30, 694, 82, 124, 25, 694, 33, 34, 38, 2, 18, 1, 15, 2, 22, 353, 24, 18, 22, 2287, 6153, 64, 31, 250, 6172, 2129, 324, 33, 126, 350, 764, 3239, 920, 105, 58, 55, 175, 202, 636, 72, 7453, 162, 829, 776, 942, 1445, 4239, 1381, 669, 235, 7, 270, 76, 811, 164, 3572, 1695, 68]
        posts = [32, 286, 13, 679, 6, 344, 16, 33, 72, 213, 648, 76, 298, 117, 487, 254, 59, 1570, 378, 526, 228, 35, 281, 285, 148, 57, 17, 511, 230, 15, 980, 53, 111, 719, 1164, 497, 18, 50, 74, 8, 7389, 420, 433, 156, 4494, 751, 4, 27, 91, 262, 274, 271, 713, 200, 12, 26, 75, 94, 63, 69, 12, 63, 19, 100, 661, 149, 22, 400, 149, 122, 74, 13, 8, 77, 5, 3, 106, 14, 172, 111, 38, 19, 227, 221, 580, 40, 101, 157, 197, 61, 698, 49, 85, 77, 58, 232, 20, 98, 559, 189, 388, 28, 156, 6, 69, 775, 205, 209, 334, 9, 6, 416, 13, 33, 1, 711, 114, 16, 107, 5, 7, 21, 65, 10, 59, 137, 10, 571, 24, 328, 161, 280, 92, 31, 0, 25, 921, 1020, 301, 9, 158, 43, 24, 60, 4, 220, 1159, 8, 396, 38, 1, 2, 43, 131, 7, 57, 36, 91, 8, 11, 252, 15, 74, 83, 126, 663, 0, 10, 8, 24, 65, 64, 664, 130, 131, 917, 2, 142, 165, 80, 32, 81, 334, 8, 373, 56, 7, 12, 5, 77, 93, 192, 8, 145, 135, 18, 222, 222, 5, 119, 201, 12, 301, 20, 112, 54, 98, 16, 133, 142, 63, 70, 403, 15, 990, 12, 26, 2, 24, 411, 217, 156, 389, 8, 3, 22, 59, 144, 2, 78, 28, 111, 6, 4, 31, 86, 240, 11, 44, 9, 62, 0, 15, 53, 2, 52, 1, 62, 247, 9, 13, 204, 0, 51, 15, 108, 353, 5, 560, 85, 95, 14, 52, 7, 197, 89, 34, 283, 65, 126, 327, 42, 36, 3, 53, 7, 103, 241, 103, 93, 1, 16, 32, 1232, 75, 5, 3, 30, 0, 0, 2, 3, 13, 0, 1, 0, 10, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 141, 6, 1, 0, 1, 39, 0, 9, 0, 21, 0, 0, 0, 3, 0, 0, 0, 0, 0, 6, 0, 0, 1, 4, 0, 0, 0, 0, 0, 17, 0, 1, 0, 7, 13, 0, 0, 0, 5, 124, 9, 5, 2, 0, 150, 29, 108, 77, 3, 7, 3, 131, 40, 4, 84, 299, 11, 0, 0, 1, 4, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 7, 3, 0, 0, 5, 0, 1, 0, 12, 0, 0, 0, 1, 92, 0, 0, 0, 0, 21, 7, 9, 0, 14, 0, 0, 3, 0, 0, 1, 1, 0, 1, 0, 1, 28, 0, 25, 0, 0, 111, 2, 0, 0, 0, 0, 0, 5, 10, 3, 19, 0, 0, 8, 2, 10, 29, 0, 0, 2, 3, 5, 0, 63, 1, 4, 34, 0, 0, 6, 2, 7, 0, 0, 5, 0, 0, 0, 4, 1, 26, 9, 4, 4, 0, 0, 0, 0, 1, 0, 0, 28, 0, 1, 0, 2, 2, 9, 1, 8, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 4, 0, 5, 10, 1, 2, 0, 0, 0, 2, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 1, 37, 8, 4, 0, 28, 0, 0, 6, 12, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 12, 1, 0, 0, 1, 12, 59, 0, 0, 23, 3, 11, 8, 102, 6, 25, 0, 33, 44, 4, 0, 2, 35, 3, 319, 273, 6, 6, 9, 19, 17, 9, 53, 97, 17, 8, 60, 51, 25, 188, 590, 251, 0, 58, 46, 19, 250, 28, 1065, 209, 5, 1879, 9, 253, 90, 8, 12, 13, 59, 77, 14, 330, 2, 932, 6, 463, 62, 247, 85, 0, 118, 307, 9, 25, 42, 14, 78, 465, 65, 9, 145, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 3, 8, 3, 0, 0, 34, 4, 0, 1, 1, 1, 0, 0, 15, 4, 70, 2, 81, 0, 5, 21, 3, 2, 16, 3, 23, 6, 4, 0, 60, 1, 0, 0, 2, 8, 13, 4, 3, 1, 3]


        self.set_camera_orientation(phi=2*PI/5, theta=PI/5, focal_distance=10000)
        axes = ThreeDAxes(
            x_range=[0, 10000, 1000],
            y_range=[0, 5000, 1000],
            z_range=[min(posts), max(posts), 1000], 
        ).add_coordinates()
        """
        labels = axes.get_axis_labels(
            Tex("x-axis").scale(0.7), Text("y-axis").scale(0.45), Text("z-axis").scale(0.45)
        )
        """
        self.add(axes) # , labels)



        zipped = list(zip(followers, following, posts))
        dots = VGroup(*[Dot(axes.c2p(x, y, z)) for x,y,z in zipped])
        self.play(
            Write(dots)
        )
        self.wait()



        new_axes = ThreeDAxes(
            x_range=[0, 10000, 1000],
            y_range=[0, 5000, 1000], 
            z_range=[0, 100, 10],
        ).add_coordinates()
        new_dots = VGroup(*[Dot(new_axes.c2p(x, y, z)) for x,y,z in zipped if x <= 10000])
        self.play(
            ReplacementTransform(axes, new_axes),
            ReplacementTransform(dots, new_dots),
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