#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.13.0 with dump python functionality
###

import sys
import salome
import math

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'/home/vd/OpenFOAM/vd-12/run/nozzle_1/geometry')

# входные параметры
P_input = 200000
T_input = 1800
P_output = 9000
G = 1.5
alpha_ = 14
betta_ = 28
R = 287
k = 1.4

# расчет входного сечения
betta_vh = 0.999
# давление
p_vh = betta_vh*P_input
# температура
T_vh = T_input*betta_vh**((k-1)/k)
# удельный объем
mu_vh = R*T_vh/p_vh
# плотность
ro_vh = 1/mu_vh
# скорость потока
c_vh = math.sqrt(2*k/(k-1)*R*(T_input-T_vh))
# местная скорость звука
a_vh = math.sqrt(k*R*T_vh)
# площадь входного поперечного сечения
F_vh = G/ro_vh/c_vh
# диаметр входного сечения сопла
d_vh = round(math.sqrt(4/3.14*F_vh)*1e3)

# расчет критического сечения
betta_kr = (2/(k+1))**(k/(k-1))
# давление
p_kr = betta_kr*P_input
# температура
T_kr = T_input*betta_kr**((k-1)/k)
# удельный объем
mu_kr = R*T_kr/p_kr
# плотность
ro_kr = 1/mu_kr
# скорость потока
c_kr = math.sqrt(2*k/(k-1)*R*(T_input-T_kr))
# местная скорость звука
a_kr = math.sqrt(k*R*T_kr)
# площадь критического поперечного сечения
F_kr = G/ro_kr/c_kr
# диаметр критического сечения сопла
d_kr = round(math.sqrt(4/3.14*F_kr)*1e3)

# расчет выходного сечения
betta_out = P_output/P_input
# давление
p_out = betta_out*P_input
# температура
T_out = T_input*betta_out**((k-1)/k)
# удельный объем
mu_out = R*T_out/p_out
# плотность
ro_out = 1/mu_out
# скорость потока
c_out = math.sqrt(2*k/(k-1)*R*(T_input-T_out))
# местная скорость звука
a_out = math.sqrt(k*R*T_out)
# площадь выходного поперечного сечения
F_out = G/ro_out/c_out
# диаметр выходного сечения сопла
d_out = round(math.sqrt(4/3.14*F_out)*1e3)

# расчетная длина сопла до критического сечения и после
l_left_ = (d_vh-d_kr)/(2*math.tan(alpha_/2*math.pi/180))
l_right_ = (d_out-d_kr)/(2*math.tan(betta_/2*math.pi/180))

d_inlet_ = d_vh
d_kr_ = d_kr
d_outlet_ = d_out

r_ = d_kr
OS_ = r_+d_kr_/2
l1_ = (l_left_+l_right_)*1.6
l2_ = d_outlet_/5
h_ = d_outlet_*4

arc_left = math.pi * alpha_ * r_ / 180
arc_right = math.pi * betta_* r_ / 180

# atmosphere height above nozzle
k_height = 177*6/885
# atmosphere width
k_width = (1189.09+152.41+2146.4)/2146.4
# left top atmosphere
k_left_top = (2146.4+30.482)/30.482
# nozzle width
k_nozzle = (1189.09+152.41)/1189.09
# arc left
k_arc_left = (14*3.14*100)/180/628
# arc right
k_arc_right = (28*3.14*100)/180/628

NbSg1 = 15
NbSg2 = 1
NbSg3 = round(l_left_*k_nozzle/13.4)
NbSg4 = round(arc_left * k_arc_left*2)
NbSg5 = round(arc_right * k_arc_right)
NbSg6 = round(l_right_*k_nozzle/5.7)
NbSg7 = round(l1_*k_width/7)
NbSg8 = round(l2_*k_left_top/360)
NbSg9 = round(h_*k_height/15)

###
### SHAPER component
###

from SketchAPI import *

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

model.do()


### Create Part
Part_2 = model.addPart(partSet)
Part_2_doc = Part_2.document()
model.addParameter(Part_2_doc, "d_inlet", 'd_inlet_')
model.addParameter(Part_2_doc, "d_kr", 'd_kr_')
model.addParameter(Part_2_doc, "d_outlet", 'd_outlet_')
model.addParameter(Part_2_doc, "alpha", 'alpha_')
model.addParameter(Part_2_doc, "betta", 'betta_')
model.addParameter(Part_2_doc, "r", 'r_')
model.addParameter(Part_2_doc, "OS", 'OS_')
model.addParameter(Part_2_doc, "l1", 'l1_')
model.addParameter(Part_2_doc, "l2", 'l2_')
model.addParameter(Part_2_doc, "h", 'h_')
model.addParameter(Part_2_doc, "l_left", 'l_left_')
model.addParameter(Part_2_doc, "l_right", 'l_right_')

### Create Sketch
Sketch_1 = model.addSketch(Part_2_doc, model.defaultPlane("XOY"))

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("EDGE", "PartSet/OX"), False)
SketchLine_1 = SketchProjection_1.createdFeature()
SketchLine_1.setName("SketchLine_8")
SketchLine_1.result().setName("SketchLine_8")

### Create SketchProjection
SketchProjection_2 = Sketch_1.addProjection(model.selection("EDGE", "PartSet/OY"), False)
SketchLine_2 = SketchProjection_2.createdFeature()
SketchLine_2.setName("SketchLine_11")
SketchLine_2.result().setName("SketchLine_11")

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(0, 0, 0, 150)
SketchLine_3.setName("SketchLine_12")
SketchLine_3.result().setName("SketchLine_12")
SketchLine_3.setAuxiliary(True)
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_1).startPoint(), SketchLine_3.startPoint())
Sketch_1.setVertical(SketchLine_3.result())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(-1189.07, 0, -12.18693434051475, 0)
SketchLine_4.setName("SketchLine_14")
SketchLine_4.result().setName("SketchLine_14")
Sketch_1.setHorizontal(SketchLine_4.result())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(-12.18693434051475, 0, -12.18693434051475, 50.7453848358678)
SketchLine_5.setName("SketchLine_16")
SketchLine_5.result().setName("SketchLine_16")
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_5.startPoint())
Sketch_1.setVertical(SketchLine_5.result())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(-1189.07, 195.248455286882, -12.18693434051475, 50.7453848358678)
SketchLine_6.setName("SketchLine_17")
SketchLine_6.result().setName("SketchLine_17")
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.endPoint())

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(24.19218955996677, 0, 152.41, 0)
SketchLine_7.setName("SketchLine_28")
SketchLine_7.result().setName("SketchLine_28")
Sketch_1.setHorizontal(SketchLine_7.result())

### Create SketchLine
SketchLine_8 = Sketch_1.addLine(24.19218955996677, 0, 24.19218955996677, 52.97042737240036)
SketchLine_8.setName("SketchLine_29")
SketchLine_8.result().setName("SketchLine_29")
Sketch_1.setCoincident(SketchLine_7.startPoint(), SketchLine_8.startPoint())

### Create SketchLine
SketchLine_9 = Sketch_1.addLine(152.41, 0, 152.41, 84.93871797833935)
SketchLine_9.setName("SketchLine_30")
SketchLine_9.result().setName("SketchLine_30")
Sketch_1.setCoincident(SketchLine_7.endPoint(), SketchLine_9.startPoint())
Sketch_1.setVertical(SketchLine_9.result())

### Create SketchLine
SketchLine_10 = Sketch_1.addLine(24.19218955996677, 52.97042737240036, 152.41, 84.93871797833935)
SketchLine_10.setName("SketchLine_31")
SketchLine_10.result().setName("SketchLine_31")
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_10.startPoint())
Sketch_1.setCoincident(SketchLine_9.endPoint(), SketchLine_10.endPoint())
Sketch_1.setVertical(SketchLine_8.result())

### Create SketchLine
SketchLine_11 = Sketch_1.addLine(0, 0, 24.19218955996677, 0)
SketchLine_11.setName("SketchLine_32")
SketchLine_11.result().setName("SketchLine_32")
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_1).startPoint(), SketchLine_11.startPoint())
Sketch_1.setCoincident(SketchLine_7.startPoint(), SketchLine_11.endPoint())
Sketch_1.setHorizontal(SketchLine_11.result())

### Create SketchLine
SketchLine_12 = Sketch_1.addLine(-12.18693434051475, 0, 0, 0)
SketchLine_12.setName("SketchLine_33")
SketchLine_12.result().setName("SketchLine_33")
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_12.startPoint())
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_1).startPoint(), SketchLine_12.endPoint())
Sketch_1.setHorizontal(SketchLine_12.result())

### Create SketchLine
SketchLine_13 = Sketch_1.addLine(0, 0, 0, 50.00000000000001)
SketchLine_13.setName("SketchLine_34")
SketchLine_13.result().setName("SketchLine_34")
Sketch_1.setCoincident(SketchAPI_Line(SketchLine_1).startPoint(), SketchLine_13.startPoint())
Sketch_1.setVertical(SketchLine_13.result())
Sketch_1.setVerticalDistance(SketchLine_12.endPoint(), SketchLine_3.endPoint(), "OS")

### Create SketchConstraintAngle
Sketch_1.setAngle(SketchLine_10.result(), SketchLine_7.result(), 14, type = "Direct")

### Create SketchLine
SketchLine_14 = Sketch_1.addLine(-1189.07, 0, -1189.07, 195.248455286882)
SketchLine_14.setName("SketchLine_35")
SketchLine_14.result().setName("SketchLine_35")
Sketch_1.setCoincident(SketchLine_4.startPoint(), SketchLine_14.startPoint())
Sketch_1.setCoincident(SketchLine_6.startPoint(), SketchLine_14.endPoint())
Sketch_1.setVertical(SketchLine_14.result())

### Create SketchConstraintAngle
Sketch_1.setAngle(SketchLine_6.result(), SketchLine_4.result(), 7, type = "Direct")

### Create SketchArc
SketchArc_1 = Sketch_1.addArc(0, 150, -12.18693434051475, 50.7453848358678, 0, 50.00000000000001, False)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchArc_1.center())
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchArc_1.startPoint())
Sketch_1.setCoincident(SketchLine_13.result(), SketchArc_1.endPoint())
Sketch_1.setCoincident(SketchLine_13.endPoint(), SketchArc_1.endPoint())

### Create SketchArc
SketchArc_2 = Sketch_1.addArc(0, 150, 0, 50.00000000000001, 24.19218955996677, 52.97042737240036, False)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchArc_2.center())
Sketch_1.setCoincident(SketchLine_13.endPoint(), SketchArc_2.startPoint())
Sketch_1.setCoincident(SketchLine_8.result(), SketchArc_2.endPoint())
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchArc_2.endPoint())
Sketch_1.setTangent(SketchLine_6.result(), SketchArc_1.results()[1])
Sketch_1.setTangent(SketchArc_2.results()[1], SketchLine_10.result())
Sketch_1.setVerticalDistance(SketchLine_13.endPoint(), SketchArc_2.center(), "r")
Sketch_1.setHorizontalDistance(SketchLine_14.startPoint(), SketchLine_12.endPoint(), "l_left")
Sketch_1.setHorizontalDistance(SketchLine_12.endPoint(), SketchLine_7.endPoint(), "l_right")
model.do()
Sketch_1.changeFacesOrder([[SketchLine_4.result(), SketchLine_5.result(), SketchLine_6.result(), SketchLine_14.result()],
                           [SketchLine_7.result(), SketchLine_9.result(), SketchLine_10.result(), SketchLine_8.result()],
                           [SketchLine_12.result(), SketchLine_13.result(), SketchArc_1.results()[1], SketchLine_5.result()],
                           [SketchLine_8.result(), SketchArc_2.results()[1], SketchLine_13.result(), SketchLine_11.result()]
                          ])
model.do()

### Create Sketch
Sketch_2 = model.addSketch(Part_2_doc, model.defaultPlane("XOY"))

### Create SketchLine
SketchLine_15 = Sketch_2.addLine(117.21, 84.93871797833935, 152.41, 84.93871797833935)
SketchLine_15.setName("SketchLine_15")
SketchLine_15.result().setName("SketchLine_15")

### Create SketchProjection
SketchProjection_3 = Sketch_2.addProjection(model.selection("VERTEX", "Sketch_1/SketchLine_30_EndVertex"), False)
SketchPoint_1 = SketchProjection_3.createdFeature()
Sketch_2.setCoincident(SketchLine_15.endPoint(), SketchPoint_1.result())

### Create SketchLine
SketchLine_16 = Sketch_2.addLine(152.41, 84.93871797833935, 2298.78, 84.93871797833935)
SketchLine_16.setName("SketchLine_18")
SketchLine_16.result().setName("SketchLine_18")
Sketch_2.setCoincident(SketchLine_15.endPoint(), SketchLine_16.startPoint())
Sketch_2.setHorizontal(SketchLine_16.result())

### Create SketchLine
SketchLine_17 = Sketch_2.addLine(152.41, 0, 2298.78, 0)
SketchLine_17.setName("SketchLine_19")
SketchLine_17.result().setName("SketchLine_19")

### Create SketchProjection
SketchProjection_4 = Sketch_2.addProjection(model.selection("VERTEX", "Sketch_1/SketchLine_30_StartVertex"), False)
SketchPoint_2 = SketchProjection_4.createdFeature()
Sketch_2.setCoincident(SketchLine_17.startPoint(), SketchPoint_2.result())
Sketch_2.setHorizontal(SketchLine_17.result())

### Create SketchLine
SketchLine_18 = Sketch_2.addLine(152.41, 788.9387179783394, 2298.78, 788.9387179783394)
SketchLine_18.setName("SketchLine_20")
SketchLine_18.result().setName("SketchLine_20")
Sketch_2.setHorizontal(SketchLine_18.result())

### Create SketchLine
SketchLine_19 = Sketch_2.addLine(117.21, 788.9387179783394, 152.41, 788.9387179783394)
SketchLine_19.setName("SketchLine_21")
SketchLine_19.result().setName("SketchLine_21")
Sketch_2.setCoincident(SketchLine_18.startPoint(), SketchLine_19.endPoint())
Sketch_2.setHorizontal(SketchLine_19.result())

### Create SketchLine
SketchLine_20 = Sketch_2.addLine(117.21, 84.93871797833935, 117.21, 788.9387179783394)
SketchLine_20.setName("SketchLine_22")
SketchLine_20.result().setName("SketchLine_22")
Sketch_2.setCoincident(SketchLine_15.startPoint(), SketchLine_20.startPoint())
Sketch_2.setCoincident(SketchLine_19.startPoint(), SketchLine_20.endPoint())
Sketch_2.setVertical(SketchLine_20.result())

### Create SketchLine
SketchLine_21 = Sketch_2.addLine(152.41, 84.93871797833935, 152.41, 788.9387179783394)
SketchLine_21.setName("SketchLine_23")
SketchLine_21.result().setName("SketchLine_23")
Sketch_2.setCoincident(SketchLine_15.endPoint(), SketchLine_21.startPoint())
Sketch_2.setCoincident(SketchLine_18.startPoint(), SketchLine_21.endPoint())
Sketch_2.setVertical(SketchLine_21.result())

### Create SketchLine
SketchLine_22 = Sketch_2.addLine(2298.78, 84.93871797833935, 2298.78, 788.9387179783394)
SketchLine_22.setName("SketchLine_24")
SketchLine_22.result().setName("SketchLine_24")
Sketch_2.setCoincident(SketchLine_16.endPoint(), SketchLine_22.startPoint())
Sketch_2.setCoincident(SketchLine_18.endPoint(), SketchLine_22.endPoint())

### Create SketchLine
SketchLine_23 = Sketch_2.addLine(2298.78, 0, 2298.78, 84.93871797833935)
SketchLine_23.setName("SketchLine_25")
SketchLine_23.result().setName("SketchLine_25")
Sketch_2.setCoincident(SketchLine_17.endPoint(), SketchLine_23.startPoint())
Sketch_2.setCoincident(SketchLine_16.endPoint(), SketchLine_23.endPoint())

### Create SketchLine
SketchLine_24 = Sketch_2.addLine(152.41, 0, 152.41, 84.93871797833935)
SketchLine_24.setName("SketchLine_26")
SketchLine_24.result().setName("SketchLine_26")
Sketch_2.setCoincident(SketchLine_17.startPoint(), SketchLine_24.startPoint())
Sketch_2.setCoincident(SketchLine_15.endPoint(), SketchLine_24.endPoint())
Sketch_2.setHorizontal(SketchLine_15.result())
Sketch_2.setVertical(SketchLine_22.result())
Sketch_2.setVertical(SketchLine_23.result())
Sketch_2.setLength(SketchLine_20.result(), "h")
Sketch_2.setHorizontalDistance(SketchLine_20.endPoint(), SketchLine_21.endPoint(), "l2")
Sketch_2.setHorizontalDistance(SketchLine_24.endPoint(), SketchLine_16.endPoint(), "l1")
model.do()

### Create Face
Face_1 = model.addFace(Part_2_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_14f-SketchLine_16f-SketchLine_17r-SketchLine_35r")])

### Create Face
Face_2 = model.addFace(Part_2_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_33f-SketchLine_34f-SketchArc_1_2r-SketchLine_16r")])

### Create Face
Face_3 = model.addFace(Part_2_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_29f-SketchArc_2_2r-SketchLine_34r-SketchLine_32f")])

### Create Face
Face_4 = model.addFace(Part_2_doc, [model.selection("FACE", "Sketch_1/Face-SketchLine_28f-SketchLine_30f-SketchLine_31r-SketchLine_29r")])

### Create Face
Face_5 = model.addFace(Part_2_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_26r-SketchLine_19f-SketchLine_25f-SketchLine_18r")])

### Create Face
Face_6 = model.addFace(Part_2_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_18f-SketchLine_24f-SketchLine_20r-SketchLine_23r")])

### Create Face
Face_7 = model.addFace(Part_2_doc, [model.selection("FACE", "Sketch_2/Face-SketchLine_15r-SketchLine_23f-SketchLine_21r-SketchLine_22r")])

### Create Shell
Shell_1_objects = [model.selection("FACE", "Sketch_1/Face-SketchLine_14f-SketchLine_16f-SketchLine_17r-SketchLine_35r"),
                   model.selection("FACE", "Sketch_1/Face-SketchLine_33f-SketchLine_34f-SketchArc_1_2r-SketchLine_16r"),
                   model.selection("FACE", "Sketch_1/Face-SketchLine_29f-SketchArc_2_2r-SketchLine_34r-SketchLine_32f"),
                   model.selection("FACE", "Sketch_1/Face-SketchLine_28f-SketchLine_30f-SketchLine_31r-SketchLine_29r"),
                   model.selection("FACE", "Sketch_2/Face-SketchLine_26r-SketchLine_19f-SketchLine_25f-SketchLine_18r"),
                   model.selection("FACE", "Sketch_2/Face-SketchLine_18f-SketchLine_24f-SketchLine_20r-SketchLine_23r"),
                   model.selection("FACE", "Sketch_2/Face-SketchLine_15r-SketchLine_23f-SketchLine_21r-SketchLine_22r")]
Shell_1 = model.addShell(Part_2_doc, Shell_1_objects)

### Create Revolution
Revolution_1 = model.addRevolution(Part_2_doc, [model.selection("SHELL", "Shell_1_1")], model.selection("EDGE", "PartSet/OX"), 2.5, 2.5, "Faces")

### Create Group
Group_1_objects = [model.selection("EDGE", "[Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_17][Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_35]"),
                   model.selection("EDGE", "[Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_16][Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_17]"),
                   model.selection("EDGE", "[Revolution_1_1_3/Generated_Face&Sketch_1/SketchArc_2_2][Revolution_1_1_3/Generated_Face&Sketch_1/SketchLine_34]"),
                   model.selection("EDGE", "[Revolution_1_1_3/Generated_Face&Sketch_1/SketchLine_29][Revolution_1_1_3/Generated_Face&Sketch_1/SketchArc_2_2]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_15][Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_22]"),
                   model.selection("EDGE", "[Revolution_1_1_4/Generated_Face&Sketch_2/SketchLine_26&Sketch_1/SketchLine_30][Revolution_1_1_4/Generated_Face&Sketch_1/SketchLine_31]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_21][Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_22]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_23][Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_21]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_24][Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_20]"),
                   model.selection("EDGE", "[Revolution_1_1_5/Generated_Face&Sketch_2/SketchLine_25][Revolution_1_1_5/Generated_Face&Sketch_2/SketchLine_18]")]
Group_1 = model.addGroup(Part_2_doc, "Edges", Group_1_objects)

### Create Group
Group_2_objects = [model.selection("FACE", "Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_35"),
                   model.selection("FACE", "Revolution_1_1_2/Generated_Face&Sketch_1/SketchLine_16"),
                   model.selection("FACE", "Revolution_1_1_3/Generated_Face&Sketch_1/SketchLine_34"),
                   model.selection("FACE", "Revolution_1_1_4/Generated_Face&Sketch_1/SketchLine_29"),
                   model.selection("FACE", "Revolution_1_1_5/Generated_Face&Sketch_2/SketchLine_26&Sketch_1/SketchLine_30"),
                   model.selection("FACE", "Revolution_1_1_5/Generated_Face&Sketch_2/SketchLine_25")]
Group_2 = model.addGroup(Part_2_doc, "Faces", Group_2_objects)

### Create Group
Group_3_objects = [model.selection("EDGE", "[Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_17][Revolution_1_1_1/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_17][Revolution_1_1_1/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_1/From_Face][Revolution_1_1_1/To_Face]")]
Group_3 = model.addGroup(Part_2_doc, "Edges", Group_3_objects)

### Create Group
Group_4_objects = [model.selection("EDGE", "[Revolution_1_1_2/Generated_Face&Sketch_1/SketchArc_1_2][Revolution_1_1_2/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_2/Generated_Face&Sketch_1/SketchArc_1_2][Revolution_1_1_2/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_2/From_Face][Revolution_1_1_2/To_Face]")]
Group_4 = model.addGroup(Part_2_doc, "Edges", Group_4_objects)

### Create Group
Group_5_objects = [model.selection("EDGE", "[Revolution_1_1_3/Generated_Face&Sketch_1/SketchArc_2_2][Revolution_1_1_3/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_3/Generated_Face&Sketch_1/SketchArc_2_2][Revolution_1_1_3/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_3/From_Face][Revolution_1_1_3/To_Face]")]
Group_5 = model.addGroup(Part_2_doc, "Edges", Group_5_objects)

### Create Group
Group_6_objects = [model.selection("EDGE", "[Revolution_1_1_4/Generated_Face&Sketch_1/SketchLine_31][Revolution_1_1_4/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_4/Generated_Face&Sketch_1/SketchLine_31][Revolution_1_1_4/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_4/From_Face][Revolution_1_1_4/To_Face]")]
Group_6 = model.addGroup(Part_2_doc, "Edges", Group_6_objects)

### Create Group
Group_7_objects = [model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_20][Revolution_1_1_6/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_20][Revolution_1_1_6/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_18][Revolution_1_1_6/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_18][Revolution_1_1_6/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_5/From_Face][Revolution_1_1_5/To_Face]")]
Group_7 = model.addGroup(Part_2_doc, "Edges", Group_7_objects)

### Create Group
Group_8_objects = [model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_21][Revolution_1_1_7/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_21][Revolution_1_1_7/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_15][Revolution_1_1_7/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_15][Revolution_1_1_7/To_Face]")]
Group_8 = model.addGroup(Part_2_doc, "Edges", Group_8_objects)

### Create Group
Group_9_objects = [model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_22][Revolution_1_1_7/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_22][Revolution_1_1_7/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_23][Revolution_1_1_7/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_24][Revolution_1_1_6/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_23][Revolution_1_1_7/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_24][Revolution_1_1_6/From_Face]")]
Group_9 = model.addGroup(Part_2_doc, "Edges", Group_9_objects)

### Create Group
Group_10_objects = [model.selection("FACE", "Revolution_1_1_1/To_Face"),
                    model.selection("FACE", "Revolution_1_1_2/To_Face"),
                    model.selection("FACE", "Revolution_1_1_3/To_Face"),
                    model.selection("FACE", "Revolution_1_1_4/To_Face"),
                    model.selection("FACE", "Revolution_1_1_5/To_Face"),
                    model.selection("FACE", "Revolution_1_1_6/To_Face"),
                    model.selection("FACE", "Revolution_1_1_7/To_Face")]
Group_10 = model.addGroup(Part_2_doc, "Faces", Group_10_objects)
Group_10.setName("front")
Group_10.result().setName("front")

### Create Group
Group_11_objects = [model.selection("FACE", "Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_17"),
                    model.selection("FACE", "Revolution_1_1_2/Generated_Face&Sketch_1/SketchArc_1_2"),
                    model.selection("FACE", "Revolution_1_1_3/Generated_Face&Sketch_1/SketchArc_2_2"),
                    model.selection("FACE", "Revolution_1_1_4/Generated_Face&Sketch_1/SketchLine_31"),
                    model.selection("FACE", "Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_15")]
Group_11 = model.addGroup(Part_2_doc, "Faces", Group_11_objects)
Group_11.setName("wall")
Group_11.result().setName("wall")

### Create Group
Group_12 = model.addGroup(Part_2_doc, "Faces", [model.selection("FACE", "Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_20"), model.selection("FACE", "Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_21")])
Group_12.setName("outletTop")
Group_12.result().setName("outletTop")

### Create Group
Group_13 = model.addGroup(Part_2_doc, "Faces", [model.selection("FACE", "Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_22")])
Group_13.setName("inlet")
Group_13.result().setName("inlet")

### Create Group
Group_14 = model.addGroup(Part_2_doc, "Faces", [model.selection("FACE", "Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_35")])
Group_14.setName("outletLeft")
Group_14.result().setName("outletLeft")

### Create Group
Group_15 = model.addGroup(Part_2_doc, "Faces", [model.selection("FACE", "Revolution_1_1_5/Generated_Face&Sketch_2/SketchLine_25"), model.selection("FACE", "Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_24")])
Group_15.setName("outletRight")
Group_15.result().setName("outletRight")

### Create Group
Group_16_objects = [model.selection("FACE", "Revolution_1_1_1/From_Face"),
                    model.selection("FACE", "Revolution_1_1_2/From_Face"),
                    model.selection("FACE", "Revolution_1_1_3/From_Face"),
                    model.selection("FACE", "Revolution_1_1_4/From_Face"),
                    model.selection("FACE", "Revolution_1_1_5/From_Face"),
                    model.selection("FACE", "Revolution_1_1_6/From_Face"),
                    model.selection("FACE", "Revolution_1_1_7/From_Face")]
Group_16 = model.addGroup(Part_2_doc, "Faces", Group_16_objects)
Group_16.setName("back")
Group_16.result().setName("back")

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Face_1_1, = SHAPERSTUDY.shape(model.featureStringId(Face_1))
Face_2_1, = SHAPERSTUDY.shape(model.featureStringId(Face_2))
Face_3_1, = SHAPERSTUDY.shape(model.featureStringId(Face_3))
Face_4_1, = SHAPERSTUDY.shape(model.featureStringId(Face_4))
Face_5_1, = SHAPERSTUDY.shape(model.featureStringId(Face_5))
Face_6_1, = SHAPERSTUDY.shape(model.featureStringId(Face_6))
Face_7_1, = SHAPERSTUDY.shape(model.featureStringId(Face_7))
Revolution_1_1, Group_1_1, Group_2_1, Group_3_1, Group_4_1, Group_5_1, Group_6_1, Group_7_1, Group_8_1, Group_9_1, front, wall, outletTop, inlet, outletLeft, outletRight, back, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1))
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(Revolution_1_1,'Mesh_1')
Prism_3D = Mesh_1.Prism()
front_1 = Mesh_1.GroupOnGeom(front,'front',SMESH.FACE)
wall_1 = Mesh_1.GroupOnGeom(wall,'wall',SMESH.FACE)
outletTop_1 = Mesh_1.GroupOnGeom(outletTop,'outletTop',SMESH.FACE)
inlet_1 = Mesh_1.GroupOnGeom(inlet,'inlet',SMESH.FACE)
outletLeft_1 = Mesh_1.GroupOnGeom(outletLeft,'outletLeft',SMESH.FACE)
outletRight_1 = Mesh_1.GroupOnGeom(outletRight,'outletRight',SMESH.FACE)
back_1 = Mesh_1.GroupOnGeom(back,'back',SMESH.FACE)
Regular_1D = Mesh_1.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(NbSg1)
Regular_1D_1 = Mesh_1.Segment(geom=Group_1_1)
Sub_mesh_1 = Regular_1D_1.GetSubMesh()
Number_of_Segments_2 = Regular_1D_1.NumberOfSegments(NbSg2)
Regular_1D_2 = Mesh_1.Segment(geom=Group_2_1)
Sub_mesh_2 = Regular_1D_2.GetSubMesh()
status = Mesh_1.AddHypothesis(Number_of_Segments_1,Group_2_1)
RadialQuadrangle_1D2D = Mesh_1.Quadrangle(algo=smeshBuilder.RADIAL_QUAD,geom=Group_2_1)
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_1, Sub_mesh_2 ] ])
[ smeshObj_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6, smeshObj_7, smeshObj_8, smeshObj_9, front_1, wall_1, outletTop_1, inlet_1, outletLeft_1, outletRight_1, back_1 ] = Mesh_1.GetGroups()
Regular_1D_3 = Mesh_1.Segment(geom=Group_3_1)
Number_of_Segments_3 = Regular_1D_3.NumberOfSegments(NbSg3,None,[])
Number_of_Segments_3.SetConversionMode( 0 )
Number_of_Segments_3.SetExpressionFunction( '0.5*t' )
[ smeshObj_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6, smeshObj_7, smeshObj_8, smeshObj_9, front_1, wall_1, outletTop_1, inlet_1, outletLeft_1, outletRight_1, back_1 ] = Mesh_1.GetGroups()
Regular_1D_4 = Mesh_1.Segment(geom=Group_4_1)
Number_of_Segments_4 = Regular_1D_4.NumberOfSegments(NbSg4)
[ smeshObj_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6, smeshObj_7, smeshObj_8, smeshObj_9, front_1, wall_1, outletTop_1, inlet_1, outletLeft_1, outletRight_1, back_1 ] = Mesh_1.GetGroups()
Regular_1D_5 = Mesh_1.Segment(geom=Group_5_1)
Number_of_Segments_5 = Regular_1D_5.NumberOfSegments(NbSg5)
[ smeshObj_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6, smeshObj_7, smeshObj_8, smeshObj_9, front_1, wall_1, outletTop_1, inlet_1, outletLeft_1, outletRight_1, back_1 ] = Mesh_1.GetGroups()
Regular_1D_6 = Mesh_1.Segment(geom=Group_6_1)
Number_of_Segments_6 = Regular_1D_6.NumberOfSegments(NbSg6)
[ smeshObj_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6, smeshObj_7, smeshObj_8, smeshObj_9, front_1, wall_1, outletTop_1, inlet_1, outletLeft_1, outletRight_1, back_1 ] = Mesh_1.GetGroups()
Regular_1D_7 = Mesh_1.Segment(geom=Group_7_1)
Number_of_Segments_7 = Regular_1D_7.NumberOfSegments(NbSg7)
[ smeshObj_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6, smeshObj_7, smeshObj_8, smeshObj_9, front_1, wall_1, outletTop_1, inlet_1, outletLeft_1, outletRight_1, back_1 ] = Mesh_1.GetGroups()
Regular_1D_8 = Mesh_1.Segment(geom=Group_8_1)
Number_of_Segments_8 = Regular_1D_8.NumberOfSegments(NbSg8)
[ smeshObj_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6, smeshObj_7, smeshObj_8, smeshObj_9, front_1, wall_1, outletTop_1, inlet_1, outletLeft_1, outletRight_1, back_1 ] = Mesh_1.GetGroups()
Regular_1D_9 = Mesh_1.Segment(geom=Group_9_1)
Number_of_Segments_9 = Regular_1D_9.NumberOfSegments(NbSg9,None,[])
Number_of_Segments_9.SetConversionMode( 0 )
Number_of_Segments_9.SetExpressionFunction( '-t*t' )
isDone = Mesh_1.Compute()
Mesh_1.CheckCompute()
[ smeshObj_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5, smeshObj_6, smeshObj_7, smeshObj_8, smeshObj_9, front_1, wall_1, outletTop_1, inlet_1, outletLeft_1, outletRight_1, back_1 ] = Mesh_1.GetGroups()
try:
  Mesh_1.ExportUNV( r'/home/vd/OpenFOAM/vd-12/run/nozzle_1/geometry/Mesh.unv', 0 )
  pass
except:
  print('ExportUNV() failed. Invalid file name?')
Sub_mesh_3 = Regular_1D_3.GetSubMesh()
Sub_mesh_4 = Regular_1D_4.GetSubMesh()
Sub_mesh_5 = Regular_1D_5.GetSubMesh()
Sub_mesh_6 = Regular_1D_6.GetSubMesh()
Sub_mesh_7 = Regular_1D_7.GetSubMesh()
Sub_mesh_8 = Regular_1D_8.GetSubMesh()
Sub_mesh_9 = Regular_1D_9.GetSubMesh()

## some objects were removed
aStudyBuilder = salome.myStudy.NewBuilder()
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_3))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_5))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_1))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_7))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_8))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_2))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_9))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_4))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_6))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)

## Set names of Mesh objects
smesh.SetName(wall_1, 'wall')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Sub_mesh_9, 'Sub-mesh_9')
smesh.SetName(outletTop_1, 'outletTop')
smesh.SetName(Number_of_Segments_5, 'Number of Segments_5')
smesh.SetName(Number_of_Segments_3, 'Number of Segments_3')
smesh.SetName(Sub_mesh_8, 'Sub-mesh_8')
smesh.SetName(front_1, 'front')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Prism_3D.GetAlgorithm(), 'Prism_3D')
smesh.SetName(Sub_mesh_6, 'Sub-mesh_6')
smesh.SetName(Number_of_Segments_4, 'Number of Segments_4')
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')
smesh.SetName(Number_of_Segments_6, 'Number of Segments_6')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(Number_of_Segments_7, 'Number of Segments_7')
smesh.SetName(outletLeft_1, 'outletLeft')
smesh.SetName(outletRight_1, 'outletRight')
smesh.SetName(back_1, 'back')
smesh.SetName(Number_of_Segments_9, 'Number of Segments_9')
smesh.SetName(Sub_mesh_5, 'Sub-mesh_5')
smesh.SetName(Sub_mesh_7, 'Sub-mesh_7')
smesh.SetName(Number_of_Segments_8, 'Number of Segments_8')
smesh.SetName(Sub_mesh_3, 'Sub-mesh_3')
smesh.SetName(RadialQuadrangle_1D2D.GetAlgorithm(), 'RadialQuadrangle_1D2D')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Sub_mesh_4, 'Sub-mesh_4')
smesh.SetName(inlet_1, 'inlet')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
