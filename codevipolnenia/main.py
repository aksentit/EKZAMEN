import cv2
image = cv2.imread("F:\papka\image.jpg") #путь к файлу
def viewImage(image, name_of_window): #функция показа изображения
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0) #после нажатия кнопки
    cv2.destroyAllWindows() #закрыть все окна после нажатия любой кнопки
output = image.copy() #копируется изображение
cv2.putText(output, "Best", (100, 900),cv2.FONT_HERSHEY_SIMPLEX, 6, (10, 5, 200), 20) #вставляется текст, прописывается размер, цвет и ширина, а так же координаты x and y
viewImage(output, "sdfghsdrgger") #показ исходного изображения
