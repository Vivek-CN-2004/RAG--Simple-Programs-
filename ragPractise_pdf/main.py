from pypdf import PdfReader

reader = PdfReader("document/Vivek_C_N_Resume.pdf")

print("total  pages",len(reader.pages))

documnet = '' 

for page in reader.pages:
    text = page.extract_text()

    if text:
        documnet += text +'\n'

print(documnet)
print("total number of charcter in document : ", len(documnet))

 
                                               

