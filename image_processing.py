from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

im = Image.open("konjikido_01.jpg")

# print(im.filename)  # ファイル名
# print(im.size)  # サイズ
# print(im.width)  # 幅
# print(im.height)  # 高さ
# print(im.mode)  # モード
# print(im.format)  # フォーマット

im_resized = im.resize((933, 486))
im_resized.save("resized_konjikido_01.jpg")

# 読み込む画像のファイル名
pic_name = "resized_konjikido_01.jpg"
# 挿入する文字列
ins_text = "平泉 最高"
# 文字を配置っするピクセル数を指定（左上が基準）
pos_x = 125
pos_y = 170
# 文字サイズを指定
font_size = 150
# フォントの種類を指定
font_path = "/Users/risunjae121/Library/Fonts/RictyDiminished-Regular.ttf"
# RGBで文字色指定
font_color = (0, 255, 255)
# 処理開始
img = Image.open(pic_name)
font = ImageFont.truetype(font_path, font_size)
ImageDraw.Draw(img).text((pos_x, pos_y), ins_text, font=font, fill=font_color)
img.save("add_text.jpg", quality=100)
