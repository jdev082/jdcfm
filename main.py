#!/usr/bin/env python3
# jdcfm - jdev082 commandline file manager
# jdev082, MIT license, 2024
import os
import pathlib
import platform
import sys
import subprocess
from simple_term_menu import TerminalMenu

system = platform.system().lower()

def interact(file):
    if os.path.isdir(file):
        draw(file)
    else:
        opts(file)

def opts(file):        
    if os.access(file, os.X_OK):
        options = ['Run', 'Run with arguments']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 0:
            subprocess.run([file])
        if menu_entry_index == 1:
            args = input("Supply arguments: ")
            subprocess.run([file, args])
    else:
        if system == "linux":
            editor = os.environ.get("EDITOR")
            subprocess.run([editor, file])

def draw(dir):
    contents = os.listdir(dir)
    contents.insert(0, "..")
    terminal_menu = TerminalMenu(contents)
    menu_entry_index = terminal_menu.show()
    if contents[menu_entry_index] == "..":
        interact(os.path.dirname(dir))
    else:
        interact(os.path.join(dir, contents[menu_entry_index]))

def main():
    if len(sys.argv) > 1:
        draw(sys.argv[1])
    else:
        draw(os.getcwd())

if __name__ == "__main__":
    main()