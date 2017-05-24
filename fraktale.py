#trojkat_sierpinskiego
from PIL import Image, ImageDraw
im = Image.new('RGBA', (400, 400), (0, 0, 0, 0))
draw = ImageDraw.Draw(im)

poziom=input("Ile poziomow? Maksymalnie 9  ")
xlewy=[1,1,1,1,1,1,1,1,1,1]
xprawy=[1,1,1,1,1,1,1,1,1,1]
xgorny=[1,1,1,1,1,1,1,1,1,1]
ylewy=[1,1,1,1,1,1,1,1,1,1]
yprawy=[1,1,1,1,1,1,1,1,1,1]
ygorny=[1,1,1,1,1,1,1,1,1,1]
a=[0,0,0]
b=[0,0,0]
c=[0,0,0]
e=[0,0,0]
d=[0,0,0]
f=[0,0,0]
lewy=30
w=300
wl=w+lewy
xlewy[poziom]= 0
ylewy[poziom]= 0
xprawy[poziom]= w
yprawy[poziom]= 0
xgorny[poziom]= 0.5*w
ygorny[poziom]= w
a[0]=0.5
a[1]=0.5
a[2]=0.5
d[0]=0.5
d[1]=0.5
d[2]=0.5
e[0]=0
e[1]=0.5*w
e[2]=0.25*w
f[0]=0
f[1]=0
f[2]=0.5*w

def prze(poziom,przekszt):
    xlewy[poziom]= a[przekszt]*xlewy[poziom+1]+e[przekszt]
    ylewy[poziom]= d[przekszt]*ylewy[poziom+1]+f[przekszt]
    xprawy[poziom]= a[przekszt]*xprawy[poziom+1]+e[przekszt]
    yprawy[poziom]= d[przekszt]*yprawy[poziom+1]+f[przekszt]
    xgorny[poziom]= a[przekszt]*xgorny[poziom+1]+e[przekszt]
    ygorny[poziom]= d[przekszt]*ygorny[poziom+1]+f[przekszt]

def rekurencja(poziom):
    if(poziom <= 1):
        draw.line((lewy+xlewy[1],wl-ylewy[1], lewy+xprawy[1],wl-yprawy[1]))
        draw.line((lewy+xprawy[1],wl-yprawy[1], lewy+xgorny[1],wl-ygorny[1]))
        draw.line((lewy+xgorny[1],wl-ygorny[1], lewy+xlewy[1],wl-ylewy[1]))
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

rekurencja(poziom)
im.show()
