def pdfHandler():
    print(f"file open as pdf.")

def docHandler():
    print(f"file open as doc.")
    
def imageHandler():
    print(f"file open as img.")        


def handleFile(cb): #cb == imageHandler
    print("handle file called...")    
    cb() 

#handleFile(imageHandler)    
fileName = "abc.doc"

if fileName.endswith(".jpg"):
    handleFile(imageHandler)
elif fileName.endswith(".pdf"):
    handleFile(pdfHandler)    
elif fileName.endswith(".doc"):
    handleFile(docHandler)    