
import os
import zipfile

def compactFile(filePath, zipName):
    with zipfile.ZipFile(zipName, 'w') as zipf:
        zipf.write(filePath, os.path.basename(filePath))
        os.remove(filePath)