# Computaci-n-Blanda

El código de Backpropagation.py utiliza como entradas el archivo cancerdata.csv

El archivo cancerdata.csv tiene los datos de 600 tumores de cancer de mama. Cada fila
está compuesta por 10 columnas con los datos organizados de izquierda a derecha así:
1. Clump Thickness: 1 - 10 
2. Uniformity of Cell Size: 1 - 10 
3. Uniformity of Cell Shape: 1 - 10 
4. Marginal Adhesion: 1 - 10 
5. Single Epithelial Cell Size: 1 - 10 
6. Bare Nuclei: 1 - 10 
7. Bland Chromatin: 1 - 10 
8. Normal Nucleoli: 1 - 10 
9. Mitoses: 1 - 10 
10. Class: (2 for benign, 4 for malignant)

Backpropagation.py se entrena por 200 épocas y luego da como salidas el resultado esperado y la predicción del algoritmo,
si la preducción fue correcta la línea es visualizada con fuente color verde, de lo contrario la fuente es roja.
Finalmente se muestra la presición del algoritmo.

NOTA: El código utiliza para el formato de colores de fuente códigos de escape ANSI, por lo tanto solo se pueden
visualizar correctamente los colores de fuente en las salidas en sistemas LINUX/UNIX o en un entorno como PyCharm en Windows.

