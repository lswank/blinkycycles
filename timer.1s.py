#!/usr/bin/python3

# <xbar.title>Blinky Cycles</xbar.title>
# <xbar.version>v0.3.0</xbar.version>
# <xbar.author>Lorenzo Swank</xbar.author>
# <xbar.author.github>LSwank</xbar.author.github>
# <xbar.desc>A work timer with functions to display work status with the
# blink(1) LED device.</xbar.desc>
# <xbar.dependencies>python</xbar.dependencies>

import math
import os
import subprocess
import sys
from datetime import datetime, timedelta
from blink1.blink1 import Blink1

colors = {
    "indian red": [176, 23, 31],
    "crimson": [220, 20, 60],
    "lightpink": [255, 182, 193],
    "lightpink 1": [255, 174, 185],
    "lightpink 2": [238, 162, 173],
    "lightpink 3": [205, 140, 149],
    "lightpink 4": [139, 95, 101],
    "pink": [255, 192, 203],
    "pink 1": [255, 181, 197],
    "pink 2": [238, 169, 184],
    "pink 3": [205, 145, 158],
    "pink 4": [139, 99, 108],
    "palevioletred": [219, 112, 147],
    "palevioletred 1": [255, 130, 171],
    "palevioletred 2": [238, 121, 159],
    "palevioletred 3": [205, 104, 137],
    "palevioletred 4": [139, 71, 93],
    "lavenderblush 1 (lavenderblush)": [255, 240, 245],
    "lavenderblush 2": [238, 224, 229],
    "lavenderblush 3": [205, 193, 197],
    "lavenderblush 4": [139, 131, 134],
    "violetred 1": [255, 62, 150],
    "violetred 2": [238, 58, 140],
    "violetred 3": [205, 50, 120],
    "violetred 4": [139, 34, 82],
    "hotpink": [255, 105, 180],
    "hotpink 1": [255, 110, 180],
    "hotpink 2": [238, 106, 167],
    "hotpink 3": [205, 96, 144],
    "hotpink 4": [139, 58, 98],
    "raspberry": [135, 38, 87],
    "deeppink 1 (deeppink)": [255, 20, 147],
    "deeppink 2": [238, 18, 137],
    "deeppink 3": [205, 16, 118],
    "deeppink 4": [139, 10, 80],
    "maroon 1": [255, 52, 179],
    "maroon 2": [238, 48, 167],
    "maroon 3": [205, 41, 144],
    "maroon 4": [139, 28, 98],
    "mediumvioletred": [199, 21, 133],
    "violetred": [208, 32, 144],
    "orchid": [218, 112, 214],
    "orchid 1": [255, 131, 250],
    "orchid 2": [238, 122, 233],
    "orchid 3": [205, 105, 201],
    "orchid 4": [139, 71, 137],
    "thistle": [216, 191, 216],
    "thistle 1": [255, 225, 255],
    "thistle 2": [238, 210, 238],
    "thistle 3": [205, 181, 205],
    "thistle 4": [139, 123, 139],
    "plum 1": [255, 187, 255],
    "plum 2": [238, 174, 238],
    "plum 3": [205, 150, 205],
    "plum 4": [139, 102, 139],
    "plum": [221, 160, 221],
    "violet": [238, 130, 238],
    "magenta (fuchsia*)": [255, 0, 255],
    "magenta 2": [238, 0, 238],
    "magenta 3": [205, 0, 205],
    "magenta 4 (darkmagenta)": [139, 0, 139],
    "purple*": [128, 0, 128],
    "mediumorchid": [186, 85, 211],
    "mediumorchid 1": [224, 102, 255],
    "mediumorchid 2": [209, 95, 238],
    "mediumorchid 3": [180, 82, 205],
    "mediumorchid 4": [122, 55, 139],
    "darkviolet": [148, 0, 211],
    "darkorchid": [153, 50, 204],
    "darkorchid 1": [191, 62, 255],
    "darkorchid 2": [178, 58, 238],
    "darkorchid 3": [154, 50, 205],
    "darkorchid 4": [104, 34, 139],
    "indigo": [75, 0, 130],
    "blueviolet": [138, 43, 226],
    "purple 1": [155, 48, 255],
    "purple 2": [145, 44, 238],
    "purple 3": [125, 38, 205],
    "purple 4": [85, 26, 139],
    "mediumpurple": [147, 112, 219],
    "mediumpurple 1": [171, 130, 255],
    "mediumpurple 2": [159, 121, 238],
    "mediumpurple 3": [137, 104, 205],
    "mediumpurple 4": [93, 71, 139],
    "darkslateblue": [72, 61, 139],
    "lightslateblue": [132, 112, 255],
    "mediumslateblue": [123, 104, 238],
    "slateblue": [106, 90, 205],
    "slateblue 1": [131, 111, 255],
    "slateblue 2": [122, 103, 238],
    "slateblue 3": [105, 89, 205],
    "slateblue 4": [71, 60, 139],
    "ghostwhite": [248, 248, 255],
    "lavender": [230, 230, 250],
    "blue*": [0, 0, 255],
    "blue 2": [0, 0, 238],
    "blue 3 (mediumblue)": [0, 0, 205],
    "blue 4 (darkblue)": [0, 0, 139],
    "navy*": [0, 0, 128],
    "midnightblue": [25, 25, 112],
    "cobalt": [61, 89, 171],
    "royalblue": [65, 105, 225],
    "royalblue 1": [72, 118, 255],
    "royalblue 2": [67, 110, 238],
    "royalblue 3": [58, 95, 205],
    "royalblue 4": [39, 64, 139],
    "cornflowerblue": [100, 149, 237],
    "lightsteelblue": [176, 196, 222],
    "lightsteelblue 1": [202, 225, 255],
    "lightsteelblue 2": [188, 210, 238],
    "lightsteelblue 3": [162, 181, 205],
    "lightsteelblue 4": [110, 123, 139],
    "lightslategray": [119, 136, 153],
    "slategray": [112, 128, 144],
    "slategray 1": [198, 226, 255],
    "slategray 2": [185, 211, 238],
    "slategray 3": [159, 182, 205],
    "slategray 4": [108, 123, 139],
    "dodgerblue 1 (dodgerblue)": [30, 144, 255],
    "dodgerblue 2": [28, 134, 238],
    "dodgerblue 3": [24, 116, 205],
    "dodgerblue 4": [16, 78, 139],
    "aliceblue": [240, 248, 255],
    "steelblue": [70, 130, 180],
    "steelblue 1": [99, 184, 255],
    "steelblue 2": [92, 172, 238],
    "steelblue 3": [79, 148, 205],
    "steelblue 4": [54, 100, 139],
    "lightskyblue": [135, 206, 250],
    "lightskyblue 1": [176, 226, 255],
    "lightskyblue 2": [164, 211, 238],
    "lightskyblue 3": [141, 182, 205],
    "lightskyblue 4": [96, 123, 139],
    "skyblue 1": [135, 206, 255],
    "skyblue 2": [126, 192, 238],
    "skyblue 3": [108, 166, 205],
    "skyblue 4": [74, 112, 139],
    "skyblue": [135, 206, 235],
    "deepskyblue 1 (deepskyblue)": [0, 191, 255],
    "deepskyblue 2": [0, 178, 238],
    "deepskyblue 3": [0, 154, 205],
    "deepskyblue 4": [0, 104, 139],
    "peacock": [51, 161, 201],
    "lightblue": [173, 216, 230],
    "lightblue 1": [191, 239, 255],
    "lightblue 2": [178, 223, 238],
    "lightblue 3": [154, 192, 205],
    "lightblue 4": [104, 131, 139],
    "powderblue": [176, 224, 230],
    "cadetblue 1": [152, 245, 255],
    "cadetblue 2": [142, 229, 238],
    "cadetblue 3": [122, 197, 205],
    "cadetblue 4": [83, 134, 139],
    "turquoise 1": [0, 245, 255],
    "turquoise 2": [0, 229, 238],
    "turquoise 3": [0, 197, 205],
    "turquoise 4": [0, 134, 139],
    "cadetblue": [95, 158, 160],
    "darkturquoise": [0, 206, 209],
    "azure 1 (azure)": [240, 255, 255],
    "azure 2": [224, 238, 238],
    "azure 3": [193, 205, 205],
    "azure 4": [131, 139, 139],
    "lightcyan 1 (lightcyan)": [224, 255, 255],
    "lightcyan 2": [209, 238, 238],
    "lightcyan 3": [180, 205, 205],
    "lightcyan 4": [122, 139, 139],
    "paleturquoise 1": [187, 255, 255],
    "paleturquoise 2 (paleturquoise)": [174, 238, 238],
    "paleturquoise 3": [150, 205, 205],
    "paleturquoise 4": [102, 139, 139],
    "darkslategray": [47, 79, 79],
    "darkslategray 1": [151, 255, 255],
    "darkslategray 2": [141, 238, 238],
    "darkslategray 3": [121, 205, 205],
    "darkslategray 4": [82, 139, 139],
    "cyan / aqua*": [0, 255, 255],
    "cyan 2": [0, 238, 238],
    "cyan 3": [0, 205, 205],
    "cyan 4 (darkcyan)": [0, 139, 139],
    "teal*": [0, 128, 128],
    "mediumturquoise": [72, 209, 204],
    "lightseagreen": [32, 178, 170],
    "manganeseblue": [3, 168, 158],
    "turquoise": [64, 224, 208],
    "coldgrey": [128, 138, 135],
    "turquoiseblue": [0, 199, 140],
    "aquamarine 1 (aquamarine)": [127, 255, 212],
    "aquamarine 2": [118, 238, 198],
    "aquamarine 3 (mediumaquamarine)": [102, 205, 170],
    "aquamarine 4": [69, 139, 116],
    "mediumspringgreen": [0, 250, 154],
    "mintcream": [245, 255, 250],
    "springgreen": [0, 255, 127],
    "springgreen 1": [0, 238, 118],
    "springgreen 2": [0, 205, 102],
    "springgreen 3": [0, 139, 69],
    "mediumseagreen": [60, 179, 113],
    "seagreen 1": [84, 255, 159],
    "seagreen 2": [78, 238, 148],
    "seagreen 3": [67, 205, 128],
    "seagreen 4 (seagreen)": [46, 139, 87],
    "emeraldgreen": [0, 201, 87],
    "mint": [189, 252, 201],
    "cobaltgreen": [61, 145, 64],
    "honeydew 1 (honeydew)": [240, 255, 240],
    "honeydew 2": [224, 238, 224],
    "honeydew 3": [193, 205, 193],
    "honeydew 4": [131, 139, 131],
    "darkseagreen": [143, 188, 143],
    "darkseagreen 1": [193, 255, 193],
    "darkseagreen 2": [180, 238, 180],
    "darkseagreen 3": [155, 205, 155],
    "darkseagreen 4": [105, 139, 105],
    "palegreen": [152, 251, 152],
    "palegreen 1": [154, 255, 154],
    "palegreen 2 (lightgreen)": [144, 238, 144],
    "palegreen 3": [124, 205, 124],
    "palegreen 4": [84, 139, 84],
    "limegreen": [50, 205, 50],
    "forestgreen": [34, 139, 34],
    "green 1 (lime*)": [0, 255, 0],
    "green 2": [0, 238, 0],
    "green 3": [0, 205, 0],
    "green 4": [0, 139, 0],
    "green*": [0, 128, 0],
    "darkgreen": [0, 100, 0],
    "sapgreen": [48, 128, 20],
    "lawngreen": [124, 252, 0],
    "chartreuse 1 (chartreuse)": [127, 255, 0],
    "chartreuse 2": [118, 238, 0],
    "chartreuse 3": [102, 205, 0],
    "chartreuse 4": [69, 139, 0],
    "greenyellow": [173, 255, 47],
    "darkolivegreen 1": [202, 255, 112],
    "darkolivegreen 2": [188, 238, 104],
    "darkolivegreen 3": [162, 205, 90],
    "darkolivegreen 4": [110, 139, 61],
    "darkolivegreen": [85, 107, 47],
    "olivedrab": [107, 142, 35],
    "olivedrab 1": [192, 255, 62],
    "olivedrab 2": [179, 238, 58],
    "olivedrab 3 (yellowgreen)": [154, 205, 50],
    "olivedrab 4": [105, 139, 34],
    "ivory 1 (ivory)": [255, 255, 240],
    "ivory 2": [238, 238, 224],
    "ivory 3": [205, 205, 193],
    "ivory 4": [139, 139, 131],
    "beige": [245, 245, 220],
    "lightyellow 1 (lightyellow)": [255, 255, 224],
    "lightyellow 2": [238, 238, 209],
    "lightyellow 3": [205, 205, 180],
    "lightyellow 4": [139, 139, 122],
    "lightgoldenrodyellow": [250, 250, 210],
    "yellow 1 (yellow*)": [255, 255, 0],
    "yellow 2": [238, 238, 0],
    "yellow 3": [205, 205, 0],
    "yellow 4": [139, 139, 0],
    "warmgrey": [128, 128, 105],
    "olive*": [128, 128, 0],
    "darkkhaki": [189, 183, 107],
    "khaki 1": [255, 246, 143],
    "khaki 2": [238, 230, 133],
    "khaki 3": [205, 198, 115],
    "khaki 4": [139, 134, 78],
    "khaki": [240, 230, 140],
    "palegoldenrod": [238, 232, 170],
    "lemonchiffon 1 (lemonchiffon)": [255, 250, 205],
    "lemonchiffon 2": [238, 233, 191],
    "lemonchiffon 3": [205, 201, 165],
    "lemonchiffon 4": [139, 137, 112],
    "lightgoldenrod 1": [255, 236, 139],
    "lightgoldenrod 2": [238, 220, 130],
    "lightgoldenrod 3": [205, 190, 112],
    "lightgoldenrod 4": [139, 129, 76],
    "banana": [227, 207, 87],
    "gold 1 (gold)": [255, 215, 0],
    "gold 2": [238, 201, 0],
    "gold 3": [205, 173, 0],
    "gold 4": [139, 117, 0],
    "cornsilk 1 (cornsilk)": [255, 248, 220],
    "cornsilk 2": [238, 232, 205],
    "cornsilk 3": [205, 200, 177],
    "cornsilk 4": [139, 136, 120],
    "goldenrod": [218, 165, 32],
    "goldenrod 1": [255, 193, 37],
    "goldenrod 2": [238, 180, 34],
    "goldenrod 3": [205, 155, 29],
    "goldenrod 4": [139, 105, 20],
    "darkgoldenrod": [184, 134, 11],
    "darkgoldenrod 1": [255, 185, 15],
    "darkgoldenrod 2": [238, 173, 14],
    "darkgoldenrod 3": [205, 149, 12],
    "darkgoldenrod 4": [139, 101, 8],
    "orange 1 (orange)": [255, 165, 0],
    "orange 2": [238, 154, 0],
    "orange 3": [205, 133, 0],
    "orange 4": [139, 90, 0],
    "floralwhite": [255, 250, 240],
    "oldlace": [253, 245, 230],
    "wheat": [245, 222, 179],
    "wheat 1": [255, 231, 186],
    "wheat 2": [238, 216, 174],
    "wheat 3": [205, 186, 150],
    "wheat 4": [139, 126, 102],
    "moccasin": [255, 228, 181],
    "papayawhip": [255, 239, 213],
    "blanchedalmond": [255, 235, 205],
    "navajowhite 1 (navajowhite)": [255, 222, 173],
    "navajowhite 2": [238, 207, 161],
    "navajowhite 3": [205, 179, 139],
    "navajowhite 4": [139, 121, 94],
    "eggshell": [252, 230, 201],
    "tan": [210, 180, 140],
    "brick": [156, 102, 31],
    "cadmiumyellow": [255, 153, 18],
    "antiquewhite": [250, 235, 215],
    "antiquewhite 1": [255, 239, 219],
    "antiquewhite 2": [238, 223, 204],
    "antiquewhite 3": [205, 192, 176],
    "antiquewhite 4": [139, 131, 120],
    "burlywood": [222, 184, 135],
    "burlywood 1": [255, 211, 155],
    "burlywood 2": [238, 197, 145],
    "burlywood 3": [205, 170, 125],
    "burlywood 4": [139, 115, 85],
    "bisque 1 (bisque)": [255, 228, 196],
    "bisque 2": [238, 213, 183],
    "bisque 3": [205, 183, 158],
    "bisque 4": [139, 125, 107],
    "melon": [227, 168, 105],
    "carrot": [237, 145, 33],
    "darkorange": [255, 140, 0],
    "darkorange 1": [255, 127, 0],
    "darkorange 2": [238, 118, 0],
    "darkorange 3": [205, 102, 0],
    "darkorange 4": [139, 69, 0],
    "orange": [255, 128, 0],
    "tan 1": [255, 165, 79],
    "tan 2": [238, 154, 73],
    "tan 3 (peru)": [205, 133, 63],
    "tan 4": [139, 90, 43],
    "linen": [250, 240, 230],
    "peachpuff 1 (peachpuff)": [255, 218, 185],
    "peachpuff 2": [238, 203, 173],
    "peachpuff 3": [205, 175, 149],
    "peachpuff 4": [139, 119, 101],
    "seashell 1 (seashell)": [255, 245, 238],
    "seashell 2": [238, 229, 222],
    "seashell 3": [205, 197, 191],
    "seashell 4": [139, 134, 130],
    "sandybrown": [244, 164, 96],
    "rawsienna": [199, 97, 20],
    "chocolate": [210, 105, 30],
    "chocolate 1": [255, 127, 36],
    "chocolate 2": [238, 118, 33],
    "chocolate 3": [205, 102, 29],
    "chocolate 4 (saddlebrown)": [139, 69, 19],
    "ivoryblack": [41, 36, 33],
    "flesh": [255, 125, 64],
    "cadmiumorange": [255, 97, 3],
    "burntsienna": [138, 54, 15],
    "sienna": [160, 82, 45],
    "sienna 1": [255, 130, 71],
    "sienna 2": [238, 121, 66],
    "sienna 3": [205, 104, 57],
    "sienna 4": [139, 71, 38],
    "lightsalmon 1 (lightsalmon)": [255, 160, 122],
    "lightsalmon 2": [238, 149, 114],
    "lightsalmon 3": [205, 129, 98],
    "lightsalmon 4": [139, 87, 66],
    "coral": [255, 127, 80],
    "orangered 1 (orangered)": [255, 69, 0],
    "orangered 2": [238, 64, 0],
    "orangered 3": [205, 55, 0],
    "orangered 4": [139, 37, 0],
    "sepia": [94, 38, 18],
    "darksalmon": [233, 150, 122],
    "salmon 1": [255, 140, 105],
    "salmon 2": [238, 130, 98],
    "salmon 3": [205, 112, 84],
    "salmon 4": [139, 76, 57],
    "coral 1": [255, 114, 86],
    "coral 2": [238, 106, 80],
    "coral 3": [205, 91, 69],
    "coral 4": [139, 62, 47],
    "burntumber": [138, 51, 36],
    "tomato 1 (tomato)": [255, 99, 71],
    "tomato 2": [238, 92, 66],
    "tomato 3": [205, 79, 57],
    "tomato 4": [139, 54, 38],
    "salmon": [250, 128, 114],
    "mistyrose 1 (mistyrose)": [255, 228, 225],
    "mistyrose 2": [238, 213, 210],
    "mistyrose 3": [205, 183, 181],
    "mistyrose 4": [139, 125, 123],
    "scurrent_date_and_time 1 (scurrent_date_and_time)": [255, 250, 250],
    "scurrent_date_and_time 2": [238, 233, 233],
    "scurrent_date_and_time 3": [205, 201, 201],
    "scurrent_date_and_time 4": [139, 137, 137],
    "rosybrown": [188, 143, 143],
    "rosybrown 1": [255, 193, 193],
    "rosybrown 2": [238, 180, 180],
    "rosybrown 3": [205, 155, 155],
    "rosybrown 4": [139, 105, 105],
    "lightcoral": [240, 128, 128],
    "indianred": [205, 92, 92],
    "indianred 1": [255, 106, 106],
    "indianred 2": [238, 99, 99],
    "indianred 4": [139, 58, 58],
    "indianred 3": [205, 85, 85],
    "brown": [165, 42, 42],
    "brown 1": [255, 64, 64],
    "brown 2": [238, 59, 59],
    "brown 3": [205, 51, 51],
    "brown 4": [139, 35, 35],
    "firebrick": [178, 34, 34],
    "firebrick 1": [255, 48, 48],
    "firebrick 2": [238, 44, 44],
    "firebrick 3": [205, 38, 38],
    "firebrick 4": [139, 26, 26],
    "red 1 (red*)": [255, 0, 0],
    "red 2": [238, 0, 0],
    "red 3": [205, 0, 0],
    "red 4 (darkred)": [139, 0, 0],
    "maroon*": [128, 0, 0],
    "sgi beet": [142, 56, 142],
    "sgi slateblue": [113, 113, 198],
    "sgi lightblue": [125, 158, 192],
    "sgi teal": [56, 142, 142],
    "sgi chartreuse": [113, 198, 113],
    "sgi olivedrab": [142, 142, 56],
    "sgi brightgray": [197, 193, 170],
    "sgi salmon": [198, 113, 113],
    "sgi darkgray": [85, 85, 85],
    "sgi gray 12": [30, 30, 30],
    "sgi gray 16": [40, 40, 40],
    "sgi gray 32": [81, 81, 81],
    "sgi gray 36": [91, 91, 91],
    "sgi gray 52": [132, 132, 132],
    "sgi gray 56": [142, 142, 142],
    "sgi lightgray": [170, 170, 170],
    "sgi gray 72": [183, 183, 183],
    "sgi gray 76": [193, 193, 193],
    "sgi gray 92": [234, 234, 234],
    "sgi gray 96": [244, 244, 244],
    "white*": [255, 255, 255],
    "white smoke (gray 96)": [245, 245, 245],
    "gainsboro": [220, 220, 220],
    "lightgrey": [211, 211, 211],
    "silver*": [192, 192, 192],
    "darkgray": [169, 169, 169],
    "gray*": [128, 128, 128],
    "dimgray (gray 42)": [105, 105, 105],
    "black*": [0, 0, 0],
    "gray 99": [252, 252, 252],
    "gray 98": [250, 250, 250],
    "gray 97": [247, 247, 247],
    "gray 96": [245, 245, 245],
    "gray 95": [242, 242, 242],
    "gray 94": [240, 240, 240],
    "gray 93": [237, 237, 237],
    "gray 92": [235, 235, 235],
    "gray 91": [232, 232, 232],
    "gray 90": [229, 229, 229],
    "gray 89": [227, 227, 227],
    "gray 88": [224, 224, 224],
    "gray 87": [222, 222, 222],
    "gray 86": [219, 219, 219],
    "gray 85": [217, 217, 217],
    "gray 84": [214, 214, 214],
    "gray 83": [212, 212, 212],
    "gray 82": [209, 209, 209],
    "gray 81": [207, 207, 207],
    "gray 80": [204, 204, 204],
    "gray 79": [201, 201, 201],
    "gray 78": [199, 199, 199],
    "gray 77": [196, 196, 196],
    "gray 76": [194, 194, 194],
    "gray 75": [191, 191, 191],
    "gray 74": [189, 189, 189],
    "gray 73": [186, 186, 186],
    "gray 72": [184, 184, 184],
    "gray 71": [181, 181, 181],
    "gray 70": [179, 179, 179],
    "gray 69": [176, 176, 176],
    "gray 68": [173, 173, 173],
    "gray 67": [171, 171, 171],
    "gray 66": [168, 168, 168],
    "gray 65": [166, 166, 166],
    "gray 64": [163, 163, 163],
    "gray 63": [161, 161, 161],
    "gray 62": [158, 158, 158],
    "gray 61": [156, 156, 156],
    "gray 60": [153, 153, 153],
    "gray 59": [150, 150, 150],
    "gray 58": [148, 148, 148],
    "gray 57": [145, 145, 145],
    "gray 56": [143, 143, 143],
    "gray 55": [140, 140, 140],
    "gray 54": [138, 138, 138],
    "gray 53": [135, 135, 135],
    "gray 52": [133, 133, 133],
    "gray 51": [130, 130, 130],
    "gray 50": [127, 127, 127],
    "gray 49": [125, 125, 125],
    "gray 48": [122, 122, 122],
    "gray 47": [120, 120, 120],
    "gray 46": [117, 117, 117],
    "gray 45": [115, 115, 115],
    "gray 44": [112, 112, 112],
    "gray 43": [110, 110, 110],
    "gray 42": [107, 107, 107],
    "gray 40": [102, 102, 102],
    "gray 39": [99, 99, 99],
    "gray 38": [97, 97, 97],
    "gray 37": [94, 94, 94],
    "gray 36": [92, 92, 92],
    "gray 35": [89, 89, 89],
    "gray 34": [87, 87, 87],
    "gray 33": [84, 84, 84],
    "gray 32": [82, 82, 82],
    "gray 31": [79, 79, 79],
    "gray 30": [77, 77, 77],
    "gray 29": [74, 74, 74],
    "gray 28": [71, 71, 71],
    "gray 27": [69, 69, 69],
    "gray 26": [66, 66, 66],
    "gray 25": [64, 64, 64],
    "gray 24": [61, 61, 61],
    "gray 23": [59, 59, 59],
    "gray 22": [56, 56, 56],
    "gray 21": [54, 54, 54],
    "gray 20": [51, 51, 51],
    "gray 19": [48, 48, 48],
    "gray 18": [46, 46, 46],
    "gray 17": [43, 43, 43],
    "gray 16": [41, 41, 41],
    "gray 15": [38, 38, 38],
    "gray 14": [36, 36, 36],
    "gray 13": [33, 33, 33],
    "gray 12": [31, 31, 31],
    "gray 11": [28, 28, 28],
    "gray 10": [26, 26, 26],
    "gray 9": [23, 23, 23],
    "gray 8": [20, 20, 20],
    "gray 7": [18, 18, 18],
    "gray 6": [15, 15, 15],
    "gray 5": [13, 13, 13],
    "gray 4": [10, 10, 10],
    "gray 3": [8, 8, 8],
    "gray 2": [5, 5, 5],
    "gray 1": [3, 3, 3],
}

# A function to convert from an RGB triple to a hex string. The output
# is of the form 0xAARRGGBB where the AA alpha channel is always 0xFF.
def rgb_to_hex_string(rgb):
    return "0xFF" + "".join(["%02X" % x for x in rgb])


# A function to run the command line command
# yabai -m config active_window_border_color
# with an RGB color in quotations at the end. Ignore the output.
def set_border_color(rgb):
    # Check to see if /opt/homebrew/bin/yabai exists
    if os.path.exists("/opt/homebrew/bin/yabai"):
        # Run the command and print the output
        os.system(
            '/opt/homebrew/bin/yabai -m config active_window_border_color "' + rgb + '"'
        )


# Determine if the blink(1) device is available.
# Application works without blink(1) device.
blink1_is_available = False
try:
    blink1_controller = Blink1()
    blink1_is_available = True
except Exception as e:
    sys.stderr.write("Error: " + str(e) + "\n")
    blink1_is_available = False

# Determine if yabai is available.
# Application works without yabai.
yabai_is_available = False
if os.path.exists("/opt/homebrew/bin/yabai"):
    yabai_is_available = True

# Generate a list of sequential plan and work phases.
plan_phase_duration_in_minutes = 10
work_phase_duration_in_minutes = 30
minutes_in_day = 24 * 60
plan_and_work_phase_list = []
current_date_and_time = datetime.now()
time_marker = datetime(
    current_date_and_time.year,
    current_date_and_time.month,
    current_date_and_time.day,
    0,
    0,
    0,
)
total_period_duration = plan_phase_duration_in_minutes + work_phase_duration_in_minutes
periods_in_day = math.ceil(minutes_in_day / total_period_duration)
for i in range(periods_in_day):
    # Plan
    plan_and_work_phase_list.append((time_marker, "Plan"))
    # Move the marker to the end of the Plan phase.
    time_marker += timedelta(minutes=plan_phase_duration_in_minutes)
    # Work
    plan_and_work_phase_list.append((time_marker, "Work"))
    # Move the marker to the end of the Work phase.
    time_marker += timedelta(minutes=work_phase_duration_in_minutes)


def get_event_index_for_time(event_list, time):
    # Given a sequential list of (event, time) tuples, determine the event
    # associated with a given time.
    index = 0
    for i in range(len(event_list)):
        if event_list[i][0] > time:
            index = i
            break
    return index - 1


def main():
    current_date_and_time = datetime.now()
    index = get_event_index_for_time(plan_and_work_phase_list, current_date_and_time)
    # phaseStartTime = plan_and_work_phase_list[index][0]
    phaseStopTime = plan_and_work_phase_list[index + 1][0]
    currentPhaseLabel = plan_and_work_phase_list[index][1]
    timeRemainingInPhase = phaseStopTime - current_date_and_time

    # Calculate the time remaining in the phase in minutes and seconds.
    minutesRemaining = timeRemainingInPhase.seconds // 60
    secondsRemaining = timeRemainingInPhase.seconds % 60

    desiredRGB = [0, 0, 0]
    if currentPhaseLabel == "Work":
        if minutesRemaining > 2:
            if timeRemainingInPhase.seconds % minutesRemaining == 0:
                desiredRGB = colors["ivoryblack"]
            else:
                desiredRGB = colors["crimson"]
        else:
            if secondsRemaining % 2 == 0:
                desiredRGB = colors["orange"]
            else:
                desiredRGB = colors["crimson"]
    elif currentPhaseLabel == "Plan":
        if minutesRemaining > 8:
            if timeRemainingInPhase.seconds % 2 == 0:
                desiredRGB = colors["crimson"]
            else:
                desiredRGB = colors["springgreen"]
        else:
            desiredRGB = (
                colors["springgreen"]
                if secondsRemaining % 2 == 0
                else colors["lightseagreen"]
            )

    # Set the RGB value of the blink1.
    if blink1_is_available:
        blink1_controller.fade_to_color(
            1000, (desiredRGB[0], desiredRGB[1], desiredRGB[2])
        )

    # If yabai is available, set the border color.
    # Convert the color to hex and run the command line command.
    if yabai_is_available:
        hex_color = rgb_to_hex_string(desiredRGB)
        set_border_color(hex_color)

    # Print the minutes and seconds of time remaining in the phase
    # with a status light (???? or ????) indicating the current phase.
    statusLight = "????" if currentPhaseLabel == "Work" else "????"
    print(
        "%s %s %2d:%02d"
        % (statusLight, currentPhaseLabel, minutesRemaining, secondsRemaining)
    )


if __name__ == "__main__":
    main()
