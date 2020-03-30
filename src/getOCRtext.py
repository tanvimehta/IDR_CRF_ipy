import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

image = "../datasets/SplitYB.png"
im = Image.open(image) 
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.jpg')
text = pytesseract.image_to_string(Image.open('temp2.jpg'))
print(text)
