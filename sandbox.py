import os

def listar_archivos_recursivamente(ruta):
    for raiz, directorios, archivos in os.walk(ruta):
        for archivo in archivos:
            archivo_completo = os.path.join(raiz, archivo)
            print(archivo_completo)

def listar_archivos_en_carpeta_de_usuario():
    carpeta_usuario = os.path.expanduser("~")  # Obtiene la ruta de la carpeta de usuario
    print(f"Archivos en la carpeta de usuario ({carpeta_usuario}) y sus subdirectorios:")

    listar_archivos_recursivamente(carpeta_usuario)

if __name__ == "__main__":
    listar_archivos_en_carpeta_de_usuario()
