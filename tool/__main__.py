import click

from tool import __version__
from tool.custom_decorators import add_version


@click.group()
@click.version_option(
    __version__, "-V", "--version", message="%(prog)s, version %(version)s"
)
@click.pass_context
@add_version
def cli(ctx):
    """
    Welcome to the Help Page of tool.

    $ tool ...
    """
    pass


@cli.command()
@click.option(
    "-t",
    "--text",
    default="Hello World",
    help="Text to print"
)
@click.pass_context
def do(ctx, text):
    """Print text."""
    print(text)


if __name__ == "__main__":
    cli()
