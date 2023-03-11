from PyPDF2 import PdfFileReader, PdfFileWriter
import sys


# open the watermark file
# list all apges of content/super pdf
# merge tge watermark page on contennt pages

# write the output

with open('pdf/wtr.pdf', 'rb') as water:
    watermark = PdfFileReader(water)
    water_page = watermark.getPage(0)
    writer = PdfFileWriter()
    # print(watermark.getNumPages())
    with open('pdf/super.pdf', 'rb') as super:
        super_pages = PdfFileReader(super)
        # print(super_pages.getNumPages())
        for i in range(super_pages.getNumPages()):
            page = super_pages.getPage(i)
            # print(page)
            page.mergePage(water_page)
            writer.addPage(page)
        with open('pdf/watermarked.pdf', 'wb') as wm:
            writer.write(wm)
