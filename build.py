"""Builds the paste-ready home page files from home-page-elementor.html.

    python3 build.py

Writes:
  home-page-elementor-compact.html   one file for the Elementor HTML widget
  home-page-split/                   the same page in three parts, for when
                                     a firewall blocks saving <style>/<script>
"""
import os
import re

SRC = "home-page-elementor.html"
DIAGRAM_MIN = "src/one-diagram-home.min.html"
START, END = "<!-- ONE DIAGRAM START -->", "<!-- ONE DIAGRAM END -->"


def minify_css(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s*\n\s*", " ", css)
    css = re.sub(r"\s*([{};:,>])\s*", r"\1", css)
    return css.replace(";}", "}").strip()


def tidy_html(html):
    return re.sub(r"\n\s*\n+", "\n\n", html)


page = open(SRC, encoding="utf-8").read()
diagram = open(DIAGRAM_MIN, encoding="utf-8").read().strip()

css_end = page.index("</style>")
css = minify_css(page[len("<style>"):css_end])
body = page[css_end + len("</style>"):]
before, rest = body.split(START, 1)
after = rest.split(END, 1)[1]

# 1. Single compact file
with open("home-page-elementor-compact.html", "w", encoding="utf-8") as f:
    f.write("<style>\n" + css + "\n</style>" + tidy_html(before) + diagram + tidy_html(after))

# 2. Split version: CSS, HTML with no <style>/<script>, and the scripts
d_style = re.search(r"<style>(.*?)</style>", diagram, re.S)
d_script = re.search(r"<script>(.*?)</script>", diagram, re.S)
d_markup = diagram[:d_style.start()] + diagram[d_style.end():d_script.start()]

scripts = re.findall(r"<script[^>]*>.*?</script>", before + after, re.S)
for s in scripts:
    before, after = before.replace(s, ""), after.replace(s, "")

os.makedirs("home-page-split", exist_ok=True)
with open("home-page-split/1-styles.css", "w", encoding="utf-8") as f:
    f.write(css + "\n" + d_style.group(1).strip() + "\n")
with open("home-page-split/2-page.html", "w", encoding="utf-8") as f:
    f.write(tidy_html(before + d_markup + after).strip() + "\n")
with open("home-page-split/3-scripts.html", "w", encoding="utf-8") as f:
    f.write("<script>" + d_script.group(1) + "</script>\n" + "\n".join(scripts) + "\n")

print("Built home-page-elementor-compact.html and home-page-split/")
