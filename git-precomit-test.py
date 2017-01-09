# This is my git pre-commit test script.
import subprocess

import sys 
import re

def main():
    input  = sys.stdin.read()
    oldrev, newrev, refname = input.split(" ")
    separator = "----****----"


    proc = subprocess.Popen(["git", "log", "--format=%H%n%ci%n%s%b%n" + separator, oldrev + ".." +  newrev], stdout=subprocess.PIPE)
    message = proc.stdout.read()
    commit_list = message.strip().split(separator)[:-1] #discard the last line

    is_valid = True

    print "Parsing message:"
    print message

    for commit in commit_list:
        line_list = commit.strip().split("\n")
        hash = line_list[0]
        date = line_list[1]
        content = " ".join(line_list[2:])
        if not re.findall("refs *#[0-9]+", content): #check for keyword
            is_valid = False

        sys.exit(1)

main()