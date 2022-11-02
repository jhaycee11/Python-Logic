import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("super.pdf")


def pdf_rotate():
    """
    Rotate PDF and save as newfile
    """
    with open("dummy.pdf", 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        page = reader.getPage(0)
        page.rotateCounterClockwise(90)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open("tilt.pdf", "wb") as newfile:
            writer.write(newfile)

def water_mark():
    template = PyPDF2.PdfFileReader(open("super.pdf", "rb"))
    watermark = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open("watermarked_output.pdf", "wb") as file:
            output.write(file)
