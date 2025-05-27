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
sys.path.insert(0, r'/home/mark/OpenFOAM/mark-12/run/nozzle_1/geometry')


# входные параметры
P_input = 200000
T_input = 1000
P_output = 8000
G = 2
alpha_ = 14
betta_ = 22
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

### Create SketchLine
SketchLine_1 = Sketch_1.addLine(-1195.190840489832, 0, -12.18693434055722, 0)
Sketch_1.setHorizontal(SketchLine_1.result())

### Create SketchLine
SketchLine_2 = Sketch_1.addLine(-12.18693434055722, 0, 0, 0)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_2.startPoint())

### Create SketchProjection
SketchProjection_1 = Sketch_1.addProjection(model.selection("VERTEX", "PartSet/Origin"), False)
SketchPoint_1 = SketchProjection_1.createdFeature()
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchPoint_1.result())

### Create SketchLine
SketchLine_3 = Sketch_1.addLine(0, 0, 24.19218956861992, 0)
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_3.startPoint())
Sketch_1.setHorizontal(SketchLine_3.result())

### Create SketchLine
SketchLine_4 = Sketch_1.addLine(24.19218956861992, 0, 164.6881315615066, 0)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_4.startPoint())
Sketch_1.setHorizontal(SketchLine_4.result())

### Create SketchLine
SketchLine_5 = Sketch_1.addLine(-1195.190840489832, 0, -1195.190840489832, 196)
Sketch_1.setCoincident(SketchLine_1.startPoint(), SketchLine_5.startPoint())
Sketch_1.setVertical(SketchLine_5.result())

### Create SketchLine
SketchLine_6 = Sketch_1.addLine(-1195.190840489832, 196, -12.18693434055722, 50.74538483586102)
Sketch_1.setCoincident(SketchLine_5.endPoint(), SketchLine_6.startPoint())

### Create SketchLine
SketchLine_7 = Sketch_1.addLine(-12.18693434055722, 0, -12.18693434055722, 50.74538483586102)
Sketch_1.setCoincident(SketchLine_1.endPoint(), SketchLine_7.startPoint())
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchLine_7.endPoint())
Sketch_1.setVertical(SketchLine_7.result())

### Create SketchLine
SketchLine_8 = Sketch_1.addLine(24.19218956861992, 0, 24.19218956861992, 52.97042737453264)
Sketch_1.setCoincident(SketchLine_3.endPoint(), SketchLine_8.startPoint())
Sketch_1.setVertical(SketchLine_8.result())

### Create SketchLine
SketchLine_9 = Sketch_1.addLine(24.19218956861992, 52.97042737453264, 164.6881315615066, 88)
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchLine_9.startPoint())

### Create SketchLine
SketchLine_10 = Sketch_1.addLine(164.6881315615066, 0, 164.6881315615066, 88)
Sketch_1.setCoincident(SketchLine_4.endPoint(), SketchLine_10.startPoint())
Sketch_1.setCoincident(SketchLine_9.endPoint(), SketchLine_10.endPoint())

### Create SketchLine
SketchLine_11 = Sketch_1.addLine(0, 0, 0, 150)
SketchLine_11.setAuxiliary(True)
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_11.startPoint())
Sketch_1.setVertical(SketchLine_11.result())

### Create SketchLine
SketchLine_12 = Sketch_1.addLine(0, 0, 0, 50)
Sketch_1.setCoincident(SketchLine_2.endPoint(), SketchLine_12.startPoint())
Sketch_1.setVertical(SketchLine_12.result())
Sketch_1.setHorizontal(SketchLine_2.result())
Sketch_1.setVertical(SketchLine_10.result())
Sketch_1.setLength(SketchLine_11.result(), "OS")

### Create SketchArc
SketchArc_1 = Sketch_1.addArc(0, 150, -12.18693434055722, 50.74538483586102, 0, 50, False)
Sketch_1.setCoincident(SketchLine_11.endPoint(), SketchArc_1.center())
Sketch_1.setCoincident(SketchLine_6.endPoint(), SketchArc_1.startPoint())
Sketch_1.setCoincident(SketchLine_12.result(), SketchArc_1.endPoint())
Sketch_1.setCoincident(SketchArc_1.endPoint(), SketchLine_12.endPoint())

### Create SketchArc
SketchArc_2 = Sketch_1.addArc(0, 150, 0, 50, 24.19218956861992, 52.97042737453264, False)
Sketch_1.setCoincident(SketchLine_11.endPoint(), SketchArc_2.center())
Sketch_1.setCoincident(SketchLine_12.endPoint(), SketchArc_2.startPoint())
Sketch_1.setCoincident(SketchLine_8.result(), SketchArc_2.endPoint())
Sketch_1.setCoincident(SketchLine_8.endPoint(), SketchArc_2.endPoint())
Sketch_1.setVerticalDistance(SketchArc_1.center(), SketchLine_12.endPoint(), "r")

### Create SketchConstraintAngle
Sketch_1.setAngle(SketchLine_6.result(), SketchLine_1.result(), "alpha/2", type = "Direct")

### Create SketchConstraintAngle
Sketch_1.setAngle(SketchLine_9.result(), SketchLine_4.result(), "betta/2", type = "Direct")
Sketch_1.setTangent(SketchLine_6.result(), SketchArc_1.results()[1])
Sketch_1.setTangent(SketchArc_2.results()[1], SketchLine_9.result())
Sketch_1.setLength(SketchLine_10.result(), "d_outlet/2")
Sketch_1.setLength(SketchLine_5.result(), "d_inlet/2")
model.do()
Sketch_1.changeFacesOrder([[SketchLine_1.result(), SketchLine_7.result(), SketchLine_6.result(), SketchLine_5.result()],
                           [SketchLine_3.result(), SketchLine_8.result(), SketchArc_2.results()[1], SketchLine_12.result()],
                           [SketchLine_2.result(), SketchLine_12.result(), SketchArc_1.results()[1], SketchLine_7.result()],
                           [SketchLine_4.result(), SketchLine_10.result(), SketchLine_9.result(), SketchLine_8.result()]
                          ])
model.do()

### Create Sketch
Sketch_2 = model.addSketch(Part_2_doc, model.defaultPlane("XOY"))

### Create SketchLine
SketchLine_13 = Sketch_2.addLine(164.6881315615066, 0, 2311.058131561506, 0)

### Create SketchProjection
SketchProjection_2 = Sketch_2.addProjection(model.selection("VERTEX", "Sketch_1/SketchLine_4_EndVertex"), False)
SketchPoint_2 = SketchProjection_2.createdFeature()
Sketch_2.setCoincident(SketchLine_13.startPoint(), SketchPoint_2.result())
Sketch_2.setHorizontal(SketchLine_13.result())

### Create SketchLine
SketchLine_14 = Sketch_2.addLine(2311.058131561506, 0, 2311.058131561506, 88)
Sketch_2.setCoincident(SketchLine_13.endPoint(), SketchLine_14.startPoint())
Sketch_2.setVertical(SketchLine_14.result())

### Create SketchLine
SketchLine_15 = Sketch_2.addLine(2311.058131561506, 88, 2311.058131561506, 792)
Sketch_2.setCoincident(SketchLine_14.endPoint(), SketchLine_15.startPoint())
Sketch_2.setVertical(SketchLine_15.result())

### Create SketchLine
SketchLine_16 = Sketch_2.addLine(164.6881315615066, 0, 164.6881315615066, 88)
Sketch_2.setCoincident(SketchLine_13.startPoint(), SketchLine_16.startPoint())

### Create SketchProjection
SketchProjection_3 = Sketch_2.addProjection(model.selection("VERTEX", "Sketch_1/SketchLine_10_EndVertex"), False)
SketchPoint_3 = SketchProjection_3.createdFeature()
Sketch_2.setCoincident(SketchLine_16.endPoint(), SketchPoint_3.result())

### Create SketchLine
SketchLine_17 = Sketch_2.addLine(164.6881315615066, 88, 164.6881315615066, 792)
Sketch_2.setCoincident(SketchLine_16.endPoint(), SketchLine_17.startPoint())
Sketch_2.setVertical(SketchLine_17.result())

### Create SketchLine
SketchLine_18 = Sketch_2.addLine(164.6881315615066, 792, 2311.058131561506, 792)
Sketch_2.setCoincident(SketchLine_17.endPoint(), SketchLine_18.startPoint())
Sketch_2.setCoincident(SketchLine_15.endPoint(), SketchLine_18.endPoint())

### Create SketchLine
SketchLine_19 = Sketch_2.addLine(129.4881315615066, 88, 164.6881315615066, 88)
Sketch_2.setHorizontal(SketchLine_19.result())

### Create SketchLine
SketchLine_20 = Sketch_2.addLine(164.6881315615066, 88, 2311.058131561506, 88)
Sketch_2.setCoincident(SketchLine_19.endPoint(), SketchLine_20.startPoint())
Sketch_2.setCoincident(SketchLine_14.endPoint(), SketchLine_20.endPoint())
Sketch_2.setHorizontal(SketchLine_20.result())
Sketch_2.setCoincident(SketchLine_16.endPoint(), SketchLine_19.endPoint())

### Create SketchLine
SketchLine_21 = Sketch_2.addLine(129.4881315615066, 88, 129.4881315615066, 792)
Sketch_2.setCoincident(SketchLine_19.startPoint(), SketchLine_21.startPoint())
Sketch_2.setVertical(SketchLine_21.result())

### Create SketchLine
SketchLine_22 = Sketch_2.addLine(129.4881315615066, 792, 164.6881315615066, 792)
Sketch_2.setCoincident(SketchLine_21.endPoint(), SketchLine_22.startPoint())
Sketch_2.setCoincident(SketchLine_17.endPoint(), SketchLine_22.endPoint())
Sketch_2.setHorizontal(SketchLine_22.result())
Sketch_2.setHorizontal(SketchLine_18.result())
Sketch_2.setLength(SketchLine_21.result(), "h")
Sketch_2.setLength(SketchLine_22.result(), "l2")
Sketch_2.setLength(SketchLine_13.result(), "l1")
model.do()

### Create Face
Face_1_objects = [model.selection("FACE", "Sketch_1/Face-SketchLine_1r-SketchLine_7f-SketchLine_6r-SketchLine_5r"),
                  model.selection("FACE", "Sketch_1/Face-SketchLine_2f-SketchLine_12f-SketchArc_1_2r-SketchLine_7r"),
                  model.selection("FACE", "Sketch_1/Face-SketchLine_3f-SketchLine_8f-SketchArc_2_2r-SketchLine_12r"),
                  model.selection("FACE", "Sketch_1/Face-SketchLine_4f-SketchLine_10f-SketchLine_9r-SketchLine_8r"),
                  model.selection("FACE", "Sketch_2/Face-SketchLine_13r-SketchLine_14f-SketchLine_20r-SketchLine_16r"),
                  model.selection("FACE", "Sketch_2/Face-SketchLine_15f-SketchLine_18r-SketchLine_17r-SketchLine_20f"),
                  model.selection("FACE", "Sketch_2/Face-SketchLine_17f-SketchLine_22r-SketchLine_21r-SketchLine_19f")]
Face_1 = model.addFace(Part_2_doc, Face_1_objects)

### Create Shell
Shell_1_objects = [model.selection("FACE", "Sketch_1/Face-SketchLine_1r-SketchLine_7f-SketchLine_6r-SketchLine_5r"),
                   model.selection("FACE", "Sketch_1/Face-SketchLine_2f-SketchLine_12f-SketchArc_1_2r-SketchLine_7r"),
                   model.selection("FACE", "Sketch_1/Face-SketchLine_3f-SketchLine_8f-SketchArc_2_2r-SketchLine_12r"),
                   model.selection("FACE", "Sketch_1/Face-SketchLine_4f-SketchLine_10f-SketchLine_9r-SketchLine_8r"),
                   model.selection("FACE", "Sketch_2/Face-SketchLine_13r-SketchLine_14f-SketchLine_20r-SketchLine_16r"),
                   model.selection("FACE", "Sketch_2/Face-SketchLine_15f-SketchLine_18r-SketchLine_17r-SketchLine_20f"),
                   model.selection("FACE", "Sketch_2/Face-SketchLine_17f-SketchLine_22r-SketchLine_21r-SketchLine_19f")]
Shell_1 = model.addShell(Part_2_doc, Shell_1_objects)

### Create Revolution
Revolution_1 = model.addRevolution(Part_2_doc, [model.selection("SHELL", "Shell_1_1")], model.selection("EDGE", "PartSet/OX"), 2.5, 2.5, "Faces")

### Create Group
Group_1_objects = [model.selection("EDGE", "[Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_6][Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_5]"),
                   model.selection("EDGE", "[Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_7][Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_6]"),
                   model.selection("EDGE", "[Revolution_1_1_3/Generated_Face&Sketch_1/SketchArc_2_2][Revolution_1_1_3/Generated_Face&Sketch_1/SketchLine_12]"),
                   model.selection("EDGE", "[Revolution_1_1_3/Generated_Face&Sketch_1/SketchLine_8][Revolution_1_1_3/Generated_Face&Sketch_1/SketchArc_2_2]"),
                   model.selection("EDGE", "[Revolution_1_1_4/Generated_Face&Sketch_2/SketchLine_16&Sketch_1/SketchLine_10][Revolution_1_1_4/Generated_Face&Sketch_1/SketchLine_9]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_21][Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_19]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_22][Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_21]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_17][Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_22]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_15][Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_18]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_15][Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_20]")]
Group_1 = model.addGroup(Part_2_doc, "Edges", Group_1_objects)

### Create Group
Group_2_objects = [model.selection("FACE", "Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_5"),
                   model.selection("FACE", "Revolution_1_1_2/Generated_Face&Sketch_1/SketchLine_7"),
                   model.selection("FACE", "Revolution_1_1_3/Generated_Face&Sketch_1/SketchLine_12"),
                   model.selection("FACE", "Revolution_1_1_4/Generated_Face&Sketch_1/SketchLine_8"),
                   model.selection("FACE", "Revolution_1_1_5/Generated_Face&Sketch_2/SketchLine_16&Sketch_1/SketchLine_10"),
                   model.selection("FACE", "Revolution_1_1_5/Generated_Face&Sketch_2/SketchLine_14")]
Group_2 = model.addGroup(Part_2_doc, "Faces", Group_2_objects)

### Create Group
Group_3_objects = [model.selection("EDGE", "[Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_6][Revolution_1_1_1/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_6][Revolution_1_1_1/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_1/From_Face][Revolution_1_1_1/To_Face]")]
Group_3 = model.addGroup(Part_2_doc, "Edges", Group_3_objects)

### Create Group
Group_4_objects = [model.selection("EDGE", "[Revolution_1_1_2/From_Face][Revolution_1_1_2/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_2/Generated_Face&Sketch_1/SketchArc_1_2][Revolution_1_1_2/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_2/Generated_Face&Sketch_1/SketchArc_1_2][Revolution_1_1_2/To_Face]")]
Group_4 = model.addGroup(Part_2_doc, "Edges", Group_4_objects)

### Create Group
Group_5_objects = [model.selection("EDGE", "[Revolution_1_1_3/From_Face][Revolution_1_1_3/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_3/Generated_Face&Sketch_1/SketchArc_2_2][Revolution_1_1_3/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_3/Generated_Face&Sketch_1/SketchArc_2_2][Revolution_1_1_3/To_Face]")]
Group_5 = model.addGroup(Part_2_doc, "Edges", Group_5_objects)

### Create Group
Group_6_objects = [model.selection("EDGE", "[Revolution_1_1_4/Generated_Face&Sketch_1/SketchLine_9][Revolution_1_1_4/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_4/Generated_Face&Sketch_1/SketchLine_9][Revolution_1_1_4/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_4/From_Face][Revolution_1_1_4/To_Face]")]
Group_6 = model.addGroup(Part_2_doc, "Edges", Group_6_objects)

### Create Group
Group_7_objects = [model.selection("EDGE", "[Revolution_1_1_5/Generated_Face&Sketch_2/SketchLine_20][Revolution_1_1_5/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_5/Generated_Face&Sketch_2/SketchLine_20][Revolution_1_1_5/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_5/From_Face][Revolution_1_1_5/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_18][Revolution_1_1_6/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_18][Revolution_1_1_6/To_Face]")]
Group_7 = model.addGroup(Part_2_doc, "Edges", Group_7_objects)

### Create Group
Group_8_objects = [model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_22][Revolution_1_1_7/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_22][Revolution_1_1_7/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_19][Revolution_1_1_7/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_19][Revolution_1_1_7/From_Face]")]
Group_8 = model.addGroup(Part_2_doc, "Edges", Group_8_objects)

### Create Group
Group_9_objects = [model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_21][Revolution_1_1_7/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_17][Revolution_1_1_7/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_15][Revolution_1_1_6/To_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_21][Revolution_1_1_7/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_17][Revolution_1_1_7/From_Face]"),
                   model.selection("EDGE", "[Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_15][Revolution_1_1_6/From_Face]")]
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
Group_11_objects = [model.selection("FACE", "Revolution_1_1_1/From_Face"),
                    model.selection("FACE", "Revolution_1_1_2/From_Face"),
                    model.selection("FACE", "Revolution_1_1_3/From_Face"),
                    model.selection("FACE", "Revolution_1_1_4/From_Face"),
                    model.selection("FACE", "Revolution_1_1_5/From_Face"),
                    model.selection("FACE", "Revolution_1_1_6/From_Face"),
                    model.selection("FACE", "Revolution_1_1_7/From_Face")]
Group_11 = model.addGroup(Part_2_doc, "Faces", Group_11_objects)
Group_11.setName("back")
Group_11.result().setName("back")

### Create Group
Group_12_objects = [model.selection("FACE", "Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_6"),
                    model.selection("FACE", "Revolution_1_1_2/Generated_Face&Sketch_1/SketchArc_1_2"),
                    model.selection("FACE", "Revolution_1_1_3/Generated_Face&Sketch_1/SketchArc_2_2"),
                    model.selection("FACE", "Revolution_1_1_4/Generated_Face&Sketch_1/SketchLine_9"),
                    model.selection("FACE", "Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_19")]
Group_12 = model.addGroup(Part_2_doc, "Faces", Group_12_objects)
Group_12.setName("wall")
Group_12.result().setName("wall")

### Create Group
Group_13 = model.addGroup(Part_2_doc, "Faces", [model.selection("FACE", "Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_18"), model.selection("FACE", "Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_22")])
Group_13.setName("outletTop")
Group_13.result().setName("outletTop")

### Create Group
Group_14 = model.addGroup(Part_2_doc, "Faces", [model.selection("FACE", "Revolution_1_1_7/Generated_Face&Sketch_2/SketchLine_21")])
Group_14.setName("outletLeft")
Group_14.result().setName("outletLeft")

### Create Group
Group_15 = model.addGroup(Part_2_doc, "Faces", [model.selection("FACE", "Revolution_1_1_1/Generated_Face&Sketch_1/SketchLine_5")])
Group_15.setName("inlet")
Group_15.result().setName("inlet")

### Create Group
Group_16 = model.addGroup(Part_2_doc, "Faces", [model.selection("FACE", "Revolution_1_1_5/Generated_Face&Sketch_2/SketchLine_14"), model.selection("FACE", "Revolution_1_1_6/Generated_Face&Sketch_2/SketchLine_15")])
Group_16.setName("outletRight")
Group_16.result().setName("outletRight")

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Face_1_1, = SHAPERSTUDY.shape(model.featureStringId(Face_1))
Face_1_2, = SHAPERSTUDY.shape(model.featureStringId(Face_1, 1))
Face_1_3, = SHAPERSTUDY.shape(model.featureStringId(Face_1, 2))
Face_1_4, = SHAPERSTUDY.shape(model.featureStringId(Face_1, 3))
Face_1_5, = SHAPERSTUDY.shape(model.featureStringId(Face_1, 4))
Face_1_6, = SHAPERSTUDY.shape(model.featureStringId(Face_1, 5))
Face_1_7, = SHAPERSTUDY.shape(model.featureStringId(Face_1, 6))
Revolution_1_1, Group_1_1, Group_2_1, Group_3_1, Group_4_1, Group_5_1, Group_6_1, Group_7_1, Group_8_1, Group_9_1, front, back, wall, outletTop, outletLeft, inlet, outletRight, = SHAPERSTUDY.shape(model.featureStringId(Revolution_1))
###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(Revolution_1_1,'Mesh_1')
Regular_1D = Mesh_1.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(NbSg1)
Prism_3D = Mesh_1.Prism()
Regular_1D_1 = Mesh_1.Segment(geom=Group_1_1)
Sub_mesh_1 = Regular_1D_1.GetSubMesh()
Number_of_Segments_2 = Regular_1D_1.NumberOfSegments(NbSg2)
Regular_1D_2 = Mesh_1.Segment(geom=Group_2_1)
Sub_mesh_2 = Regular_1D_2.GetSubMesh()
status = Mesh_1.AddHypothesis(Number_of_Segments_1,Group_2_1)
RadialQuadrangle_1D2D = Mesh_1.Quadrangle(algo=smeshBuilder.RADIAL_QUAD,geom=Group_2_1)
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_1, Sub_mesh_2 ] ])
Regular_1D_3 = Mesh_1.Segment(geom=Group_3_1)
Number_of_Segments_3 = Regular_1D_3.NumberOfSegments(NbSg3,None,[])
Number_of_Segments_3.SetConversionMode( 0 )
Number_of_Segments_3.SetExpressionFunction( '0.5*t' )
Regular_1D_4 = Mesh_1.Segment(geom=Group_4_1)
Number_of_Segments_4 = Regular_1D_4.NumberOfSegments(NbSg4)
Regular_1D_5 = Mesh_1.Segment(geom=Group_5_1)
Number_of_Segments_5 = Regular_1D_5.NumberOfSegments(NbSg5)
Regular_1D_6 = Mesh_1.Segment(geom=Group_6_1)
Number_of_Segments_6 = Regular_1D_6.NumberOfSegments(NbSg6)
Regular_1D_7 = Mesh_1.Segment(geom=Group_7_1)
Number_of_Segments_7 = Regular_1D_7.NumberOfSegments(NbSg7)
Regular_1D_8 = Mesh_1.Segment(geom=Group_8_1)
Number_of_Segments_8 = Regular_1D_8.NumberOfSegments(NbSg8)
Regular_1D_9 = Mesh_1.Segment(geom=Group_9_1)
Number_of_Segments_9 = Regular_1D_9.NumberOfSegments(NbSg9,None,[])
Number_of_Segments_9.SetConversionMode( 0 )
Number_of_Segments_9.SetExpressionFunction( '-t*t' )
isDone = Mesh_1.Compute()
Mesh_1.CheckCompute()
front_1 = Mesh_1.GroupOnGeom(front,'front',SMESH.FACE)
[ front_1 ] = Mesh_1.GetGroups()
back_1 = Mesh_1.GroupOnGeom(back,'back',SMESH.FACE)
[ front_1, back_1 ] = Mesh_1.GetGroups()
wall_1 = Mesh_1.GroupOnGeom(wall,'wall',SMESH.FACE)
[ front_1, back_1, wall_1 ] = Mesh_1.GetGroups()
outletTop_1 = Mesh_1.GroupOnGeom(outletTop,'outletTop',SMESH.FACE)
[ front_1, back_1, wall_1, outletTop_1 ] = Mesh_1.GetGroups()
outletLeft_1 = Mesh_1.GroupOnGeom(outletLeft,'outletLeft',SMESH.FACE)
[ front_1, back_1, wall_1, outletTop_1, outletLeft_1 ] = Mesh_1.GetGroups()
inlet_1 = Mesh_1.GroupOnGeom(inlet,'inlet',SMESH.FACE)
[ front_1, back_1, wall_1, outletTop_1, outletLeft_1, inlet_1 ] = Mesh_1.GetGroups()
outletRight_1 = Mesh_1.GroupOnGeom(outletRight,'outletRight',SMESH.FACE)
[ front_1, back_1, wall_1, outletTop_1, outletLeft_1, inlet_1, outletRight_1 ] = Mesh_1.GetGroups()
try:
  Mesh_1.ExportUNV( r'/home/mark/OpenFOAM/mark-12/run/nozzle_1/geometry/Mesh.unv', 0 )
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


## Set names of Mesh objects
smesh.SetName(front_1, 'front')
smesh.SetName(Number_of_Segments_4, 'Number of Segments_4')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(Sub_mesh_7, 'Sub-mesh_7')
smesh.SetName(Sub_mesh_5, 'Sub-mesh_5')
smesh.SetName(Sub_mesh_3, 'Sub-mesh_3')
smesh.SetName(Number_of_Segments_9, 'Number of Segments_9')
smesh.SetName(Sub_mesh_4, 'Sub-mesh_4')
smesh.SetName(Number_of_Segments_3, 'Number of Segments_3')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Number_of_Segments_8, 'Number of Segments_8')
smesh.SetName(outletTop_1, 'outletTop')
smesh.SetName(inlet_1, 'inlet')
smesh.SetName(Sub_mesh_6, 'Sub-mesh_6')
smesh.SetName(outletLeft_1, 'outletLeft')
smesh.SetName(outletRight_1, 'outletRight')
smesh.SetName(Number_of_Segments_6, 'Number of Segments_6')
smesh.SetName(Sub_mesh_9, 'Sub-mesh_9')
smesh.SetName(back_1, 'back')
smesh.SetName(RadialQuadrangle_1D2D.GetAlgorithm(), 'RadialQuadrangle_1D2D')
smesh.SetName(Number_of_Segments_5, 'Number of Segments_5')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(wall_1, 'wall')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(Number_of_Segments_7, 'Number of Segments_7')
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')
smesh.SetName(Prism_3D.GetAlgorithm(), 'Prism_3D')
smesh.SetName(Sub_mesh_8, 'Sub-mesh_8')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
# change params for setFields
file = open("/home/mark/OpenFOAM/mark-12/run/nozzle_1/params.txt", "a")
file.write(f"width\n{l_left_/1000}\n\nheight\n{d_inlet_/2000}")
file.close()
