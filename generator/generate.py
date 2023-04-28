from qrcode import QRCode
from yaml import safe_load as load_yaml
from qrcode.constants import ERROR_CORRECT_L

# loop through file paths for config files (Jess sent two...)
for path in ['./generator/parksJH.yml', './generator/parksJH1.yml']:

    # load config file
    with open(path, 'r') as file:
        parks = load_yaml(file)

    # loop theough each town and park
    for town, park_list in parks.items():
        for park in park_list:

            # init qrcode object
            qr = QRCode(
                version=1,
                error_correction=ERROR_CORRECT_L,
                box_size=50,
                border=4,
            )

            # add data to qr object, 'make' and export to image
            qr.add_data(f"https://qr.huckg.is/{town}/{park}")
            qr.make(fit=True)
            qrcode_im = qr.make_image()
            qrcode_im.save(f"./generator/qr_codes/{town}-{park}.png", 'PNG')