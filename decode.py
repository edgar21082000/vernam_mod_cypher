import click
import getpass
from core import decode

@click.command()
@click.option('--base', default=14+12)
def main(base):        
    text = input()
    key = getpass.getpass()
    
    print(decode(text, key, base))

if __name__ == '__main__':
    main()