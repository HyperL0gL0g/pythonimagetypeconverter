from PIL import Image

i=Image.open("C:\\Users\\KIIT\\N.jpg").convert("RGBA")
bg=Image.new("RGBA",(20,220),(255,255,255))
x,y=i.size
bg.paste(i, (0,0,x,y), i)
i = i.convert("RGB")
bg.save("g.png",quality=95)
