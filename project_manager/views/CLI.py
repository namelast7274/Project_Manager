import click

@click.group()
def cli():
    """
    Docstring para cli
    """
    pass
@cli.command()
def init():
    pass

@cli.command()
def stop():
    pass


if __name__ == '__main__':
    cli()