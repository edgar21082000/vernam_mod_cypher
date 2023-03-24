import click
import datetime
import getpass
import os

from core import encode


@click.command()
@click.option('--base', default=14+12)
def main(base):
    text = input()
    key = getpass.getpass()

    res = encode(text, key, base)
    print(res[0], res[1])

    path = ".code.history"
    with open(path, "a") as fp:
        fp.write(f"{datetime.datetime.now().isoformat()[:-7]}: {str(res[1])[0]+res[0]+str(res[1])[1]}\n")


if __name__ == '__main__':
    main()
