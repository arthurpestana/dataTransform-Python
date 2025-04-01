import pandas as pd
from modules import extractTables

def dataTransform(pdfPath, fileName):
    dataFrame = pd.DataFrame(extractTables(pdfPath))

    dataFrame.columns = dataFrame.columns.astype(str)

    for row in dataFrame.values:
        for i, item in enumerate(row):
            if (item == "AMB"):
                row[i] = "Seg. Ambulatorial"
            elif (item == "OD"):
                row[i] = "Seg. Odontológica"
    
    dataFrame.to_csv(fileName, index=False, header=False, encoding='utf-8-sig', sep=';')