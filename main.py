import modules.csvHandler as csvHandler
from modules import dataTransform, compactFile

def main():
    pdfName = 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
    fileName = 'conversaoDados.csv'
    zipName = 'Teste_arthur_henrique_pestana_schneider.zip'

    dataTransform(pdfName, fileName)
    compactFile(fileName, zipName)

    print(f"Arquivo compactado!")

main()