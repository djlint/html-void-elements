"""
python port of https://github.com/wooorm/html-tag-names/blob/main/build.js
"""
from bs4 import BeautifulSoup
import requests
import re

from HtmlVoidElements import html_void_elements

tags = html_void_elements

# Crawl W3C.
page = requests.get("https://html.spec.whatwg.org/multipage/syntax.html")
soup = BeautifulSoup(page.content, "html.parser")

parent = soup.select("#elements-2 ~ dl")[0].find("dd")

# html is poorly made, need to remove child dd.

for child in parent.find_all("dd"):
    child.decompose()
for child in parent.find_all("dt"):
    child.decompose()

for row in parent.select("code"):
    tag = row.get_text().strip()

    if not re.search(r"\s", tag) and tag not in tags:
        tags.append(tag)


tags.sort()
with open("HtmlVoidElements/html_void_elements.py", "w+", encoding="utf8") as built:
    built.write(
        f"""\"\"\"
List of HTML void tag names.
\"\"\"

html_void_elements = {tags}"""
    )
