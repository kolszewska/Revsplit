import click


@click.command()
@click.option('--name')
def hello(name: str):
    click.echo(f"Hello {name}!")
