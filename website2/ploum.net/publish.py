#!/bin/python
# TODO : links should all be absolute, never relative
import sys
import os
from pathlib import Path
# used to escape the content
import html
# used to produce the time
from datetime import datetime
import textwrap
import unicodedata

global_title = "Ploum.net"
global_subtitle = "le blog de Lionel Dricot"
htmldir="../public_html"
today = datetime.today().strftime("%Y-%m-%d")

geminidir = "../public_gemini"
base_url = "ploum.net/"
local_url = "/home/ploum/dev/gemlog/"
short_limit = 25
maxwidth = 72
old_post_url = ["2005-01-25","2013-05-17","2011-02-07","2012-03-19","2012-01-18","2012-10-15"]

html_page_template = "page_template.html"
email_template = "email_template.html"
gemini_page_template = "page_template.gmi"
# Add the html version to the post dictionnary
# Also convert locals links that ends .gmi to .html
# if index = true, a special style is applied before the first subtitle
def gmi2html(raw,index=False,signature=None,relative_links=True,local=False):
    lines = raw.split("\n")
    inquote = False
    inpre = False
    inul = False
    inindex = index
    def sanitize(line):
        line = unicodedata.normalize('NFC', line)
        return html.escape(line)
    content = ""
    title = ""
    if inindex:
        content += "<div class=\"abstract\">\n"
    for line in lines:
        if inul and not line.startswith("=>") and not line.startswith("* "):
            content += "</ul>\n"
            inul = False
        if inquote and not line.startswith(">"):
            content += "</blockquote>\n"
            inquote = False
        if line.startswith("```"):
            if inpre:
                content += "</pre>\n"
            else:
                content += "<pre>"
            inpre = not inpre
        elif inpre:
            content += sanitize(line) + "\n"
        elif line.startswith("* "):
            if not inul:
                content +="<ul>"
                inul = True
            content += "<li>%s</li>\n" %sanitize(line[2:])
        elif line.startswith(">"):
            if not inquote:
                content += "<blockquote>"
                inquote = True
            content += sanitize(line[1:]) + "<br>"
        elif line.startswith("##"):
            if inindex:
                inindex = False
                content += "</div>\n"
            content += "<h2>"
            content += sanitize(line.lstrip("# "))
            content += "</h2>\n"
        elif line.startswith("# "):
            #We don’t add directly the first title as it is used in the template
            if not title:
                title = sanitize(line[2:])
            else:
                content += "<h1>"
                content += sanitize(line[2:])
                content += "</h1>\n"
        elif line.startswith("=>"):
            splitted = line[2:].strip().split(maxsplit=1)
            link = splitted[0]
            #converting local links
            if "://" not in link and link.endswith(".gmi"):
                link = link[:-4] + ".html"
            if not relative_links and "://" not in link:
                link = "https://" + base_url + link.lstrip("./")
            elif local:
                link = local_url + link.lstrip("./")
            if len(splitted) == 1:
                description = ""
                name = link
            else:
                name = sanitize(splitted[1])
                description = name
            if (link[-4:] in [".jpg",".png",".gif"] or link[-5:] == ".jpeg") and\
                not link.startswith("https://commons.wikimedia.org"):
                if inul:
                    content += "</ul>\n"
                    inul = False
                #content += "<div class=\"center\">"
                imgtag = "<img alt=\"%s\" src=\"%s\" width=\"450\" class=\"center\">"%(name,link)
                content += "<a href=\"%s\">"%link + imgtag + "</a>"
                #content += "</div>"
                if description:
                    content += "<p class=\"subtitle\">" + description + "</p>"
            else:
                if not inul:
                    if inindex:
                        content += "<ul class=\"horizontal\">\n"
                    else:
                        content += "<ul>\n"
                    inul = True
                #elif inindex :
                #    content += " - "
                if inindex:
                    content += "    "
                content += "<li><a href=\"%s\">%s</a></li>"%(link,name)
                if inindex:
                    content += "    "
                content += "\n"
        elif line.strip() :
            content += "<p>%s</p>\n"%sanitize(line)
    if inul:
        content += "</ul>\n"
        inul = False
    if signature:
        content += "\n<div class=\"signature\">" + signature + "</div>"
    return content

def plaintext(content):
    lines = content.split("\n")
    result = ""
    for l in lines:
        if l.startswith("=>"):
            words = l.split(maxsplit=2)
            if len(words) > 2:
                result += textwrap.fill(words[2],width=maxwidth) + "\n"
            url = words[1]
            if "://" not in url and "mailto:" not in url:
                if url.endswith(".gmi"):
                    url = url[:-4] + ".html"
                url = "https://" + base_url + url.lstrip("/")
            result += url.rstrip() + "\n\n"
        elif l.startswith("```"):
            pass
        else:
            istitle = l.startswith("#")
            newlines = textwrap.wrap(l.lstrip("# "),width=maxwidth)
            size = len(newlines)
            while len(newlines) > 0:
                nl = newlines.pop(0)
                space = " \n"
                last = len(newlines) == 0
                if last : space = "\n"
                result += nl + space
                if istitle:
                    result += len(nl)*"=" + "\n"
            if size > 0:
                result += "\n"
    return result

# We first create a list of all entries
# Each entry is a dictionnary with the following keys.
# - title
# - date (if None, it’s a page)
# - gmifilename
# - htmlfilename
# - lang
# - folder
# - gem_content
# - html_content
# - gem_url
# - html_url
# - image
def build_post(filepath,lang="fr",signature=True,relative_links=True,local=False):
    post = {}
    post["lang"] = lang
    with open(filepath) as fi:
        lines = fi.readlines()
        fi.close()
    #special case for wordpress imported content
    #to preserver URL
    f = filepath.name
    # old if the last directory is called old
    old = filepath.parent.parts[-1] == "old"
    if old:
        slug = f[11:-4] #we remove the date and extension
        post["gmifilename"] = slug + "/index.gmi"
        post["htmlfilename"] = slug + "/index.html"
    #normal case
    else:
        post["gmifilename"] = f[:-4] + ".gmi"
        post["htmlfilename"] = f[:-4] + ".html"
    post["gem_url"] = "gemini://" + base_url + post["gmifilename"]
    post["html_url"] = "https://" + base_url + post["htmlfilename"]
    if len(lines) > 0 and lines[0].startswith("# "):
        post["title"] = lines.pop(0).strip("#  ").strip()
    # special case for header images which are right after the title
    if len(lines) > 0 and lines[0].startswith("=> "):
        if lines[0].strip().endswith(".jpg") or lines[0].strip().endswith(".png") or\
                                            lines[0].strip().endswith(".jpeg"):
            post["image"] = lines.pop(0).removeprefix("=> ").strip()
    content = "".join(lines) 
    post["gem_content"] = content
    if f.startswith("20") and len(f) >= 14:
        # We need to get the title of the post
        line = ""
        post["date"] = f[:10]
    elif f.startswith("20"):
        post["date"] = f
    else:
        post["date"] = ""
    # on produit la version html avec la signature
    sigpath = Path(post["lang"] + "/signature.html")
    if sigpath.exists() and signature:
        with open(sigpath) as sigf:
            signature_content = sigf.read()
            sigf.close()
    else:
        signature_content = None
    post["html_content"] = gmi2html(content,signature=signature_content,relative_links=relative_links,\
                                                                        local=local)
    txt = ""
    if "title" in post.keys():
        txt += textwrap.fill(post["title"].upper(),width=maxwidth) + "\n"
        txt += "by Ploum"
    if "date" in post.keys():
        txt += " on %s"%post["date"]
    txt += "\n\n"
    txt += post["html_url"] + "\n\n"
    txt += plaintext(content)
    post["plaintext_content"] = txt
    return post

def build_list(allposts,folder,local=False):
    if folder:
        folder += "/"
        recurs = True
    else:
        recurs = False
        folder = "./"
    files = os.listdir(folder)
    index_list = ""
    # We recursively build nested folder except for root
    for f in files:
        ff = folder + f
        p = Path(ff)
        if recurs and p.is_dir():
            print("Building recursively %s from %s"%(p,folder))
            allposts = build_list(allposts,ff,local=local)
        elif f.endswith(".gmi") and "index" not in f and "template" not in f:
            if len(folder) > 2:
                lang = folder[:2]
            else:
                lang = "fr"
            post = build_post(p,lang=lang,local=local)
            post["folder"] = folder
            allposts.append(post)
    return allposts

def build_atom_post(p):
    with open("atom_post_template.xml") as f:
        template = f.read()
        f.close()
    date = datetime.strptime(p["date"],"%Y-%m-%d").isoformat() + "Z"
    content = html.escape(p["html_content"])
    title = html.escape(p["title"])
    final = template.replace("$DATE",date).replace("$TITLE",title).\
            replace("$URL",p["html_url"]).replace("$CONTENT",content).\
            replace("$LANG",p["lang"])
    return final

def write_atom_index(allposts,folder,limit=10):
    with open("atom_template.xml") as f:
        atom_template = f.read()
        f.close()
    atom_posts = []
    if folder:
        atomname = "atom_" + folder.strip("/").replace("/","_") + ".xml"
        atom2 = []
    else:
        atomname = "atom.xml"
        atom2 =  [htmldir + "/feed/", htmldir + "/rss/"]
    atompath = htmldir + "/" + atomname
    allposts.sort(reverse=True,key=postdate)
    for p in allposts:
        if len(atom_posts)< limit and "date" in p.keys() and p["folder"].startswith(folder):
            if len(p["date"]) >= 10:
                atom_posts.append(build_atom_post(p))
    atom_content = ""
    for p in atom_posts:
        atom_content += p
    date = datetime.now().isoformat() + "Z"
    if folder.startswith("en"):
        lang = "en"
    else:
        lang = "fr"
    url = "https://"+base_url
    feedurl = url + atomname
    final = atom_template.replace("$CONTENT",atom_content).replace("$DATE",date).\
            replace("$GLOBAL_TITLE",global_title).replace("$URL",url).\
            replace("$SUBTITLE",global_subtitle).replace("$LANG",lang).\
            replace("$FEEDURL",feedurl)
    with open(atompath,"w") as f:
        f.write(final)
        f.close()
    for a in atom2:
        if not os.path.exists(a):
            os.makedirs(a)
        a += "index.html"
        with open(a,"w") as f:
            f.write(final)
            f.close()


# Build the index and the corresponding atom.xml file
def build_index(allposts,folder,short=False):
    index = {}
    if folder:
        indexname = "index_" + folder.strip("/").replace("/","_")
        lang = folder[:2]
    else:
        if short:
            indexname = "index"
        else:
            indexname = "index_all"
        lang = "fr"
    index["gmifilename"] = indexname + ".gmi"
    index["htmlfilename"] = indexname + ".html"
    index["lang"] = lang
    index["folder"] = folder
    content = "" 
    path = Path(folder + "/index.gmi")
    if path.exists():
        with open(path) as ind:
            content += ind.read()
            ind.close()
    else:
        with open("index.gmi") as main:
            lines = main.readlines()
            for l in lines:
                content += l
            main.close()
        with open("fr/index.gmi") as fr:
            lines = fr.readlines()
            for l in lines:
                if not l.startswith("# "):
                    content += l
            fr.close()
        with open("en/index.gmi") as en:
            lines = en.readlines()
            for l in lines:
                if not l.startswith("# "):
                    content += l
            en.close()
        with open("postindex.gmi") as main:
            lines = main.readlines()
            for l in lines:
                content += l
            main.close()
    if content:
        lines = content.split("\n")
        if lines[0].strip().startswith("# "):
            index["title"] = lines.pop(0).strip().removeprefix("# ")
        content = "\n".join(lines) + "\n"

    allposts.sort(reverse=True,key=postdate)
    last_year = 10000
    nbr_post = 0
    stop = False
    print("we have %s posts"%len(allposts))
    for p in allposts:
        if short and nbr_post >= short_limit:
            stop = True
        if not stop and "date" in p.keys() and p["date"] and p["folder"].startswith(folder):
            date = p["date"]
            year = int(date[:4])
            if not short and year < last_year:
                last_year = year
                content += "\n## %s\n\n"%year
            if len(date) >= 10:
                line = "=> %s %s : %s\n"%(p["gmifilename"],date,p["title"])
                content += line
            nbr_post += 1
            # giving a title to year. Not working with different languages
            #else:
                #content += p["gem_content"]
    if short and stop:
        content += "\n[…]"
        content += "\n=> index_all.gmi All posts"
    index["gem_content"] = content
    index["html_content"] = gmi2html(content,index=True)
    index["gem_url"] = "gemini://" + base_url + index["gmifilename"]
    index["html_url"] = "https://" + base_url + index["htmlfilename"]
    if "title" not in index.keys():
        index["title"] = global_title
    allposts.append(index)
    return allposts

def filltemplate(post,template):
    with open(template) as f:
        template = f.read()
        f.close()
    if "date" in post.keys() and post["lang"] =="en" : 
        if post["date"]: ladate = " on %s"%post["date"]
        else : ladate = ""
        subtitle = "by <a href=\"/index.html\">Ploum</a>%s"%ladate
    elif "date" in post.keys() and post["lang"] =="fr" : 
        if post["date"]: 
            ladate = " le %s"%post["date"]
        else : 
            ladate = ""
        subtitle = "par <a href=\"https://ploum.net\">Ploum</a>%s"%ladate
    else : 
        subtitle = global_subtitle
    if "date" in post.keys():
        published_date = post["date"]
    else:
        published_date = today 
    if "image" in post.keys():
        image = "<img src=\"../%s\" class=\"header\">"%post["image"]
        if not post["image"].startswith("/"):
            image_preview = "https://ploum.net/"+post["image"]
        else:
            image_preview = "https://ploum.net"+post["image"]
    else:
        image = ""
        image_preview = "https://ploum.net/files/avatar.jpg"
    if "title" in post.keys():
        template = template.replace("$TITLE",post["title"])
    final_page = template.replace("$CONTENT",post["html_content"]).\
                replace("$SUBTITLE",subtitle).replace("$LANG",post["lang"]).\
                replace("$GEMLINK",post["gem_url"]).replace("$HTMLLINK",post["html_url"]).\
                replace("$IMAGE_HEADER",image).replace("$PUBLISHED_DATE",published_date).\
                replace("$IMAGE_PREVIEW",image_preview)
    return final_page
    
def writehtml(post):
    filenames = []
    filenames.append(htmldir + "/" + post["htmlfilename"])
    if post["htmlfilename"].endswith("index.html"):
        if "date" in post.keys() and post["date"] in old_post_url:
            #old posts with old url
            filenames.append(htmldir + "/post/" + post["htmlfilename"])
    content = filltemplate(post,html_page_template)
    #print("creating %s" %filename)
    for f in filenames:
        p = Path(f)
        if not p.parent.exists():
            os.makedirs(p.parent)
        with open(f,mode="w") as ff:
            ff.write(content)
            ff.close()

def make_email(file,lang,html=True):
    post = build_post(file,lang,signature=False,relative_links=False)
    if html:
        content = filltemplate(post,email_template)
    else:
        content = post["plaintext_content"]
    return content

def writegmi(post):
    with open(gemini_page_template) as f:
        template = f.read()
        f.close()
    if "gem_content" not in post.keys():
        print("no gem_content for %s "%post)
    if "title" in post.keys():
        template = template.replace("$TITLE",post["title"])
    if "date" in post.keys():
        date = post["date"]
    else:
        date = ""
    final_page = template.replace("$CONTENT",post["gem_content"]).replace("$DATE",date).\
                replace("$GEMLINK",post["gem_url"]).replace("$HTMLLINK",post["html_url"])
    filename = geminidir + "/" + post["gmifilename"]
    p = Path(filename)
    if not p.parent.exists():
        os.makedirs(p.parent)
    with open(filename,mode="w") as f:
        f.write(final_page)
        f.close()

def postdate(p):
    if "date" in p.keys():
        return p["date"]
    else:
        return ""

## Main call
if __name__=="__main__":
    all_posts = []
    local = False
    if len(sys.argv) > 1:
        local = sys.argv[1] == "local"
        print("building locally")
    for folder in ["","fr","en"]:
        all_posts = build_list(all_posts,folder,local=local)
        all_posts = build_index(all_posts,folder)
        write_atom_index(all_posts,folder)
    all_posts = build_index(all_posts,"",short=True)
    all_posts = build_index(all_posts,"",short=False)
    write_atom_index(all_posts,"")
    all_posts.sort(reverse=True,key=postdate)
    for p in all_posts:
        writehtml(p)
        writegmi(p)
