import subprocess
import sys

def instalar_dependencias():
    print("Iniciando la instalación de las dependencias...")
    # Usa exactamente el intérprete de Python actual para instalar
    resultado = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    if resultado.returncode == 0:
        print("\n¡Dependencias instaladas exitosamente en esta versión de Python!")
    else:
        print("\nHubo un error al instalar las dependencias.")

if __name__ == "__main__":
    instalar_dependencias()