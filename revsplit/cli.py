import click


@click.command()
@click.option('--name')
def hello(name: str):
    """Dummy function for testing."""
    click.echo(f'Hello {name}!')
