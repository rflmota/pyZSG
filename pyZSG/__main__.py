import os
import subprocess
import sys


def main():
    sys.exit(
        subprocess.call([os.path.join(os.path.dirname(__file__), "zsg"), *sys.argv[1:]])
    )


if __name__ == "__main__":
    main()
