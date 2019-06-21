from fuzzylite import *

# Variables: Estado_carretera, lluvia, Hora, Dia, Mes, Riesgo

eng = Engine

Estado_carretera = eng.variable("Estado_carretera", 0, 100)
eng.output_variable(Estado_carretera, "Mala")
eng.output_variable(Estado_carretera, "Regular")
eng.output_variable(Estado_carretera, "Buena")

eng.output_variable(Estado_carretera, 0, "Triangular", (0, 33, 66))
eng.output_variable(Estado_carretera, 1, "Triangular", (33, 66, 100))
eng.output_variable(Estado_carretera, 2, "Trapezoidal_Derecho", (66, 100))

lluvia = eng.variable("lluvia", 0, 100)
eng.output_variable(lluvia, "Poca")
eng.output_variable(lluvia, "Moderada")
eng.output_variable(lluvia, "Excesiva")

eng.output_variable(lluvia, 0, "Triangular", (0, 33, 66))
eng.output_variable(lluvia, 1, "Triangular", (33, 66, 100))
eng.output_variable(lluvia, 2, "Trapezoidal_Derecho", (66, 100))

Hora = eng.variable("Hora", 0, 23)
eng.output_variable(Hora, "Madrugada")
eng.output_variable(Hora, "Mañana")
eng.output_variable(Hora, "Medio_dia")
eng.output_variable(Hora, "Tarde")
eng.output_variable(Hora, "Noche")

eng.output_variable(Hora, 0, "Triangular", (0, 6, 9))
eng.output_variable(Hora, 1, "Triangular", (6, 9, 11))
eng.output_variable(Hora, 2, "Triangular", (11, 13, 14))
eng.output_variable(Hora, 3, "Triangular", (14, 16, 18))
eng.output_variable(Hora, 4, "Triangular", (18, 21, 23))

Dia = eng.variable("Dia", 1, 7)
eng.output_variable(Dia, "Lunes")
eng.output_variable(Dia, "Martes")
eng.output_variable(Dia, "Miercoles")
eng.output_variable(Dia, "Jueves")
eng.output_variable(Dia, "Viernes")
eng.output_variable(Dia, "Sabado")
eng.output_variable(Dia, "Domingo")

Mes = eng.variable("Mes", 1, 12)
eng.output_variable(Mes, "Enero")
eng.output_variable(Mes, "Febrero")
eng.output_variable(Mes, "Marzo")
eng.output_variable(Mes, "Abril")
eng.output_variable(Mes, "Mayo")
eng.output_variable(Mes, "Junio")
eng.output_variable(Mes, "Julio")
eng.output_variable(Mes, "Agosto")
eng.output_variable(Mes, "Septiembre")
eng.output_variable(Mes, "Octubre")
eng.output_variable(Mes, "Noviembre")
eng.output_variable(Mes, "Diciembre")

eng.output_variable(Mes, 0, "Singleton", (1, 1))
eng.output_variable(Mes, 1, "Singleton", (2, 2))
eng.output_variable(Mes, 2, "Singleton", (3, 3))
eng.output_variable(Mes, 3, "Singleton", (4, 4))
eng.output_variable(Mes, 4, "Singleton", (5, 5))
eng.output_variable(Mes, 5, "Singleton", (6, 6))
eng.output_variable(Mes, 6, "Singleton", (7, 7))
eng.output_variable(Mes, 7, "Singleton", (8, 8))
eng.output_variable(Mes, 8, "Singleton", (9, 9))
eng.output_variable(Mes, 9, "Singleton", (10, 10))
eng.output_variable(Mes, 10, "Singleton", (11, 11))
eng.output_variable(Mes, 11, "Singleton", (12, 12))

Riesgo = eng.variable("Riesgo", 0, 100)
eng.output_variable(Riesgo, "Bajo")
eng.output_variable(Riesgo, "Medio")
eng.output_variable(Riesgo, "Alto")

eng.output_variable(Riesgo, 0, "Triangular", (0, 33, 66))
eng.output_variable(Riesgo, 1, "Triangular", (33, 66, 100))
eng.output_variable(Riesgo, 2, "Trapezoidal_Derecho", (66, 100))

reglas = 'reglas'
eng.rule_block(reglas, "if Estado_carretera is Mala and lluvia is Poca then Riesgo Medio")
eng.rule_block(reglas, "if Estado_carretera is Mala and lluvia is Moderada then Riesgo Alto")
eng.rule_block(reglas, "if Estado_carretera is Mala and lluvia is Excesiva then Riesgo Alto")
eng.rule_block(reglas, "if Estado_carretera is Regular and lluvia is Poca then Riesgo Bajo")
eng.rule_block(reglas, "if Estado_carretera is Regular and lluvia is Moderada then Riesgo Medio")
eng.rule_block(reglas, "if Estado_carretera is Regular and lluvia is Excesiva then Riesgo Medio")
eng.rule_block(reglas, "if Estado_carretera is Buena and lluvia is Poca then Riesgo Bajo")
eng.rule_block(reglas, "if Estado_carretera is Buena and lluvia is Moderada then Riesgo Medio")
eng.rule_block(reglas, "if Estado_carretera is Buena and lluvia is Excesiva then Riesgo Medio")


def Riesgo(A, B, C, D, E):
    festadocarretera = eng.process(A, Estado_carretera)
    fpresencialluvia = eng.process(B, lluvia)
    fhora = eng.process(C, Hora)
    fdia = eng.process(D, Dia)
    fmes = eng.process(E, Mes)
    Resultado = eng.process(A, B, C, D, E)
    return Resultado
