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
            if re.search("\.[png|jpeg|jpg]", f) is not None:
                midle += "<img src='" + f + "'>"
    if len(midle) > 0:
        writeHtml(path + os.sep + "pic.html", before + midle + after)


def writeHtml(path, content):
    f = open(path, 'w', encoding="UTF-8")
    f.write(content)
    f.close()


if __name__ == "__main__":
    base = "F:\pic"
    searchPic(base)
