from pypdf import PdfReader, PdfWriter
import sys

#~ Variable / Object Initialization
input_file = sys.argv[1]
reader = PdfReader(input_file)
writer = PdfWriter()
searchQuery = "Homework Problem"
pagesToKeep = []

#~ Check every page for search query
for i in range(len(reader.pages)):
    if(searchQuery in reader.pages[i].extract_text()):
        pagesToKeep.append(i)

#~ Output
print('"' + searchQuery + '" found on pages: ' + str(pagesToKeep))
writer.append(reader, pagesToKeep)
output = open(input_file[:-4] + " HW Only.pdf", "wb")
writer.write(output)