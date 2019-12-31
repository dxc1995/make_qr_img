import qrcode
from PIL import Image
import os, sys
def gen_qrcode(string, path, logo=""):
    """
     生成中间带有logo的二维码
     需要安装qrcode'PIL库
     @参数string:二维码字符串
     @path：生成二维码保存路径
     @logo:logo文件路径
    """
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=1
    )

    qr.add_data(string)
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")
    if logo and os.path.exists(logo):
        try:
            icon = Image.open(logo)
            img_w, img_h = img.size
        except Exception as e:
            print(e)
            sys.exit(1)
        factor = 4
        # 计算logo的尺寸
        size_w = int(img_w/factor)
        size_h = int(img_h/factor)
        # 比较并重新设置logo文件的尺寸
        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon=icon.resize((icon_w, icon_h), Image.ANTIALIAS)
        # 计算logo的位置,并复制到二维码图像中
        w = int((img_w-icon_w)/2)
        h = int((img_h-icon_h)/2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w,h), icon)
        # 保存二维码
        img.save(path)

if __name__ == "__main__":
    info = input("输入转成二维码的网址: ")
    pic_path = input("二维码保存路径: ")
    logo_path = input("logo文件路径: ")
    
    gen_qrcode(info, pic_path, logo_path)
    