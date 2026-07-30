from PIL import Image

def test():
    img = Image.new("P", (10, 10))
    img.putpalette([255, 0, 0, 0, 255, 0, 0, 0, 255] + [0]*(253*3))
    img.info['transparency'] = 0 # index 0 is transparent

    print(img.getpalette()[:9])
    print(img.info)

test()
