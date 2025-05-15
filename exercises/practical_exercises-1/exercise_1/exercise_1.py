# ----------------------------------Exercise 1--------------------------------------

# A) Diferencia en porcentaje entre el curso actual y:
#   - El más rapido de otros cursos.
#   - El más lento de otros cursos.
#   - El promedio de los cursos.

# data -> duracción.
course_current = 1.5
course_min = 2.5
course_max = 7
course_avg = 4

# result -> A.
print("----------------------------Start Result A------------------------------")
difference_with_min = 100 - round((course_current / course_min * 100), 2)
print(f"Diferencia en procentaje entre el curso actual y el min (rapido) es igual a: {difference_with_min}%.")
difference_with_max = 100 - round((course_current / course_max * 100), 2)
print(f"Diferencia en procentaje entre el curso actual y el max (lento) es igual a: {difference_with_max}%.")
difference_with_avg = 100 - round((course_current / course_avg * 100), 2)
print(f"Diferencia en procentaje entre el curso actual y el avg (promedio) es igual a: {difference_with_avg}%.")
print("----------------------------End Result A------------------------------")

# B) Porcentaje de material inservible que se reduce en:
#   - El promedio de los cursos.
#   - El curso actual.

# data -> crudo.
raw_avg = 5
raw_current = 3.5

# result -> B.
print("----------------------------Start Result B------------------------------")
time_raw_avg = 100 - round((course_avg / raw_avg * 100), 2)
print(f"El promedio vacio de los cursos es igual a: {time_raw_avg}%.")
time_raw_course_current = 100 - round((course_current / raw_current * 100), 2)
print(f"El tiempo vacio de el curso es igual a: {time_raw_course_current}%.")
print("----------------------------End Result B------------------------------")

# C) Ver 10 horas de este curso a cuantas horas de otros cursos equivale?¿y al revés?.

# result -> C.
print("----------------------------Start Result C------------------------------")
print(f"Ver 10 horas de este curso equivale a ver {round((course_avg / course_current * 10), 2)} horas de otros cursos.")
print(f"Ver 10 horas de otros cursos equivale a ver {round((course_current / course_avg * 10), 2)} horas de este curso.")
print("----------------------------End Result C------------------------------")