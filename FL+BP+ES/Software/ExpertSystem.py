from pyDatalog import pyDatalog

pyDatalog.create_terms('Riesgo, vel, Aviso')


+Riesgo(0,"45-90")
+Riesgo(1,"30-60")
+Riesgo(2,"20-40")
+Riesgo(3,"10-30")

V(Riesgo,Aviso) <= vel(Riesgo, Aviso)