#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pathlib
import re
import os
import random

root = pathlib.Path(__file__).parent.resolve()


TOKEN = os.environ.get("GITHUB_TOKEN", "")


def replace_chunk(content, marker, chunk):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    chunk = "<!-- {} starts -->\n{}\n<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)


if __name__ == "__main__":
    if random.randint(1,100) == 27:
        readme = root / "README.md"
        readme_contents = readme.open().read()
        md = random.choice([
            "**A rocket moves a nation 🚀**",
            "**A ship in harbor is safe, but that is not what ships are built for ⚓️**",
            "**The moon moves the tide in mysterious ways**",
            "**The tide waits for no man 👨‍🚀**",
            ])
        rewritten = replace_chunk(readme_contents, "daily_quote", md)
        readme.open("w").write(rewritten)
