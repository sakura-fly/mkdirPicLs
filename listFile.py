import os
import re

before = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Document</title>
</head>
<body>
"""

after = """
</body>
</html>
"""


def searchPic(path):
    p = os.listdir(path)
    midle = ''
    for f in p:
        if os.path.isdir(path + os.sep + f):
            searchPic(path + os.sep + f)
        else:
            if re.search(".[png|jpeg|jpg]", f) is not None:
                midle += "<img src='" + f + "'>"
    print(midle)
    if not midle.isspace():
        f = open(path + os.sep + "pic.html", 'w', encoding="UTF-8")
        f.write(before + midle + after)
        f.close()


if __name__ == "__main__":
    base = "F:\pic"
    searchPic(base)
