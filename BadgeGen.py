from PIL import Image, ImageFont, ImageDraw 
import pathlib
from tkinter import filedialog
import tkinter as tk
import pyperclip

def GenerateBadge():
    def copyHTML():
        ProtocolID=str(Text3.get("1.0",'end-1c'))
        URL=str(Text5.get("1.0",'end-1c'))
        line1="""<div class="DeFiSafetyBadge" align="right";>"""
        line2='<a href="https://www.defisafety.com/pqrs/'+ProtocolID+'">'
        line3='<img src="'+URL+'" alt="DeFiSafetyBadge" style="width:228px;height:76px;"></a></div>'
        CopyTo=line1+line2+line3
        pyperclip.copy(CopyTo)
    localpath=str(pathlib.Path().resolve())
    pathlist=localpath.split('\\')
    newpathlist=[]
    for x in pathlist:
        if x == "Sync":
            break
        newpathlist.append(x)
    localpath="/".join(newpathlist)
    print(localpath)
    path=localpath+"/Sync/PQ Processs Quality Audit/Python Scripts/BadgeGenerator"
    savelocation=filedialog.askdirectory(initialdir=localpath+"/Sync/DeFiSafety Common/Products/Processs Quality Reviews/Reviews - Copy/0.8")
    fontpath=path+"/Lato-Bold.ttf"
    title_text=str(Text1.get("1.0",'end-1c'))
    Score=int(Text2.get("1.0",'end-1c'))
    try: fontsize=int(Text4.get("1.0",'end-1c'))
    except Exception:
        fontsize=""
    newtitlelist=[]
    if Score>=95:
        baseimagepath=path+"/blankgoldbadge.png"
    else:
        baseimagepath=path+"/blankbadge.png"
    if "$$$$" in title_text:
        titlelist=title_text.split("$$$$")
        TitleSize=500
    elif fontsize!="":
        TitleSize=int(fontsize)
        if "$$$$" not in title_text:
            titlelist=[title_text]
    else:
        if len(title_text)>11:
            if " " in title_text:
                titlelist=title_text.split(" ")
                if len(titlelist)<=2:
                    for x in titlelist:
                        if len(x)>11 and len(x)<16:
                            TitleSize=380
                            break
                        if len(x)>11 and len(x)>15:
                            TitleSize=380
                            SliceTitle=[title_text[i:i+14] for i in range(0, len(title_text), 14)]
                            for x in SliceTitle:
                                newtitlelist.append(x+"-")
                            break
                        else:
                            TitleSize=500
                else:
                    TitleSize=380
                    SliceTitle=[title_text[i:i+14] for i in range(0, len(title_text), 14)]
                    for x in SliceTitle:
                        newtitlelist.append(x+"-")
            else:
                TitleSize=380
                SliceTitle=[title_text[i:i+14] for i in range(0, len(title_text), 14)]
                for x in SliceTitle:
                    newtitlelist.append(x+"-")
        else:
            titlelist=[title_text]
            TitleSize=500

    if len(newtitlelist)>0:
        lastelement=newtitlelist[len(newtitlelist)-1]
        titlelist=newtitlelist
        newlastelement=lastelement.rstrip("-")
        titlelist.remove(lastelement)
        titlelist.append(newlastelement)

    if Score==100:
        ScoreSize=750
        y=980
    else:
        ScoreSize=900
        y=850
    Score=str(Score)+"%"
    my_image=Image.open(baseimagepath)
    image_editable = ImageDraw.Draw(my_image)
    counter=0
    for x in titlelist:
        ytitle=15+counter*450
        title_font = ImageFont.truetype(fontpath, TitleSize)
        image_editable.text((2300,ytitle), x, (0, 0, 0), font=title_font)
        counter=counter+1
    title_font = ImageFont.truetype(fontpath, ScoreSize)
    image_editable.text((2300,y), Score, (0, 0, 0), font=title_font)
    my_image.save(savelocation+"/"+title_text+"Badge.png")
    Label5= tk.Label(root,text="1. Upload badge to strapi under upload media (on the left)\n2. then click the link icon over the image to get the URL,\n3.add URL here", height=4, width=60)
    Text5= tk.Text(root, height=1, width=50)
    Label5.place(x=0, y=380)
    Text5.place(x=20, y=460)
    RunButton2= tk.Button(root,text="Copy HTML", height=1, width=8,command=copyHTML)
    RunButton2.place(x=380,y=455)


root= tk.Tk()
root.geometry("500x500")
root.title("Generate Badge")
Label1= tk.Label(root,text="Protocol Name", height=1, width=20)
Label2= tk.Label(root,text="Enter Protocol Score", height=1, width=20)
Label3= tk.Label(root,text="Enter Protocol ID", height=1, width=20)
Label4= tk.Label(root,text="To add line break, write $$$$", height=1, width=40)
Label5= tk.Label(root,text="Font Size (optional)", height=1, width=20)

Text1= tk.Text(root, height=1, width=50)
Text2= tk.Text(root, height=1, width=50)
Text3= tk.Text(root, height=1, width=50)
Text4= tk.Text(root, height=1, width=10)

RunButton= tk.Button(root,text="Generate Badge", height=1, width=10,command=GenerateBadge)

Label1.place(x=0, y=40)
Label2.place(x=0, y=100)
Label3.place(x=0, y=160)
Label4.place(x=0, y=10)
Label5.place(x=140, y=225)

Text1.place(x=20, y=70)
Text2.place(x=20, y=130)
Text3.place(x=20, y=190)
Text4.place(x=300, y=225)


RunButton.place(x=20,y=220)

tk.mainloop()