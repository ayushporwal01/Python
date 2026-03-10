from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["./Assets/pc-games.pdf", "./Assets/re4-wiki.pdf"]:
    merger.append(pdf)

merger.write("./Assets/pc-wiki.pdf")


