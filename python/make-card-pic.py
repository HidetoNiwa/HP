##############################################################
# 【参考】
# Pythonで文字画像を作る
# http://kamiya.tech/blog/draw-font/
# PIL（Python Imaging Library）を使って画像ファイルを作成する。(Qiita)
# https://qiita.com/suto3/items/5181b4a3b9ebc206f579

# Author : Hideto Niwa
##############################################################

from PIL import Image, ImageDraw, ImageFont

height = 400
horizontal = 764

#文字未入れ状態の画像作成
def make_bace_image(logo_path,img_path):
    tmp = Image.new('RGB', (horizontal, height), (0xFF, 0xFF, 0xFF)) # dummy for get text_size
    logo = Image.open(logo_path)

    save_img=tmp.copy()
    save_img.paste(logo)
    save_img.save(img_path)

#文字入れ部分
def make_image(font_path, img_path,text,x=0.0 ,y=0.0, font_size=32, font_color="black"):
    font = ImageFont.truetype(font_path, font_size)
    img=Image.open(img_path)
    
    img_d = ImageDraw.Draw(img)
    text_size = img_d.textsize(text, font) #テキストサイズの取得

    img_d.text((x-(text_size[0]/2),y-(text_size[1]/2)), text, fill=font_color, font=font)
    img.save(img_path)

make_bace_image(".\static\img\logo.jpg", ".\python\card.png")
make_image(".\python\MPLUSRounded1c-Medium.ttf" ,".\python\card.png", "どと～る ブログ",horizontal*0.75, height*0.45,38)
make_image(".\python\MPLUSRounded1c-Light.ttf" , ".\python\card.png", "https://www.hahahahaha-nnn.work",horizontal*0.75, height*0.55,18)