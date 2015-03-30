# coding=utf-8
"""
cryptoboxcli
-
Active8 (30-03-15)
author: erik@a8.nl
license: GNU-GPL2
"""

import ast
import codegen
def main():
    """
    main
    """
    tree = ast.parse(open("__init__.py").read(), '__init__.py', 'exec')
    names = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef):
            names.add(n.name)
    names = list(names)
    names.sort()
    nw = open("newfile.py", "wt")
    lines = open("__init__.py").read().split("\n")
    methods = []
    lines = [x for x in lines if len(x.strip())>0]
    for n in names:
        b = False

        for l in lines:
            if l.startswith("def "+n):
                if b is False:
                    b = True

            if b is True:
                methods.append(l)

            #else:
            #    print(l)

    for x in methods:
        print("--------")
        print(x)


if __name__ == "__main__":
    main()
