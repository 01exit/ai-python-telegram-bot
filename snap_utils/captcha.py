from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from io import BytesIO
import string

def generate_captcha():
    captcha_text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    background_color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
    img = Image.new('RGB', (240, 60), color=background_color)
    d = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("comicbd.ttf", 34)
    except IOError:
        font = ImageFont.load_default()
    text_color = (
        random.randint(0, 150),
        random.randint(0, 150),
        random.randint(0, 150)
    )
    bbox = d.textbbox((0, 0), captcha_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (img.width - text_width) // 2
    y = (img.height - text_height) // 20
    d.text((x, y), captcha_text, font=font, fill=text_color)
    for _ in range(14):
        start = (random.randint(0, 240), random.randint(0, 60))
        end = (random.randint(0, 240), random.randint(0, 60))
        line_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        d.line([start, end], fill=line_color, width=2)
    img = img.filter(ImageFilter.GaussianBlur(2))
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return captcha_text, img_byte_arr
