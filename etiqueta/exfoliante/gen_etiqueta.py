# Etiqueta frontal del exfoliante (mismo estilo que la del sérum: Jost en mayúsculas espaciadas, luna, «rizelune» en Lora, Lora cursiva).
from PIL import Image, ImageDraw, ImageFont
import sys
F='/root/tiendas/dfqp9i-am/etiqueta/fuentes/'
JOST5=F+'fontsource-jost-5.3.0/files/jost-latin-500-normal.woff'
JOST4=F+'fontsource-jost-5.3.0/files/jost-latin-400-normal.woff'
LORA=F+'fontsource-lora-5.3.0/files/lora-latin-400-normal.woff'
LORAI=F+'fontsource-lora-5.3.0/files/lora-latin-400-italic.woff'
DARK=(47,59,46,255); SOFT=(94,106,91,255)

def spaced(d, cx, y, text, font, fill, track):
    w=sum(d.textlength(ch,font=font) for ch in text)+track*(len(text)-1)
    x=cx-w/2
    for ch in text:
        d.text((x,y),ch,font=font,fill=fill); x+=d.textlength(ch,font=font)+track

def build(lines_top, sub, size, s=1.12, W=3600, H=1300, big=205):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im); cx=W/2
    fcap=ImageFont.truetype(JOST5,int(48*s)); fbig=ImageFont.truetype(LORA,int(big*s))
    fit=ImageFont.truetype(LORAI,int(68*s)); fsz=ImageFont.truetype(JOST4,int(42*s))
    y=int(60*s)
    for t in lines_top:
        spaced(d,cx,y,t,fcap,SOFT,int(10*s)); y+=int(62*s)
    y+=int(46*s)
    r=int(42*s); my=y+r
    moon=Image.new('L',(4*r,4*r),0); md=ImageDraw.Draw(moon)
    md.ellipse((r,r,3*r,3*r),fill=255)
    md.ellipse((r+int(0.62*r),r-int(0.28*r),3*r+int(0.62*r),3*r-int(0.28*r)),fill=0)
    im.paste(Image.new('RGBA',moon.size,DARK),(int(cx-2*r),int(my-2*r)),moon)
    y=my+r+int(62*s)
    bb=d.textbbox((0,0),'rizelune',font=fbig)
    d.text((cx-(bb[2]-bb[0])/2-bb[0], y-bb[1]),'rizelune',font=fbig,fill=DARK); y+=(bb[3]-bb[1])+int(62*s)
    d.line((cx-int(60*s),y,cx+int(60*s),y),fill=SOFT,width=max(3,int(3*s))); y+=int(45*s)
    bb=d.textbbox((0,0),sub,font=fit); d.text((cx-(bb[2]-bb[0])/2-bb[0],y-bb[1]),sub,font=fit,fill=DARK); y+=(bb[3]-bb[1])+int(55*s)
    spaced(d,cx,y,size,fsz,SOFT,int(6*s))
    box=im.getbbox(); pad=60
    return im.crop((box[0]-pad,box[1]-pad,box[2]+pad,box[3]+pad))

if __name__=='__main__':
    out=sys.argv[1]
    im=build(['EXFOLIANTE CAPILAR','DE ROMERO'],'Romero & menta','170 ml · 5.75 fl oz')
    im.save(out); print(im.size)
