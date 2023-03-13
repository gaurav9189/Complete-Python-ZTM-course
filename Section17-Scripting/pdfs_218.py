import PyPDF2

# pdf is a binary file hence 'rb'
with open('pdf/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    # print(len(reader.pages))
    page = reader.getPage(0)
    rotated = page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(rotated)

    with open('pdf/tilt.pdf', 'wb') as new_file:
        writer.write(new_file)
        print(writer.getPage(0))
