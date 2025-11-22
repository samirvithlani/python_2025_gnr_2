def pdfHandler(fileName):
    print(f" {fileName} file open as pdf.")

def docHandler(fileName):
    print(f"{fileName} file open as doc.")
    
def imageHandler(fileName):
    print(f"{fileName} file open as img.")        


def handleFile(cb,fname): #cb == imageHandler
    print("handle file called...")    
    cb(fname) 

#handleFile(imageHandler)    
fileName = "abc.doc"

if fileName.endswith(".jpg"):
    handleFile(imageHandler,fileName)
elif fileName.endswith(".pdf"):
    handleFile(pdfHandler,fileName)    
elif fileName.endswith(".doc"):
    handleFile(docHandler,fileName)    