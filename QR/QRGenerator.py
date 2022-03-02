import qrcode

img = qrcode.make('https://www.youtube.com/channel/UC1ZMZQeel_mTfHQqHBa74-g')
img.save('QRcode.png')
img.show()

