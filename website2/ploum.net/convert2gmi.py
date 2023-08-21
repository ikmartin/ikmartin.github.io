import sys
import os
sys.path.append("../md2gemini")
import shutil
from md2gemini import md2gemini
from pathlib import Path
import html
import unicodedata
import urllib


mdsource = "/home/ploum/archives/oldblog"
filesource = "/home/ploum/gandi_backup_202210119/vhosts/ploum.net/htdocs"
filedest = "/home/ploum/dev/gemlog"

def convertlink(inlink):
    localfolder = ""
    writtenlink = ""
    if inlink.startswith("http://ploum.net") or inlink.startswith("https://ploum.net"):
        inlink = inlink.removeprefix("http://ploum.net").removeprefix("https://ploum.net")
    if not inlink.startswith("http"):
        if inlink.startswith("/post/"):
            inlink = inlink.removeprefix("/post")
        elif inlink.startswith("/public/"):
            inlink = "/wp-content/uploads/" + inlink.removeprefix("/public/")
        elif inlink.startswith("/images/"):
            inlink = "/wp-content/uploads/" + inlink.removeprefix("/images/")
        elif inlink.startswith("../uploads"):
            inlink = "/wp-content/" + inlink.removeprefix("../")
        if inlink.startswith("wp-content/") \
                                or inlink.startswith("/wp-content/"):
            inlink = inlink.removeprefix("/")
            inlink = urllib.parse.unquote(inlink)
            p = Path(filesource + "/" + inlink)
            inlink = "../files/old/" + inlink.removeprefix("wp-content/uploads/")
            if p.exists():
                dest = Path(filedest + inlink[2:])
                print("copying %s file to %s"%(p,dest))
                if not dest.exists():
                    if not dest.parent.exists():
                        os.makedirs(dest.parent)
                    shutil.move(p,dest)

    elif "ploum" in inlink or "plus.google.com" in inlink:
        if "medium.com" in inlink or "facebook.com" in inlink or "twitter.com" in inlink or\
                "patreon.com" in inlink or "last.fm" in inlink or "tipeee.com" in inlink or\
                "klout.com" in inlink or "flattr.com" in inlink or "app.net" in inlink or\
                "500px.com" in inlink or "instagram.com" in inlink or "changetip.com" in inlink or\
                "linkedin.com" in inlink or "getpocket.com" in inlink or "tip.me" in inlink or\
                "lastfm.fr" in inlink or "plus.google.com" in inlink:
            inlink = "/no-proprietary-service.html"
    return inlink

pngs = 0
jpgs = 0
noh = 0
other = 0
#print(mdsource)
testfile = "interdire-le-port-du-voile-est-il-une-discrimination.md"
testlist = [testfile]
#print(testlist)
#for md_file in testlist:
for md_file in os.listdir(mdsource):
    title = ""
    date = ""
    permalink = ""
    text = ""
    tag = []
    lang = "fr"
    image = None
    with open(mdsource + "/" + md_file) as f:
        md = html.unescape(f.read())
        md = unicodedata.normalize('NFC', md)
        md = md.replace("</div>","\n")
        md = md.replace("<figcaption>"," ")
        md = md.replace("</figcaption>","\n")
        md = md.replace("<figure class=\"aligncenter size-large is-resized\">","")
        md = md.replace("<figure class=\"aligncenter size-large\">","")
        md = md.replace("<figure class=\"aligncenter is-resized\">","")
        md = md.replace("<figure class=\"aligncenter\">","")
        md = md.replace("<figure class=\"aligncenter size-full\">","")
        md = md.replace("<figure class=\"wp-block-image\">","")
        md = md.replace("<figure class=\"wp-block-image size-large\">","")
        md = md.replace("<figure class=\"wp-container-2 wp-block-gallery-1 wp-block-gallery columns-2 is-cropped\">","")
        md = md.replace("</figure>","\n")
        md = md.replace("<div class=\"wp-block-image\">","")
        md = md.replace("<div class=\"footnotes\">","")
        md = md.replace("</div>","\n")
        if "<figure class" in md:
            print("figure class in %s"%md_file)
            print(md)
        if "<div class=\"" in md:
            print("div class in %s"%md_file)
            if "politique-a-olln" in md_file:
                print(md)
        f.close()
        header = md.split("---")[1].split("\n")
    intag = False
    for line in header:
        if intag:
            if line.strip().startswith("-"):
                tag.append(line.strip(" -"))
            else:
                intag = False
        if line.startswith("title:"):
            title = html.unescape(line.removeprefix("title:").strip("\" '")).replace("\_"," ")
        elif line.startswith("date"):
            date = line.removeprefix("date: ").strip("\' ").split("T")[0]
        elif line.startswith("permalink:"):
            permalink = line.removeprefix("permalink: /").strip(" ")
        elif line.startswith("tag"):
            intag = True
        elif line.startswith("thumbnail:"):
            image = line.removeprefix("thumbnail: ../uploads/").strip()
            image_folder = filesource + "/wp-content/uploads/"
            image = image.replace("-150x150","")
            p = Path(image_folder+image)
            if p.exists():
                dest = Path(filedest + "/files/old/"+image)
                print("copying %s to %s"%(p,dest))
                if not dest.parent.exists():
                    os.makedirs(dest.parent)
                shutil.move(p,dest)

    if "EN" in tag or "en" in tag:
        lang = "en"
  
    path = "%s/old/%s-%s.gmi"%(lang,date,permalink)
    text = md2gemini(md,links="copy",img_tag="",plain=True,strip_html=True,\
           frontmatter=True,link_func=convertlink).replace("\r","")
    #We will now try to identify doublelinks (when an image was linking to itself)
    # and remove those
    lines = text.split("\n")
    newtext = ""
    previousimg = None
    previous = None
    def get_imagename(link):
        imagename = None
        if link.startswith("=> "):
            link = link.split(" ")[1]
            if link.endswith(".jpg") or link.endswith(".png") or link.endswith(".gif"):
                imagename = link[:-4]
            elif link.endswith(".jpeg"):
                imagename = link[:-5]
        if imagename:
            imagename = urllib.parse.unquote(imagename)
        return imagename
    for l in lines:
        if l.startswith("=> ../files/old"):
            imagename = get_imagename(l)
            if previousimg and imagename and (previousimg in imagename or imagename in previousimg):
                #print("skip link %s" %l)
                pass
            else:
                previousimg = imagename
                if imagename:
                    extension = l.split()[1].split(".")[-1]
                    pathimg = Path(filedest+imagename[2:]+"."+extension)
                    if not pathimg.exists():
                        print("not imported in %s yet : %s" %(path,pathimg))
                newtext += l + "\n"
        ## detecting other double links
        elif l.startswith("=> ") and not "no-proprietary-service" in l:
            if previous and l.split()[1] == previous.split()[1]:
                #print("%s : skip   link   %s" %(date,l))
                pass
            else:
                previous = l
                newtext += l + "\n"
        else:
            newtext += l + "\n"

    final = "# %s\n" %title
    if image:
        final += "=> files/old/%s\n"%image
    final += "\n"
    final += newtext
    #print(final)
    with open(path,mode="w") as f:
        f.write(final)
        f.close()
