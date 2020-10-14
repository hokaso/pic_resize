from PIL import Image

image_path = "123.jpg"
max_line = 4000
image = Image.open(image_path)
long_side = None
short_side = None
flag = None
if image.width >= max_line and image.height >= max_line:
    pass
# 这个图片太宽了
elif image.width >= max_line:
    long_side = image.width
    short_side = image.height
    flag = 1
# 这个图片太高了
elif image.height >= max_line:
    long_side = image.height
    short_side = image.width
    flag = 2
if long_side:
    clip = long_side // max_line
    flow = long_side % max_line
    new_pic_long = max_line
    new_pic_short = (clip + 1) * short_side
    if flag == 2:
        target = Image.new('RGB', (new_pic_short, new_pic_long),(255, 255, 255))
        for i in range(1, clip + 1):
            image_temp = image.crop((0, (i - 1) * max_line, short_side, i * max_line))
            target.paste(image_temp, (0, (i - 1) * max_line, short_side * i, max_line))
        image_temp = image.crop((0, long_side - flow, short_side, long_side))
        target.paste(image_temp, (short_side, 0, new_pic_short, flow))
    else:
        target = Image.new('RGB', (new_pic_long, new_pic_short))
        for i in range(1, clip + 1):
            image_temp = image.crop(((i - 1) * max_line, 0, i * max_line, short_side))
            target.paste(image_temp, ((i - 1) * max_line, 0, max_line, short_side * i))
        image_temp = image.crop((long_side - flow, 0, long_side, short_side))
        target.paste(image_temp, (0, short_side, flow, new_pic_short))

    target.save('result.jpg', quality=100)
