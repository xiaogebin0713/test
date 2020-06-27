import re

if __name__ == "__main__":
    a = "[mysql]"
    print(re.match("^\[([^\[\]]*)\]$", a).group(1))