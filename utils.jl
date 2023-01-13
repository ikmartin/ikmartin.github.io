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

# prints an ordered list of pages in a given directory
# expects an argument of the form (directory::String, number::number-of-pages-to-display)
# sorted in reverse chronological order
function hfun_printpages(args)
  basedir = args[1]
  println(args)
  num = parse(Int64, args[2])

  # get all subdirectories of blog, these are the posts
  dirs = filter(x -> check_post(joinpath(basedir,x)), readdir(basedir))
  print("\nAll posts: ")
  println(dirs)

  # get dates and sort posts
  dates = [stat(joinpath("$basedir", "$post/index.md")).mtime for post in dirs]
  perm = sortperm(dates, rev=true)
  idxs = perm[1:min(num, length(perm))]

  # start IOBuffer for output
  io = IOBuffer()
  write(io, "<ul>")

  # iterate through posts and generate HTML
  for (k, i) in enumerate(idxs)
    fi = basedir * splitext(dirs[i])[1] * "/"
    mdfi = fi * "index.md"
    date = Libc.strftime("%Y-%m-%d",dates[i])
    title = pagevar(mdfi,"title")
    write(io, """<li><a href="/$fi">$title (revised $date)</a></li>\n""")
  end

  # end list of posts and return output
  write(io, "</ul>")
  return String(take!(io))
end

function lx_baz(com, _)
  # keep this first line
  brace_content = Franklin.content(com.braces[1]) # input string
  # do whatever you want here
  return uppercase(brace_content)
end
