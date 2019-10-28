#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
how many clicks is one wiki article from another
"""

from urllib.request import Request, urlopen
from urllib import error
from html import parser
import queue
import sys

sys.setrecursionlimit(10000)
wikipedia_url = "https://en.wikipedia.org/wiki/"

father = {}
depth = {}
q = queue.Queue()


def get_attr(name, attrs):
    for n, v in attrs:
        if n == name:
            return v
    return None


def test(href):
    if href == None:
        return False
    if href.find("/wiki/") != -1:
        if href.find(":") == -1:
            return True
    return False


class ParserEx(parser.HTMLParser):
    def __init__(self, con):
        parser.HTMLParser.__init__(self)
        self.divlevel = None
        self.content = False
        self.conception = con

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            if get_attr("class", attrs) == "mw-parser-output":
                self.content = True
                self.divlevel = 0

            if self.content:
                self.divlevel += 1

        if tag == "a":
            href = get_attr("href", attrs)
            global father
            if self.content and test(href):
                if href[6:] not in father:
                    q.put(con)
                    father[con] = self.conception

    def handle_endtag(self, tag):
        if tag == "div" and self.content:
            self.divlevel -= 1
            if self.divlevel <= 0:
                self.content = False

    def handle_data(self, data):
        pass


def getConceptionHTML(con):
    req = Request(wikipedia_url + con, headers={"User-Agent": "Magic Browser"})
    src = urlopen(req)
    src = src.read().decode(sys.stdout.encoding, errors="replace")
    return src


def processConception(con):
    html_string = getConceptionHTML(con)
    html_parser = ParserEx(con)
    for line in html_string:
        html_parser.feed(line)


def traverse_wikipedia(father, depth, conception, desc_conception):
    q.put(conception)

    currentdepth = 0

    while q.qsize() > 0:
        conception = q.get()
        print("Currently processing: {}".format(conception))
        depth[conception] = depth[father[conception]] + 1

        if depth[conception] > currentdepth:
            currentdepth = depth[conception]
            print("Actual level of BFS: {}".format(currentdepth))

        if conception == desc_conception:
            break

        processConception(conception)


def main(conception, desc_conception):
    father[conception] = conception
    depth[conception] = -1

    traverse_wikipedia(father, depth, conception, desc_conception)

    print(depth)
    print(father)

    current_conception = desc_conception
    while current_conception != conception:
        print("{}{}".format("\t" * depth[current_conception], current_conception))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
