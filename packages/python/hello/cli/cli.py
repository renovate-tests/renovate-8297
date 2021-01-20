import click

from packages.python.hello.core.hello import say_hello

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(name):
    """Simple program that greets."""
    click.echo(say_hello(name))

if __name__ == '__main__':
    hello()
