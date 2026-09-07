from PIL import Image

image = Image.open("./smiley.png").convert("RGBA") #open image file smiley.png, RGBA = red, green, blue, alpha
output_text_file = open("output.txt", "w") #open text file awesome_picture.txt and writes into it
x, y = 0, 0

for x in range(image.width):
    for y in range (image.height): 
        r, g, b, _ = image.getpixel((x,y)) #
        output_text_file.write(f"({r}, {g}, {b})\n")

