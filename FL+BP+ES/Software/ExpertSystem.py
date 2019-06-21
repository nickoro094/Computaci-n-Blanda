from pyDatalog import pyDatalog

pyDatalog.create_terms('Riesgo, vel, Aviso')


+Riesgo(0,"70-90")
+Riesgo(1,"50-60")
+Riesgo(2,"30-40")
+Riesgo(3,"10-30")

V(Riesgo,Aviso) <= vel(Riesgo, Aviso)