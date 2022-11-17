# "Blog", place to put random stuff

```julia:get-posts
#hideall
for (root, dirs, files) in walkdir("./pages/blog/posts")
  for dir in dirs
    # displays link to each post
    # chops the "." from the begining of path
    println("[$dir](" * chop(joinpath(root,dir), head = 1, tail = 0) * ")\n")
  end
end

```

\textoutput{get-posts}

<!-- Format for link:
[2022-11-04: Why Schemes?](/pages/blog/posts/post1/)
-->
