from PIL import Image as PilImage
import glob, os
import re
def getListImage(path):
    """Đối sô là một đường dẫn thư mục chứa file ảnh.
    Trả về một danh sách đường dẫn các file ảnh""" 
    filePaths = glob.glob(path)
    formatImage = [".png", ".jpg", ".jpeg", ".gif", ".bmp"]
    listOfImages = []
    for item in formatImage:
        for filePath in filePaths:
            if item in filePath:
                listOfImages.append(filePath)
    return listOfImages
    
def getNameImage(imagePath):
    """Đối số là đường dẫn ảnh.
    Trả về tên cùng định dạng từ đường dẫn ảnh"""
    regex = r'[^\\:*?"<>|\r\n]+$'
    name = re.search(regex, imagePath).group(0)
    return name

def makeName(imagePath):
    """Đối số là đường dẫn ảnh.
    Trả về tên cùng định dạng png"""
    name = getNameImage(imagePath)
    for i in range(len(name)):
        if name[i] == "." :
            makeName = name[:i] + "Convert" + ".png"
    return makeName

def convertSizeImage(imagePath, widthConvert = 512):
    """Đối số là một đường dẫn ảnh. widthConvert = 512px là mặc định.
    Nếu width > 512px, thu bé width về 512px, trả về 1.
    Nếu ảnh có định dạng khác png, convert ảnh về png.
    Nếu width ảnh < 512px, trả về 0.
    """ 
    image = PilImage.open(imagePath).convert("RGB")
    width, height = image.size
    if width < widthConvert:
        if ".png" in getNameImage(imagePath):
            print(getNameImage(imagePath) + " SIZE " + str(image.size))
        else:
            image.save(makeName(imagePath))
            print(getNameImage(imagePath) + " SIZE " + str(image.size) + " --> " + makeName(imagePath))
        return 0
    scale = widthConvert/width
    newHeight = int(height*scale)
    newSizeImage = (widthConvert, newHeight)
    newImage = image.resize(newSizeImage)
    newImage.save(makeName(imagePath))
    print("CONVERT " + getNameImage(imagePath) + " " + str(image.size) + " --> " + str(newImage.size))
    return 1
PATH = "/*.*"
myList = getListImage(PATH)
for item in myList:
    convertSizeImage(item)