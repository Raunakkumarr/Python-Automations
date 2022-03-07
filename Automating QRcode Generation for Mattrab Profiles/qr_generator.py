import csv
import qrcode
from PIL import Image

filename = "profile_links.csv"
logo_file="logo.png"

def generate_qr():
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header=next(csvreader)
        n=0
        #print(header)
        for applicant in csvreader:
            name=applicant[0]
            links=applicant[1]
            logo = Image.open(logo_file)
            basewidth = 100
            wpercent = (basewidth/float(logo.size[0]))
            hsize = int((float(logo.size[1])*float(wpercent)))
            logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
            QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            QRcode.add_data(links)
            QRcode.make()
            QRcolor = '#1d3341'
            QRimg = QRcode.make_image(fill_color=QRcolor, back_color="#eee4d1").convert('RGB')
            pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
            QRimg.paste(logo, pos)
            save_as_name="D:\\Innovation\\Python_Programs\\Python_Automations\\Mattrab\\qr_codes\\qr_img\\"+str(name)+".png"
            QRimg.save(save_as_name)
            n=n+1
            print(f'{n}. QR code generated!')

link='https://www.askmattrab.com/users/54-anish'
logo = Image.open(logo_file)
basewidth = 100
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
QRcode.add_data(link)
QRcode.make()
QRcolor = '#1d3341'
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="#eee4d1").convert('RGB')
pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
save_as_name="D:\\Innovation\\Python_Programs\\Python_Automations\\Mattrab\\qr_codes\\qr_img\\about.png"
QRimg.save(save_as_name)
