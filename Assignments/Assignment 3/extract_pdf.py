import PyPDF2
path=r"c:\Users\ebooz\Downloads\MSSE642_Assignment3_v2.pdf"
reader=PyPDF2.PdfReader(path)
with open(r"c:\Users\ebooz\OneDrive\Desktop\MSSE642-2026Spring\MSSE642-2026Spring\Assignments\Assignment 3\Assignment3.txt","w",encoding="utf-8") as f:
    for i,page in enumerate(reader.pages):
        f.write("--- PAGE %d ---\n" % i)
        f.write(page.extract_text() or "[no text]\n")
print('done')
