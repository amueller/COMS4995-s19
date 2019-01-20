""" Build index from directory listing

make_index.py </path/to/directory> [--header <header text>]
"""

INDEX_TEMPLATE = r"""
<html>
<body>
<h2>${header}</h2>
<p>
% for name in names:
    <li><a href="${name}">${name}</a></li>
% endfor
</p>
</body>
</html>
"""

import os
import glob

# May need to do "pip install mako"
from mako.template import Template


def main():
    directory = os.getcwd()
    fnames = glob.glob("aml-*")
    fnames.sort()
    header = "https://amueller.github.io/COMS4995-s19/slides/"
    with open("index.html", "w") as f:
        f.write(Template(INDEX_TEMPLATE).render(names=fnames, header=header))


if __name__ == '__main__':
    main()
