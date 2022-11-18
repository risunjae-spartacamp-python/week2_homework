import cv2
from PIL import Image

original_face_img = "image/face_img.png"
original_mask_img = "image/eye_img.png"


def find_face():
    # 顔検出の分類器を用意
    cascade_file = "haarcascade_eye.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    img = cv2.imread(original_face_img)
    face_list = cascade.detectMultiScale(img)
    return face_list


def paste_img(face_list):
    x = face_list[0][0]
    y = face_list[0][1]
    w = face_list[0][2]
    h = face_list[0][3]

    right_eye_x = face_list[1][0]
    right_eye_y = face_list[1][1]
    right_eye_w = face_list[1][2]
    right_eye_h = face_list[1][3]
    # face_img = cv2.imread(original_face_img)
    # mask_img = cv2.imread(original_mask_img)

    face_img = Image.open(original_face_img)
    mask_img = Image.open(original_mask_img)
    right_mask_img = Image.open(original_mask_img)

    # resized_mask_img = cv2.resize(
    #     mask_img,
    #     dsize=(
    #         w,
    #         h,
    #     ),
    # )

    resized_mask_img = mask_img.resize(
        (
            w,
            h,
        )
    )

    resized_right_mask_img = right_mask_img.resize(
        (
            right_eye_w,
            right_eye_h,
        )
    )

    # cv2.imwrite("images/resize_otahuku.png", resized_mask_img)
    # resized_mask_img.save("image/resize_eye.png")

    # face_img[y : y + h, x : x + w] = cv2.imread("images/resize_otahuku.png")
    # cv2.imwrite("images/hensin.png", face_img)

    face_img.paste(resized_mask_img, (x, y), resized_mask_img.split()[3])
    face_img.paste(
        resized_right_mask_img,
        (right_eye_x, right_eye_y),
        resized_right_mask_img.split()[3],
    )
    face_img.save("image/hensin_pillow.png")


face_list = find_face()
paste_img(face_list)
