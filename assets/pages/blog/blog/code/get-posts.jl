# This file was generated, do not modify it. # hide
#hideall
for (root, dirs, files) in walkdir("./pages/blog/posts")
  for dir in dirs
    # displays link to each post
    # chops the "." from the begining of path
    println("[$dir](" * chop(joinpath(root,dir), head = 1, tail = 0) * ")\n")
  end
end