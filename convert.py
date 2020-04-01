import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pdf = wi(filename = "testfile.pdf", resolution = 300)
pdfImg = pdf.convert('jpeg')

image = []

for i in pdfImg.sequence:
    page = wi(image = i)
    image.append(page.make_blob('jpeg'))

texts = []

for img in image:
    im = Image.open(io.BytesIO(image))
    text = pytesseract.image_to_string(im, lang = 'eng')
    texts.append(text)


for i in range(texts):
    print(texts[i])

    