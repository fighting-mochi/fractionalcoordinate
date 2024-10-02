import numpy as np
import pandas as pd
import datetime


b = 1
s = 0
x = (b+s) # (b + s) * 2


box_x, box_y, box_z = [10, 10, 10]

names = [ "Ba_core", "Ba_shel", "Ti_core", "Ti_shel", "O1_core", "O1_shel", "O2_core", "O2_shel", "O3_core", "O3_shel", "Sr_core", "Sr_shel"]
tags = ['Ba', 'Ba', 'Ti', 'Ti', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ', 'Sr', 'Sr']
masses = [137.33, 1.3733, 47.88, 4.788, 15.999, 1.5999, 15.999, 1.5999, 15.999, 1.5999, 85.62, 2.0]
charges = [5.62, -3.76, 4.76, -1.58, 0.91, -2.59, 0.91, -2.59, 0.91, -2.59, 5.62, -3.76]
disp_xs = [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0]
disp_ys = [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0]
disp_zs = [1.0587754104E-02, 1.0587754104E-02, 5.2606162012E-01, 5.2606162012E-01, 4.9144046563E-01, 4.9144046563E-01, 4.9144046563E-01, 4.9144046563E-01, -1.9530305493E-02, -1.9530305493E-02, 1.0587754104E-02, 1.0587754104E-02]
elements = pd.DataFrame({'tag': tags, 'mass': masses, 'charge': charges, 'disp_x': disp_xs, 'disp_y': disp_ys, 'disp_z': disp_zs}, index=names)


header=f"""Number of particles = {x*5}
A = 1 Angstrom (basic length-scale)
H0(1,1) = {box_x} A
H0(1,2) = 0 A
H0(1,3) = 0 A
H0(2,1) = 0 A
H0(2,2) = {box_y} A
H0(2,3) = 0 A
H0(3,1) = 0 A
H0(3,2) = 0 A
H0(3,3) = {box_z} A
.NO_VELOCITY.
entry_count = 4
auxiliary[0] = q
"""





strc=""

'''to generate ud structure'''
# for i in range(b): #[0,1,2,3,4,5]
#     if i == b-1:   # i=5
#         strc += f"{((Ba_x+i)/x):20.6f} {Ba_y:10.6f} {0.0:10.6f} # Ba {i} # DW\n"
#     else:
#         strc += f"{((Ba_x+i)/x):20.6f} {Ba_y:10.6f} {Ba_z:10.6f} # Ba {i}\n" 
# for j in range(b): # [7,8,9,10,11,12]:
#     i = j + b + s
#     if i == b*2:
#         strc += f"{((Ba_x+i)/x):20.6f} {Ba_y:10.6f} {0.0:10.6f} # Ba {i} # DW\n"
#     else:
#         strc += f"{((Ba_x+i)/x):20.6f} {Ba_y:10.6f} {(1-Ba_z):10.6f} # Ba {i}\n" 
# 
# for i in range(b-1): #[0,1,2,3,4]:
#     strc += f"{((Ti_x+i)/x):20.6f} {Ti_y:10.6f} {Ti_z:10.6f} # Ti {i}\n"
# for j in range(b+s): #[5,6,7,8,9,10,11]:
#     i = j + b - 1
#     strc += f"{((Ti_x+i)/x):20.6f} {Ti_y:10.6f} {(1-Ti_z):10.6f} # Ti {i}\n"
# for j in range(s*2): #[12,13]:
#     i = j + b*2
#     strc += f"{((Ti_x+i)/x):20.6f} {Ti_y:10.6f} {Ti_z:10.6f} # Ti {i}\n"
# 
# for i in range(b-1): #[0,1,2,3,4]:
#     strc += f"{((O1_x+i)/x):20.6f} {O1_y:10.6f} {O1_z:10.6f} # O1 {i}\n"
#     strc += f"{((O2_x+i)/x):20.6f} {O2_y:10.6f} {O2_z:10.6f} # O2 {i}\n"
#     strc += f"{((O3_x+i)/x):20.6f} {O3_y:10.6f} {(1+O3_z):10.6f} # O3 {i}\n"
# for j in range(b+s): #[5,6,7,8,9,10,11]:
#     i = j + b - 1
#     if i == b - 1:
#         strc += f"{((O1_x+i)/x):20.6f} {O1_y:10.6f} {0.5:10.6f} # O1 {i} # DW\n"
#     else:
#         strc += f"{((O1_x+i)/x):20.6f} {O1_y:10.6f} {(1-O1_z):10.6f} # O1 {i}\n"
#     strc += f"{((O2_x+i)/x):20.6f} {O2_y:10.6f} {(1-O2_z):10.6f} # O2 {i}\n"
#     strc += f"{((O3_x+i)/x):20.6f} {O3_y:10.6f} {(-O3_z):10.6f} # O3 {i}\n"
# for j in range(s*2): #[12,13]:
#     i = j + b*2
#     if i == b*2:
#         strc += f"{((O1_x+i)/x):20.6f} {O1_y:10.6f} {0.5:10.6f} # O1 {i} # DW\n"
#     else:
#         strc += f"{((O1_x+i)/x):20.6f} {O1_y:10.6f} {O1_z:10.6f} # O1 {i}\n"
#     strc += f"{((O2_x+i)/x):20.6f} {O2_y:10.6f} {O2_z:10.6f} # O2 {i}\n"
#     strc += f"{((O3_x+i)/x):20.6f} {O3_y:10.6f} {(1+O3_z):10.6f} # O3 {i}\n"
# 
# for j in range(s):
#     i = b + j
#     strc += f"{((Ba_x+i)/x):20.6f} {Ba_y:10.6f} {(1-Ba_z):10.6f} # Sr {i}\n" 
# for j in range(s):
#     i = 2*b + j + s
#     strc += f"{((Ba_x+i)/x):20.6f} {Ba_y:10.6f} {Ba_z:10.6f} # Sr {i}\n" 
# 
# with open(f"B{b}S{s}_ud.frac", "w") as outf:
#     outf.write(header)
#     outf.write(strc)

'''to generate uu structure'''
for i in range(2):
    if i == 1:
        for index, row in elements[10:].iterrows():
            strc += f"""
{row['mass']}
{row['tag']}
{((row['disp_x']+i)/x):10.6f} {row['disp_y']:10.6f} {row['disp_z']:10.6f} {row['charge']}"""
        for index, row in elements[2:10].iterrows():
            strc += f"""
{row['mass']}
{row['tag']}
{((row['disp_x']+i)/x):10.6f} {row['disp_y']:10.6f} {row['disp_z']:10.6f} {row['charge']}"""
    else:
        for index, row in elements[:10].iterrows():
            strc += f"""
{row['mass']}
{row['tag']}
{((row['disp_x']+i)/x):10.6f} {row['disp_y']:10.6f} {row['disp_z']:10.6f} {row['charge']}"""



#     for e in elements:
#         strc += f"""
# {e['mass']}
# {e['tag']}
# {((Ba_core_x+i)/x):10.6f} {Ba_core_y:10.6f} {Ba_core_z:10.6f} {Ba_core['charge']}
# """

with open("check", "w") as outf:
    outf.write(header)
    outf.write(strc)

# elements.loc['Ba_core', 'mass']
# for index, row in elements.iterrows():
#     ...:     print(row['mass'])

             # elements.loc['Ba_core', 'mass']

#for i in [0,1,2,3,4,5, 7,8,9,10,11,12]:
#    strc += f"{((Ba_x+i)/x):10.6f} {Ba_y:10.6f} {Ba_z:10.6f} # Ba\n" 
#
#for i in range(n):
#    strc += f"{((Ti_x+i)/x):10.6f} {Ti_y:10.6f} {Ti_z:10.6f} # Ti\n"
#
#for i in range(n):
#    strc += f"{((O1_x+i)/x):10.6f} {O1_y:10.6f} {O1_z:10.6f} # O1\n"
#    strc += f"{((O2_x+i)/x):10.6f} {O2_y:10.6f} {O2_z:10.6f} # O2\n"
#    strc += f"{((O3_x+i)/x):10.6f} {O3_y:10.6f} {O3_z:10.6f} # O3\n"
#
#for i in [6,13]:
#    strc += f"{((Ba_x+i)/x):10.6f} {Ba_y:10.6f} {Ba_z:10.6f} # Sr\n" 
#
#with open("B6S1_uu.frac", "w") as outf:
    # outf.write(header)
#    outf.write(strc)
