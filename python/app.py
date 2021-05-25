import pikepdf

def create_extractable_pdf(pdfPath, pdfPassword, pdfCopyPath):

    print(pdfPath)
    pdf = pikepdf.open(pdfPath, allow_overwriting_input=True, password=pdfPassword)
    fileName = pdfPath.split('/')
    fileName = fileName.pop()
    pdf.save("pdfCopyPath"+fileName)


if __name__ == "__main__":
    pdfPath = "C:\\Users\\jpsese\\Documents\\UiPath\\Billing Statement\\ACEPH SOA 1 (password SMPRIMEH01-006) - Copy.pdf"
    print(pdfPath)
    create_extractable_pdf(pdfPath,
                           "SMPRIMEH01-006")