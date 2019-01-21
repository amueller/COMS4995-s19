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

EXCLUDED = ['index.html']

import os

# May need to do "pip install mako"
from mako.template import Template


def main():
    directory = os.getcwd()
    fnames = [fname for fname in sorted(os.listdir(directory))
              if fname not in EXCLUDED and os.path.isdir(fname)]
    header = "https://amueller.github.io/COMS4995-s18/slides/"
    with open("index.html", "w") as f:
        f.write(Template(INDEX_TEMPLATE).render(names=fnames, header=header))


if __name__ == '__main__':
    main()
