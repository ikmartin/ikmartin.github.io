"""Python used to generate a template blog post. Usage:
python3 genpost.py "Title of Post" -d "Description of the blog post" -dn "The directory name of the post" -t tag1 tag2 tag3
"""


import os
import os.path as path
import argparse
from datetime import date


# increment given name starting at n until valid name found
def increment_name(name, n):
    if path.exists(name + str(n)) == False:
        return name + str(n)
    else:
        return increment_name(name, n + 1)


# the default post template
templatePost = """+++
title = "{}"
hascode = true
description = "{{}}"
tags = {}
date = "{}"
published = true
public = false
+++

@def mintoclevel=2
@def maxtoclevel=3

# {{title}}

> {{description}}

\\toc

---

<Put content here>

"""

# description of command line arguments
desc = """Generates a template blog post directory with a markdown file."""

# start the argument parser
parser = argparse.ArgumentParser(description=desc)

# title argument (required)
parser.add_argument(
    dest="title", metavar="title", type=str, nargs=1, help="title of the post"
)

# description argument (optional, default=no description available)
parser.add_argument(
    "-d",
    "--desc",
    default="no description available",
    nargs=1,
    dest="desc",
    help="description of the post",
)

# directory name (optional, default=post)
parser.add_argument(
    "-dn", "--dirname", default="post", nargs=1, dest="dirname", help="directory name"
)

# tags argument (optional)
parser.add_argument(
    "-t", "--tags", nargs="+", dest="tags", help="tags associated to the post"
)

# parse arguments, store relevant values in variables
args = parser.parse_args()
title = args.title[0]
dirname = args.dirname[0]
post_desc = args.desc[0]
tags = args.tags if args.tags else ["blog"]
date = date.today()

# format tags
newtags = "["
for tag in tags:
    newtags += '"' + tag + '", '

newtags = newtags[: len(newtags) - 2]  # remove last comma
newtags += "]"

# get valid directory name
if path.exists(dirname):
    dirname = increment_name(dirname, 1)

os.mkdir(dirname)
os.chdir(dirname)
with open("index.md", "w") as f:
    text = templatePost.format(title, post_desc, newtags, date)
    f.write(text)