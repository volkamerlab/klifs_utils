"""Console script for klifs_utils."""
import argparse
import sys


def main():
    """Console script for klifs_utils."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "klifs_utils.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
