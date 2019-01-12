#Pix2wall
#Python 3.6.2
#script BigБро
#idea Zirum

# example result in result.txt
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\Npcs\New\location.xml

#for npc small box 700321

from PIL import Image

im = Image.open('Minecraft_Schrift_100x130.png','r')
width, height = im.size
pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]

#insert your bottom left start point
x0=1650.4429
y0=1546.7086
z0=150.1266
h0 = 0

# Item size
iw = 0.5 #width
ih = 0.5 #height
il = 0.5 #depth

file = open ('result.txt', 'w')
for h in range (0, height-1):
  for w in range (0, width-1):
    color_black = pix_val_flat[(4*w+h*width*4)] < 50 and pix_val_flat[(4*w+h*width*4)+1] < 50 and pix_val_flat[(4*w+h*width*4)+2] < 50
    if color_black:
     x = x0+w*iw 
     y = y0
     z = z0+(height-h)*ih
     file.write('<spot h="{:d}" x="{:.1f}" y="{:.1f}" z="{:.1f}"/>\n'.format(h0, x, y, z))
file.close()
