import qrcode as qrc
img = qrc.make("https://www.linkedin.com/in/hafiz-siddiqui-018587295/")
print(type(img))
img.save("Hafiz Siddiqui.png")
print("QR code has been generated ")
