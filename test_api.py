from pixel_workbench import Workbench
from PIL import Image
import os

img = Image.new("P", (10, 10))
img.putpalette([255, 0, 0, 0, 255, 0, 0, 0, 255] + [0]*759)
img.save("test_wb.png")

wb = Workbench()
wb.open("test_wb.png")
wb.paint_index(0, 0, 1)
assert wb.document.image.getpixel((0,0)) == 1

wb.undo()
assert wb.document.image.getpixel((0,0)) == 0

wb.redo()
assert wb.document.image.getpixel((0,0)) == 1

wb.replace_color("#FF0000", "#FFFF00")
pal = wb.document.image.getpalette()
assert pal[0:3] == [255, 255, 0]

os.remove("test_wb.png")
print("Workbench API tests passed!")
