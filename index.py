import re
from PIL import Image
import pyocr
import cv2
import datetime
import csv

tools = pyocr.get_available_tools()
tool = tools[0]

# print(tool)
# print(tool.get_name())

img1 = Image.open("01.png")
img2 = Image.open("02.png")
img3 = Image.open("03.png")
img4 = Image.open("04.png")
img5 = Image.open("05.png")


txt1 = tool.image_to_string(img1, lang="eng+jpn", builder=pyocr.builders.TextBuilder())
txt2 = tool.image_to_string(img2, lang="eng+jpn", builder=pyocr.builders.DigitBuilder())
txt4 = tool.image_to_string(img4, lang="eng+jpn", builder=pyocr.builders.TextBuilder())
txt5 = tool.image_to_string(img5, lang="eng+jpn", builder=pyocr.builders.DigitBuilder())

filename = "03.png"
img = cv2.imread(filename, 0)  # グレースケールで読み込む

cv2.imwrite(filename.split(".")[0] + "03_gray.jpg", img)

img6 = Image.open("03_gray.jpg")
txt3 = tool.image_to_string(img6, lang="eng+jpn", builder=pyocr.builders.DigitBuilder())

result4 = re.sub(r"\D", "", txt4)
# print(txt1)
# print(txt2)
# print(txt3)
# print(result4)
# print(txt5)

result1 = re.sub(r"\D", "", txt1)
# print(result1)

path = "01.png"
img = cv2.imread(path)
# print(img.shape)  # 結果:(39, 370, 3)

# 切り取り範囲の指定
im = Image.open(path)  # 画像を開く
cropped = im.crop((100, 0, 300, 150))  # 左上0px, 右下100pxでトリミング
cropped.save("out0.png")  # トリミングした画像を保存

img7 = Image.open("out0.png")
txt1 = tool.image_to_string(img7, lang="eng+jpn", builder=pyocr.builders.TextBuilder())
# print(txt1)

total_kcal = (int)(txt1) + (int)(txt2) + (int)(txt3) + (int)(result4) + (int)(txt5)
today1 = datetime.date.today()
today2 = "{0:%Y/%m/%d}".format(today1)
# print(today1)
# print(today2)
print(today2 + "の摂取カロリーは" + (str)(total_kcal) + "kcalです。")

# テキスト形式
text = (str)(total_kcal)
file = open("test1.txt", "w")
file.write(text)
file.close()

# CSV形式
f = open("out.csv", "w")
data = [total_kcal]
writer = csv.writer(f)
writer.writerow(data)
f.close()
