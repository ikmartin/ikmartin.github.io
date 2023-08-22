using Dates
function hfun_bar(vname)
  val = Meta.parse(vname[1])
  return round(sqrt(val), digits=2)
end

function hfun_m1fill(vname)
  var = vname[1]
  return pagevar("index", var)
end

function hfun_pageFill(page,vname)
  var = vname
  return pagevar(page,var)
end

function check_post(postdir)
  return isdir(postdir) && isfile(joinpath(postdir,"index.md"))
end

function retrieve_date(post)
  # try to retrieve the manually inputted date from the post
  try
    date = pagevar(post,"date")
    date = Dates.DateTime(date)
    return Dates.datetime2unix(date)
  # if no date is available then use the creation time as the date
  catch e
    date = stat(joinpath("$basedir", "$post/index.md")).ctime
    return date
  end
end

# prints an ordered list of pages in a given directory
# expects an argument of the form (directory::String, number::number-of-pages-to-display)
# sorted in reverse chronological order
function hfun_printpages(args)
  basedir = args[1]
  num = parse(Int64, args[2])

  # get all subdirectories of blog, these are the posts
  dirs = filter(x -> check_post(joinpath(basedir,x)), readdir(basedir))
  print("\nAll posts: ")
  println(dirs)

  # get dates and sort posts
  dates = [retrieve_date(joinpath("$basedir", "$post/index.md")) for post in dirs]

  perm = sortperm(dates, rev=true)
  idxs = perm[1:min(num, length(perm))]

  # start IOBuffer for output
  io = IOBuffer()
  write(io, "<ul>")

  # iterate through posts and generate HTML
  for (k, i) in enumerate(idxs)
    file = basedir * splitext(dirs[i])[1] * "/"
    mdfile = file * "index.md"
    date = Libc.strftime("%Y-%m-%d",dates[i])
    title = pagevar(mdfile,"title")
    write(io, """<li><a href="/$file">$date: $title</a></li>\n""")
  end

  # end list of posts and return output
  write(io, "</ul>")
  return String(take!(io))
end

function parse_bibtex(bib)
  pairs = split(bib, ";")
  dict = Dict()
  for pair in pairs
    if isempty(pair)
      continue
    end
    println(pair)
    key,value = split(pair, ":")
    key = strip(key)
    dict[key] = value
  end
  return dict
end

function hfun_makeref(args)
  println(args)
  println(join(args, " "))
  args = parse_bibtex(join(args, " "))
  year = strip(args["year"])
  journal = args["journal"]
  volume = args["volume"]
  pages = isempty(args["pages"]) ? "" : args["pages"]
  title = lstrip(args["title"])
  path = lstrip(args["path"])

  # start io buffer
  io = IOBuffer()
  write(io, """<font color="navy"><b>$title</b></font><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i> $journal</i><b>$volume</b> ($year) $pages<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Download <a href="$path">PDF</a><br>""")
  return String(take!(io))
end

function lx_baz(com, _)
  # keep this first line
  brace_content = Franklin.content(com.braces[1]) # input string
  # do whatever you want here
  return uppercase(brace_content)
end
