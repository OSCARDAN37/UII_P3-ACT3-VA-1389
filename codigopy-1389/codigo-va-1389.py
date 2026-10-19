# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os
# ruta de imagen
ruta_imagen = os.path.join(
    "imagen-original-1389",
    "img-tostadora-1389.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
Tostadora = cv2.imread(ruta_imagen)
# convertir de BGR a RGB
tosti = cv2.cvtColor(Tostadora, cv2.COLOR_BGR2RGB)
# print(Tostadora) Muestra las matrices de la imagen
cv2.imshow("tostadora original 1389",Tostadora)
cv2.waitKey(0) # tiempo de espera
cv2.destroyAllWindows() # destruye todas las ventanas en memoria

cv2.imshow("tostadora RGB 1389",tosti)
cv2.waitKey(0)
cv2.destroyAllWindows()