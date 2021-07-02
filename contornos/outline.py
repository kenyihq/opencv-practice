import cv2 # Importamos a OpenCV

# Capturamos la imagen con una ruta relativa
img = cv2.imread('contorno.jpg')
# Convertimos la imagen a grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Capturamos el Umbral de la imagen ('_' variable ficticia)
_, umbral = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
contorn, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contorn, 1, (255,60,50), 3)
# Mostramos la imagen en una ventana
cv2.imshow('Imagen Original', img)
cv2.imshow('Imagen en grises', gray)
cv2.imshow('Imagen con umbral', umbral)
cv2.waitKey(0) # 1 dinamicom 0 estatico
cv2.destroyAllWindows() # Cierra todas las ventanas abiertas