# Importamos las librerias necesarias
from typing import Container
from cv2 import cv2
import numpy as np

var_gauss = 3
var_kernel = 5

# Capturamos la imagen desde una ubicación relativa
img = cv2.imread('monedas.jpg')
# Pasamos la imagen original a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Desefoque gaussiano
gauss = cv2.GaussianBlur(gray, (var_gauss, var_gauss), 0)
# Eliminacion de ruidos
canny = cv2.Canny(gauss, 10, 180)

# Utilizamos Nunpy
kernel = np.ones((var_kernel, var_kernel), np.uint8)
outline = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

contour, jerarquia = cv2.findContours(outline.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"Monedas encontradas: {len(contour)}")
cv2.drawContours(img, contour, -1, (0, 0,255), 2)
# Mostramos la imagen
#cv2.imshow('Soles', img)
#cv2.imshow('Gris', gray)
#cv2.imshow('Gauss', gauss)
cv2.imshow('Canny', canny)
cv2.imshow('Resutaldo', img)

cv2.waitKey(0)