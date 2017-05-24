##paprotka

from PIL import Image, ImageDraw
im = Image.new('RGBA', (400, 400), (0, 0, 0, 0))
draw = ImageDraw.Draw(im)

poziom=input("Ile poziomow? Maksymalnie 9  ")
xlewy=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
xprawy=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
xgorny=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
ylewy=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
yprawy=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
ygorny=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
a=[0,0,0,0]
b=[0,0,0,0]
c=[0,0,0,0]
e=[0,0,0,0]
d=[0,0,0,0]
f=[0,0,0,0]
lewy=50
w=300
wl=w+lewy
xlewy[poziom]= 0
ylewy[poziom]= 0
xprawy[poziom]= w
yprawy[poziom]= 0
xgorny[poziom]= 0.5*w
ygorny[poziom]= w
a[0]=0.849
a[1]=0.197
a[2]=-0.150
a[3]=0
b[0]=0.037
b[1]=-0.226
b[2]=0.283
b[3]=0
c[0]=-0.037
c[1]=0.226
c[2]=0.260
c[3]=0.0
d[0]=0.849
d[1]=0.197
d[2]=0.237
d[3]=0.160
e[0]=0.075*w
e[1]=0.400*w
e[2]=0.575*w
e[3]=0.500*w
f[0]=0.1830*w
f[1]=0.0490*w
f[2]=-0.0840*w
f[3]=0.0000*w


def prze(poziom,przekszt):
    xlewy[poziom]= a[przekszt]*xlewy[poziom+1]+b[przekszt]*ylewy[poziom+1]+e[przekszt]
    ylewy[poziom]= c[przekszt]*xlewy[poziom+1]+d[przekszt]*ylewy[poziom+1]+f[przekszt]
    xprawy[poziom]= a[przekszt]*xprawy[poziom+1]+b[przekszt]*yprawy[poziom+1]+e[przekszt]
    yprawy[poziom]= c[przekszt]*xprawy[poziom+1]+d[przekszt]*yprawy[poziom+1]+f[przekszt]
    xgorny[poziom]= a[przekszt]*xgorny[poziom+1]+b[przekszt]*ygorny[poziom+1]+e[przekszt]
    ygorny[poziom]= c[przekszt]*xgorny[poziom+1]+d[przekszt]*ygorny[poziom+1]+f[przekszt]

def rekurencja(poziom):
    if(poziom <= 1):
        draw.line((lewy+xlewy[1],wl-ylewy[1], lewy+xprawy[1],wl-yprawy[1]))
        draw.line((lewy+xprawy[1],wl-yprawy[1], lewy+xprawy[1],wl-ygorny[1]))
        draw.line((lewy+xprawy[1],wl-ygorny[1], lewy+xlewy[1],wl-ygorny[1]))
        draw.line((lewy+xlewy[1],wl-ygorny[1], lewy+xlewy[1],wl-ylewy[1]))
    else:
        poziom=poziom-1
        przekszt=0
        prze(poziom,przekszt)
        rekurencja(poziom)
        przekszt=1
        prze(poziom,przekszt)
        rekurencja(poziom)
        przekszt=2
        prze(poziom,przekszt)
        rekurencja(poziom)
        przekszt=3
        prze(poziom,przekszt)
        rekurencja(poziom)

rekurencja(poziom)
im.show()
