import numpy as np
import pandas as pd
import datetime


bto_names = [ "Ba_core", "Ba_shel", "Ti_core", "Ti_shel", "O1_core", "O1_shel", "O2_core", "O2_shel", "O3_core", "O3_shel"]
bto_tags = ['Ba', 'Ba', 'Ti', 'Ti', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ']
bto_atomtypes = [1, 5, 2, 6, 3, 7, 3, 7, 3, 7]
bto_bondtypes = [1, 2, 3, 3, 3]
bto_masses = [135.33, 2, 45.88, 2, 13.999, 2, 13.999, 2, 13.999, 2]
bto_charges = [5.62, -3.76, 4.76, -1.58, 0.91, -2.59, 0.91, -2.59, 0.91, -2.59]
bto_disp_xs = [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.5, 0.5, 0.5, 0.5]
bto_disp_ys = [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 0.5, 0.5]
bto_disp_zs = [1.0587754104E-02, 1.0587754104E-02, 5.2606162012E-01, 5.2606162012E-01, 4.9144046563E-01, 4.9144046563E-01, 4.9144046563E-01, 4.9144046563E-01, -1.9530305493E-02, -1.9530305493E-02]
bto_elements = pd.DataFrame({'tag': bto_tags, 'mass': bto_masses, 'atomtype': bto_atomtypes, 'charge': bto_charges, 'disp_x': bto_disp_xs, 'disp_y': bto_disp_ys, 'disp_z': bto_disp_zs}, index=bto_names)
sto_names = [ "Sr_core", "Sr_shel", "Ti_core", "Ti_shel", "O1_core", "O1_shel", "O2_core", "O2_shel", "O3_core", "O3_shel"]
sto_tags = ['Sr', 'Sr', 'Ti', 'Ti', 'O ', 'O ', 'O ', 'O ', 'O ', 'O ']
sto_atomtypes = [4, 8, 2, 6, 3, 7, 3, 7, 3, 7]
sto_bondtypes = [4, 2, 3, 3, 3]
sto_masses = [85.62, 2, 45.88, 2, 13.999, 2, 13.999, 2, 13.999, 2]
sto_charges = [5.62, -3.76, 4.76, -1.58, 0.91, -2.59, 0.91, -2.59, 0.91, -2.59]
sto_disp_xs = [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.5, 0.5, 0.5, 0.5]
sto_disp_ys = [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.0, 0.0, 0.5, 0.5]
sto_disp_zs = [1.0587754104E-02, 1.0587754104E-02, 5.2606162012E-01, 5.2606162012E-01, 4.9144046563E-01, 4.9144046563E-01, 4.9144046563E-01, 4.9144046563E-01, -1.9530305493E-02, -1.9530305493E-02]
sto_elements = pd.DataFrame({'tag': sto_tags, 'mass': sto_masses, 'atomtype': sto_atomtypes, 'charge': sto_charges, 'disp_x': sto_disp_xs, 'disp_y': sto_disp_ys, 'disp_z': sto_disp_zs}, index=sto_names)



num_bto = 1 * 2
num_sto = 1 * 2
num_unitcell = num_bto + num_sto  # number of unitcell along x-dir; y and z direction use the 'replicate' of lammps to generate
num_atom = num_unitcell * 10
num_bond = int(num_atom / 2)
num_atomtype = 8
num_bondtype = int(num_atomtype / 2)
latt_x, latt_y, latt_z = [ 1 , 2, 4 ]


cont_lmp = f"""# File generated by hsulan5c {datetime.datetime.now()}
  
      {num_atom:6}  atoms
      {num_bond:6}  bonds
      {num_atomtype:6}  atom types
      {num_bondtype:6}  bond types
 
      0.00       {latt_x:10.8f}  xlo xhi
      0.00       {latt_y:10.8f}  ylo yhi
      0.00       {latt_z:10.8f}  zlo zhi
 
Masses
 
            1   135.33       # Ba core
            2   45.88        # Ti core
            3   13.999       # O  core
            4   85.62        # Sr core
            5   2            # Ba shell
            6   2            # Ti shell
            7   2            # O  shell
            8   2            # Sr shell

"""

atom = f"""Atoms # full

"""

'''to generate uu structure'''
for i in range(int(num_bto/2)):
    j = 1
    for index, row in bto_elements.iterrows():
        atomID = i * 10 + j
        moleID = int(np.ceil(atomID/2))
        atom += f"""{atomID:5} {moleID:5} {row['atomtype']:3} {row['charge']:6} {((row['disp_x']+i)/num_unitcell):10.6f} {row['disp_y']:10.6f} {row['disp_z']:10.6f}\n"""
        j += 1

for i in range(int(num_sto/2)):
    j = 1
    for index, row in sto_elements.iterrows():
        atomID = i * 10 + j + int(num_bto/2) * 10
        moleID = int(np.ceil(atomID/2))
        atom += f"""{atomID:5} {moleID:5} {row['atomtype']:3} {row['charge']:6} {((row['disp_x']+i+(num_bto/2))/num_unitcell):10.6f} {row['disp_y']:10.6f} {row['disp_z']:10.6f}\n"""
        j += 1

for i in range(int(num_bto/2)):
    j = 1
    for index, row in bto_elements.iterrows():
        atomID = i * 10 + j + int((num_bto + num_sto)/2) * 10
        moleID = int(np.ceil(atomID/2))
        atom += f"""{atomID:5} {moleID:5} {row['atomtype']:3} {row['charge']:6} {((row['disp_x']+i+int(num_unitcell/2))/num_unitcell):10.6f} {row['disp_y']:10.6f} {row['disp_z']:10.6f}\n"""
        j += 1

for i in range(int(num_sto/2)):
    j = 1
    for index, row in sto_elements.iterrows():
        atomID = i * 10 + j + int(num_bto+num_sto/2) * 10
        moleID = int(np.ceil(atomID/2))
        atom += f"""{atomID:5} {moleID:5} {row['atomtype']:3} {row['charge']:6} {((row['disp_x']+i+int(num_bto+num_sto/2))/num_unitcell):10.6f} {row['disp_y']:10.6f} {row['disp_z']:10.6f}\n"""
        j += 1
 

bond = f"""
Bonds

"""

for i in range(int(num_bto/2)):
    j = 1
    for bondtype in bto_bondtypes:
        moleID = i * len(bto_bondtypes) + j
        atomID_1 = moleID * 2 - 1
        atomID_2 = moleID * 2
        bond += f"""{moleID} {bondtype} {atomID_1} {atomID_2}\n"""
        j += 1
for i in range(int(num_sto/2)):
    j = 1
    for bondtype in sto_bondtypes:
        moleID = (i + int(num_bto/2)) * len(sto_bondtypes) + j
        atomID_1 = moleID * 2 - 1
        atomID_2 = moleID * 2
        bond += f"""{moleID} {bondtype} {atomID_1} {atomID_2}\n"""
        j += 1
for i in range(int(num_bto/2)):
    j = 1
    for bondtype in bto_bondtypes:
        moleID = (i + int(num_unitcell/2)) * len(bto_bondtypes) + j
        atomID_1 = moleID * 2 - 1
        atomID_2 = moleID * 2
        bond += f"""{moleID} {bondtype} {atomID_1} {atomID_2}\n"""
        j += 1
for i in range(int(num_sto/2)):
    j = 1
    for bondtype in sto_bondtypes:
        moleID = (i + int((num_unitcell+num_bto)/2)) * len(sto_bondtypes) + j
        atomID_1 = moleID * 2 - 1
        atomID_2 = moleID * 2
        bond += f"""{moleID} {bondtype} {atomID_1} {atomID_2}\n"""
        j += 1

with open(f"B{num_bto}S{num_sto}TO_uu", "w") as outf:
    outf.write(cont_lmp)
    outf.write(atom)
    outf.write(bond)
