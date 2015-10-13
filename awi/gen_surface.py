#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import sys

#Used to save test surfaces to files that ArcGRID files which GDAL can read
def writeArrayToArcGrid(filename,arr):
  arr                = np.copy(arr)
  arr[np.isnan(arr)] = -9999
  arr                = np.flipud(arr)
  fout               = open(filename,'wb')
  headerstring       = bytes('NCOLS %d\nNROWS %d\nXLLCENTER %f\nYLLCENTER %f\nCELLSIZE %f\nNODATA_value %f\n' % (arr.shape[1], arr.shape[0], -4.2000, 53.2200, 3,-9999), 'UTF-8')
  fout.write(headerstring)
  np.savetxt(fout,arr,'%5.5f')

if len(sys.argv)!=2:
  print("Syntax: {0} <show/noshow>".format(sys.argv[0]))
  print("\tshow   = Show surfaces as they are generated")
  print("\tnoshow = Don't show surfaces")

#Generate test surface z(x,y) = sin(x cos(y))
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx*np.cos(yy))

#Show test surface
if sys.argv[1]=="show":
  plt.contourf(x,y,z)
  plt.show()

writeArrayToArcGrid("./sin-x-cos-y.asc", z)