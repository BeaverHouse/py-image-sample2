import cv2

def process_image(image):
    img_obj = cv2.imread(image)

    _,w,_= img_obj.shape

    blue = (255, 0, 0)
    font = cv2.FONT_ITALIC
    text_value = "SHIFTONE"

    textSize = cv2.getTextSize(
        text=text_value, 
        fontFace=font, 
        fontScale=2, 
        thickness=8
    )
    
    return cv2.putText(
        img_obj, 
        org=(w - textSize[0][0] - 10, 10 + textSize[0][1]),
        text=text_value, 
        fontFace=font, 
        fontScale=2, 
        color=blue, 
        thickness=8
    )