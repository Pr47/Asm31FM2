import os, sys
from application import application_start

if __name__ == '__main__':
    exit(application_start(sys.argv, os.environ))
