import pdfplumber

def extractTables(pdfPath):
    with pdfplumber.open(pdfPath) as pdf:

        allTables = []
        for page in pdf.pages:
            tables  = page.extract_tables()
            if tables:
                for table in tables:
                    allTables.extend(table)
        return allTables