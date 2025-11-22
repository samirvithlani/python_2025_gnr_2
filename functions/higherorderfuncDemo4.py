def pdfHandler(fileName):
    print(f" {fileName} file open as pdf.")
    return True

def docHandler(fileName):
    print(f"{fileName} file open as doc.")
    return True
    
def imageHandler(fileName):
    print(f"{fileName} file open as img.")        
    return True


def handleFile(cb,fname): #cb == imageHandler
    print("handle file called...")    
    x = cb(fname) 
    #print(x)
    return x

#handleFile(imageHandler)    
fileName = "abc.doc"
status = None
if fileName.endswith(".jpg"):
    status = handleFile(imageHandler,fileName)
elif fileName.endswith(".pdf"):
    status = handleFile(pdfHandler,fileName)    
elif fileName.endswith(".doc"):
    status = handleFile(docHandler,fileName)    

print(status)    