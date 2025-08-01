from pypdf import PdfReader,PdfWriter

with open("sample.pdf",mode='rb') as pdf:
    book = PdfReader(pdf)
    watermark = PdfReader("wtr.pdf").pages[0]
    writer = PdfWriter()
    for page in book.pages:
        page.merge_page(watermark, over=False)
        writer.add_page(page)

    with open("final.pdf",mode='wb') as outpdf:
            writer.write(outpdf)