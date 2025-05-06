import qrcode

website_link = 'https://imageio.readthedocs.io/en/stable/index.html'
qr = qrcode.QRCode(version=1,box_size=5,border=4)
qr.add_data(website_link)
qr.make()
img = qr.make_image(fill_color='black',back_color='white')
img.save('website_qr.png')