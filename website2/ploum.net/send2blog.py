#!/bin/python
import sys
import textwrap
import subprocess
from pathlib import Path
from publish import make_email
from io import StringIO
from email.generator import Generator
from email.message import EmailMessage

import smtplib,ssl

debug = False
mailto_debug = "lionel@ploum.net"
maxwidth = 68

enqueue="/usr/libexec/msmtp/msmtpqueue/msmtp-enqueue.sh"
blog_path = "/home/ploum/dev/gemlog"
liste={}
liste["fr_html"] = ["ploum@mailfence.com","fr@listes.ploum.net"]
liste["fr_txt"] = ["lio@ploum.be","phalfvauctehxnmyhpindnuchhiwjfu@simplelogin.co"]
liste["en_txt"] = ["lio@ploum.be","hqfnixzqxoajfufzaugcwavzslbeceyxdgxekrgz@simplelogin.co"]
liste["en_html"] = ["ploum@mailfence.com","en@listes.ploum.net"]
unsubscribe_fr = "Pour vous désabonner, envoyez un mail à ~lioploum/fr+unsubscribe@lists.sr.ht"
unsubscribe_en = "To unsubscribe, send an email to ~lioploum/en+unsubscribe@lists.sr.ht"
#mailto = ["~lioploum/fr@lists.sr.ht","fr@listes.ploum.net"]
#password=input("SMTP password: ")

def create_mail(pathpost,lang="fr",html="True"):
    if pathpost.exists():
        with open(pathpost) as post:
            content = post.read()
            post.close()
    else:
        return 
    if html:
        htmlcontent = make_email(pathpost,lang)
    txtcontent = make_email(pathpost,lang,html=False)
    if not html:
        txtcontent += "\n\n--- \n"
        if lang == "en": 
            txtcontent += unsubscribe_en 
        else:
            txtcontent += unsubscribe_fr
    if html:
        key = lang + "_html"
    else:
        key = lang + "_txt"
    message = EmailMessage()
    lines = content.split("\n")
    title = lines[0].lstrip("# ")
    message["Subject"] = title
    message["From"] = liste[key][0]
    if debug:
        message["To"] = mailto_debug
    else:
        message["To"] = liste[key][1]
    message.set_content(txtcontent)
    if html:
        message.add_alternative(htmlcontent,subtype="html")
    return message

def sendmail(dest,message):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.mailfence.com", 465, context=context) as server:
        server.login(mailfrom, password)
        server.sendmail(mailfrom, dest, email.as_string())

def msmtp(mailfromto,email):
    mailfrom = mailfromto[0]
    if "mailfence" in mailfrom:
        account = "mailfence"
    elif "mailbox" in mailfrom:
        account = "mailbox"
    else:
        account = "default"
    # can be piped to msmtp-enqueue.sh -t -a mailbox
    cmd = "%s -t -a %s"%(enqueue,account)
    result = subprocess.run(cmd,input=email.as_string().encode(),shell=True,stdout=subprocess.PIPE,\
                            stderr=subprocess.STDOUT)
    #print(result.stdout.decode())
    #print(email.as_string())

if __name__=="__main__":
    postfile = sys.argv[1]
    if len(sys.argv) <= 2:
        lang = None
        while lang not in ["en","fr"]:
            lang = input("Langue du post? FR/EN : ").lower()
    else:
        lang = sys.argv[2].lower()
    if lang not in ["fr","en"]:
        print("Choose your language : FR/EN")
    else:
        pathpost = Path(postfile)
        if not pathpost.absolute().is_relative_to(blog_path):
            print("we should check spelling")
            print("we should move the file")
            print("we should rename the file with a date")
            print("we should run publish.py and check")
            print("we should add it to the repository")
            print("we should commit")
            print("we should update pathpost")
        elif pathpost.exists():
            email = create_mail(pathpost,lang=lang,html=True)
            msmtp(liste[lang+"_html"],email)
            #sendmail(mailto,email)
            email2 = create_mail(pathpost,lang=lang,html=False)
            msmtp(liste[lang+"_txt"],email2)
        else:
            print("No %s file"%postfile)
