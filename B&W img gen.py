from PIL import Image


img = Image.open("your_file_name.jpeg").convert("L")  


threshold = 128
bw = img.point(lambda x: 255 if x > threshold else 0, '1')


bw.save("bw_output.png")
