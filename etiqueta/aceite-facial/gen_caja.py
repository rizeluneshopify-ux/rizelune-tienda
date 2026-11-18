# Caja del aceite facial (plantilla Selfnamed de la caja de 30 ml, igual que la del sérum: 4133×5009 px a 600 ppp).
# Frontal x 2242–3242 px, lateral 3242–4083 px, cuerpo y 1233–3783 px. Texto ≥ 6 pt (50 px).
from PIL import Image, ImageDraw, ImageFont
import math
F='/root/tiendas/dfqp9i-am/etiqueta/fuentes/'
JOST5=F+'fontsource-jost-5.3.0/files/jost-latin-500-normal.woff'
JOST4=F+'fontsource-jost-5.3.0/files/jost-latin-400-normal.woff'
LORA=F+'fontsource-lora-5.3.0/files/lora-latin-400-normal.woff'
LORAI=F+'fontsource-lora-5.3.0/files/lora-latin-400-italic.woff'
DARK=(47,59,46,255); SOFT=(74,90,71,255); ROSA=(190,132,112,255)
W,H=4133,5009; FX0,FX1=2242,3242; SX0,SX1=3242,4083; Y0,Y1=1233,3783

def spaced(d,cx,y,text,font,fill,track):
    w=sum(d.textlength(c,font=font) for c in text)+track*(len(text)-1); x=cx-w/2
    for c in text: d.text((x,y),c,font=font,fill=fill); x+=d.textlength(c,font=font)+track

def crescent(im,cx,cy,r,color):
    # misma luna que el logo (rz-icon «luna-logo»): disco R menos disco 0,833R desplazado (0,765R, −0,41R)
    s=4*r; m=Image.new('L',(s,s),0); md=ImageDraw.Draw(m); c=2*r
    md.ellipse((c-r,c-r,c+r,c+r),fill=255)
    ix,iy,ir=c+0.765*r,c-0.41*r,0.833*r
    md.ellipse((ix-ir,iy-ir,ix+ir,iy+ir),fill=0)
    im.paste(Image.new('RGBA',(s,s),color),(int(cx-c),int(cy-c)),m)

def phase(d,cx,cy,r,k,color,lw):
    # k: 0 nueva, 1 creciente, 2 cuarto, 3 gibosa, 4 llena
    d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=color,width=lw)
    if k==4: d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=color)
    elif k==2: d.pieslice((cx-r,cy-r,cx+r,cy+r),-90,90,fill=color)
    elif k in (1,3):
        tmp=Image.new('L',(4*r,4*r),0); t=ImageDraw.Draw(tmp)
        t.ellipse((r,r,3*r,3*r),fill=255)
        if k==1: t.ellipse((r-int(0.5*r),r,3*r-int(0.5*r),3*r),fill=0)
        else:
            t.rectangle((r,r,2*r,3*r),fill=0); t.ellipse((r+int(0.45*r),r,3*r-int(0.45*r),3*r),fill=255)
        d._image.paste(Image.new('RGBA',tmp.size,color),(cx-2*r,cy-2*r),tmp)

def build():
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); cx=(FX0+FX1)//2
    # 1) luna grande «rosa mosqueta»
    crescent(im,cx-20,Y0+600,200,ROSA)
    # 2) marca
    fbig=ImageFont.truetype(LORA,150); bb=d.textbbox((0,0),'rizelune',font=fbig)
    d.text((cx-(bb[2]-bb[0])/2-bb[0],Y0+940-bb[1]),'rizelune',font=fbig,fill=DARK)
    # 3) nombre del producto
    fcap=ImageFont.truetype(JOST5,62); y=Y0+1500
    for t in ['ACEITE FACIAL','CON BAKUCHIOL']: spaced(d,cx,y,t,fcap,SOFT,14); y+=86
    y+=40; d.line((cx-70,y,cx+70,y),fill=SOFT,width=5); y+=48
    fit=ImageFont.truetype(LORAI,74); t='Bakuchiol & rosa mosqueta'; bb=d.textbbox((0,0),t,font=fit)
    d.text((cx-(bb[2]-bb[0])/2-bb[0],y-bb[1]),t,font=fit,fill=DARK); y+=(bb[3]-bb[1])+44
    spaced(d,cx,y,'30 ml · 1.01 fl oz',ImageFont.truetype(JOST4,56),SOFT,8)
    # 4) fases de la luna
    r=34; gap=150; yy=Y1-260
    for i,k in enumerate([0,1,2,3,4]): phase(d,cx+(i-2)*gap,yy,r,k,DARK,6)
    # 5) lateral: texto vertical + lunita
    side=Image.new('RGBA',(Y1-Y0,SX1-SX0),(0,0,0,0)); sd=ImageDraw.Draw(side)
    fs=ImageFont.truetype(LORAI,92); t='rizelune  ·  ritual facial con bakuchiol'; bb=sd.textbbox((0,0),t,font=fs)
    sd.text(((side.width-(bb[2]-bb[0]))/2-bb[0],(side.height-(bb[3]-bb[1]))/2-bb[1]),t,font=fs,fill=SOFT)
    side=side.rotate(90,expand=True); im.paste(side,(SX0,Y0),side)
    crescent(im,(SX0+SX1)//2,Y0+170,40,ROSA)
    return im

if __name__=='__main__':
    im=build(); im.save('rizelune-caja-aceite-facial.png')
    # vista previa sobre crema (frontal + lateral)
    bg=Image.new('RGB',(W,H),(237,228,214)); bg.paste(im,(0,0),im)
    d=ImageDraw.Draw(bg)
    for x in (FX0,FX1,SX1): d.line((x,Y0,x,Y1),fill=(200,190,175),width=4)
    d.line((FX0,Y0,SX1,Y0),fill=(200,190,175),width=4); d.line((FX0,Y1,SX1,Y1),fill=(200,190,175),width=4)
    v=bg.crop((FX0-150,Y0-150,SX1+150,Y1+150)); v.thumbnail((900,1200)); v.save('vista-caja-aceite-facial.png')
