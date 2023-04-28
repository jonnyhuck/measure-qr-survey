from qrcode import QRCode
from pandas import read_excel
from qrcode.constants import ERROR_CORRECT_L

# load spreadsheet
parks = read_excel('generator/QR_codes_Park_names.xlsx')

# loop through spreadsheet
for id, row in parks.iterrows():

    # init qrcode object
    qr = QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=50,
        border=4,
    )

    # add data to qr object, 'make' and export to image
    qr.add_data(f"http://qr.huckg.is/{row.town}/{row['site.name']}")
    qr.make(fit=True)
    qrcode_im = qr.make_image()
    qrcode_im.save(f"./generator/qr_codes/{row.town}-{row['site.name']}.png", 'PNG')