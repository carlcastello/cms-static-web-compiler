import sys
from parser import read_file

def cms_static_web_compiler():
    print(read_file(sys.argv[1]))


if __name__ == "__main__":
    
    cms_static_web_compiler()
