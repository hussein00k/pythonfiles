def disply(dict):
    for x, y in dict.items():
        print(x + ": " + y)


info={"name":"hussein","age":"28","location":"aboalksib"}
disply(info)

print("---------add new itme\n")
info["collage"]="information technology"
disply(info)
print("---------remove the name\n")

info.pop("name")
disply(info)
