##############################################################
# 【参考】
# https://qiita.com/Yuu94/items/9ffdfcb2c26d6b33792e
# https://note.nkmk.me/python-split-rsplit-splitlines-re/
# https://note.nkmk.me/python-listdir-isfile-isdir/
# Pythonで文字画像を作る
# http://kamiya.tech/blog/draw-font/
# PIL（Python Imaging Library）を使って画像ファイルを作成する。(Qiita)
# https://qiita.com/suto3/items/5181b4a3b9ebc206f579

# Author : Hideto Niwa
##############################################################

from PIL import Image, ImageDraw, ImageFont
import os

height = 400
horizontal = 764

#記事タイトル取得
def get_title(file_path):
    print("Open file...",file_path)
    
    f = open(file_path, 'r',encoding="utf-8") #File Open（文字コード指定）
    datalist = f.readlines()
    text=datalist[3] #自分の環境では3行目にtitleが存在するため
    title=text.split('"')
    print(title)
    return title[1]

#ディレクトリ取得
def get_dir(path,num):
    path=os.path('./content/')
    print(path)



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

title=get_title(".\content\post\how_to_hugo_post.md")

make_bace_image(".\static\img\logo.jpg", ".\python\card.png")
make_image(".\python\MPLUSRounded1c-Medium.ttf" ,".\python\card.png", "どと～る ブログ",horizontal*0.75, height*0.4,42)
make_image(".\python\MPLUSRounded1c-Medium.ttf" ,".\python\card.png", title,horizontal*0.75, height*0.53,32)
make_image(".\python\MPLUSRounded1c-Light.ttf" , ".\python\card.png", "https://www.hahahahaha-nnn.work",horizontal*0.75, height*0.62,18)