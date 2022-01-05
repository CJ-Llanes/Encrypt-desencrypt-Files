import qrcode, requests
from io import BytesIO
from PIL import Image

# taking image which user wants
# in the QR code center
def QRgenerator(icon,content):
    logo = Image.open(BytesIO(requests.get(icon).content))

    new_image = Image.new("RGBA", logo.size, "WHITE") # Create a white rgba background
    new_image.paste(logo, (0, 0), logo) # Paste the image on the background
    logo=new_image.convert('RGB')

    # adjust image size
    basewidth = 300 # taking base width
    wpercent = (basewidth/float(logo.size[0]))
    hsize = int((float(logo.size[1])*float(wpercent)))
    logo = logo.resize((int(0.2*logo.size[0]), int(0.2*logo.size[1])), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    # taking url or text/text file
    content_to_QR=open(content, "r").read()
    QRcode.add_data(content_to_QR) # addingg content to QRcode
    QRcode.make() # generating QR code

    QRcolor = 'Black' # taking color name from user
    # adding color to QR code
    QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')

    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)
    QRimg = QRimg.resize((int(basewidth*1.5), int(1.5*hsize)), Image.ANTIALIAS)
    # save the QR code generated
    #QRimg.save('gfg_QR.png')
    return QRimg