from PIL import Image

i=Image.open("FILE.jpg").convert("RGBA")
#CONVERTING TO RGBA IS OPTIONAL ,BUT IS RECOMMENDED TO AVOID MASKING ERRORS WITH LARGE FILES
bg=Image.new("RGBA",(20,220),(255,255,255))
x,y=i.size
bg.paste(i, (0,0,x,y), i)
i = i.convert("RGB")
bg.save("FILE.png",quality=95)
