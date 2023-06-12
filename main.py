import os
import re
import pytesseract
import easyocr
import time


# Canviar path de tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Ferran.MERCADER-ALVA\PycharmProjects\auto-backend' \
                                        r'\Dependencies\mib\Tesseract-OCR\tesseract.exe'


def detect_dorsal(image):
    start = time.time()
    reader = easyocr.Reader(['en'])  # this needs to run only once to load the model into memory
    result = reader.readtext(image)
    end = time.time()
    pattern1 = r'^[0-9]{3}-.*$'
    pattern2 = r'^[0-9]{3}.*$'
    pattern3 = r'^[A-Za-z]{2}.*\d{2}$'
    for res in result:
        print(res[1])
        if re.match(pattern1, res[1]):
            dorsal = re.sub(r'\|', 'I', res[1])
            print(dorsal, 'its a dorsal')

        elif re.match(pattern2, res[1]):
            dorsal = re.sub(r'\|', 'I', res[1])
            print(dorsal, 'its a dorsal')

        elif re.match(pattern3, res[1]):
            dorsal = re.sub(r'\|', 'I', res[1])
            print(dorsal, 'its a dorsal')

    print("[INFO] try_easyORC {:.6f} seconds".format(end - start))


def obtener_paths_fotos(carpeta):
    paths_fotos = []

    # Obtiene la ruta absoluta de la carpeta actual
    ruta_actual = os.getcwd()

    # Combina la ruta actual con el nombre de la carpeta
    ruta_carpeta = os.path.join(ruta_actual, carpeta)

    # Verifica si la carpeta existe
    if os.path.exists(ruta_carpeta) and os.path.isdir(ruta_carpeta):
        # Recorre todos los archivos en la carpeta
        for archivo in os.listdir(ruta_carpeta):
            # Verifica si el archivo es una foto (extensión jpg, jpeg, png, etc.)
            extension = os.path.splitext(archivo)[1].lower()
            if extension in ['.jpg', '.jpeg', '.png', '.gif']:
                # Combina la ruta de la carpeta con el nombre del archivo
                path_foto = os.path.join(ruta_carpeta, archivo)
                paths_fotos.append(path_foto)

    return paths_fotos


if __name__ == '__main__':

    for image_path in obtener_paths_fotos(r'C:\Users\Ferran.MERCADER-ALVA\PycharmProjects\OCR_martin\images'):
        detect_dorsal(image_path)
