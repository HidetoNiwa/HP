##############################################################
# 【参考】
# https://note.nkmk.me/python-glob-usage/
# https://qiita.com/Yuu94/items/9ffdfcb2c26d6b33792e
# https://note.nkmk.me/python-split-rsplit-splitlines-re/
# Pythonで文字画像を作る
# http://kamiya.tech/blog/draw-font/
# PIL（Python Imaging Library）を使って画像ファイルを作成する。(Qiita)
# https://qiita.com/suto3/items/5181b4a3b9ebc206f579
# 同一要素の削除
# https://ja.stackoverflow.com/questions/21070/Pythonで1次元のリストを比較し-同一の要素の削除について
# Pythonでの文字列抽出
# https://note.nkmk.me/python-str-extract/

# Author : Hideto Niwa
##############################################################

from PIL import Image, ImageDraw, ImageFont
import glob
import re

height = 400
horizontal = 764

ignore_list = {"./content\\privacy.md", "./content\\terms.md","./content\\authors\\niwa\\_index.md","./content\\home\\about.md","./content\\home\\index.md","./content\\home\\posts.md","./content\\home\\skills.md","./content\\post\\_index.md","./content\\publication\\_index.md","./content\\talk\\_index.md"}

# 記事タイトル取得

def get_title(file_path):
    print("Open file...", file_path)

    f = open(file_path, 'r', encoding="utf-8")  # File Open（文字コード指定）
    datalist = f.readlines()
    text = datalist[3]  # 自分の環境では3行目にtitleが存在するため
    title = text.split('"')
    print(title)
    return title[1]

# ディレクトリ取得
def get_dir():
    path = './content/**/*.md'
    file_list = glob.glob(path, recursive=True)
    file_list = list(filter(lambda x: x not in ignore_list, file_list))
    print(file_list)
    return file_list

# 文字未入れ状態の画像作成
def make_bace_image(logo_path, img_path):
    tmp = Image.new('RGB', (horizontal, height),
                    (0xFF, 0xFF, 0xFF))  # dummy for get text_size
    logo = Image.open(logo_path)

    save_img = tmp.copy()
    save_img.paste(logo)
    save_img.save(img_path)

# 文字入れ部分
def make_image(font_path, img_path, text, x=0.0, y=0.0, font_size=32, font_color="black"):
    font = ImageFont.truetype(font_path, font_size)
    img = Image.open(img_path)

    img_d = ImageDraw.Draw(img)
    text_size = img_d.textsize(text, font)  # テキストサイズの取得

    img_d.text((x-(text_size[0]/2), y-(text_size[1]/2)),
               text, fill=font_color, font=font)
    img.save(img_path)

# カードのdir情報を追加する部分
def add_card_pic_data(file_path,card_path):
    add_line=14 #追加する行数指定

    file=open(file_path,'r',encoding="utf-8")
    line=file.readline()
    count=1

    while line:
        if count==add_line:
            print(line)
            card_path=card_path[8:]
            add_text='featured_image: .'+card_path
            print(add_text)
        line=file.readline()
        count+=1
    #print(card_path)

file_list = get_dir()

for i in file_list:
    print(i, "...")
    title = get_title(i)
    save_pic_filename=i[9:]
    save_pic_filename=save_pic_filename[:-3]
    #print(save_pic_filename)

    save_pic_dir='.\static\img\card'+save_pic_filename+'.png'

    #print(save_pic_dir)

    make_bace_image(".\static\img\logo.jpg", save_pic_dir)
    make_image(".\python\MPLUSRounded1c-Medium.ttf" ,save_pic_dir, "どと～る ブログ",horizontal*0.75, height*0.4,42)
    make_image(".\python\MPLUSRounded1c-Medium.ttf" ,save_pic_dir, title,horizontal*0.75, height*0.53,32)
    make_image(".\python\MPLUSRounded1c-Light.ttf" , save_pic_dir, "https://www.hahahahaha-nnn.work",horizontal*0.75, height*0.62,18)
    print(i)
    add_card_pic_data(i,save_pic_dir)
