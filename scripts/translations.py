import click
import os

@click.group()
def cli():
    pass

@click.command()
def compile():
    """Compile translations"""
    click.secho('Compiling translations', fg='green')
    os.system('pybabel compile -d ../translations')
    
@click.command()
@click.argument('lang')
def init(lang):
    """Create a new language file"""
    click.secho('Extract placeholders from templates...', fg='green')
    if os.system('pybabel extract -F ../babel.cfg -k _l -o ../messages.pot ../'):
        raise RuntimeError('extract command failed')
    click.secho('Create new language file...', fg='green')
    if os.system('pybabel init -i ../messages.pot -d ../translations -l ' + lang):
        raise RuntimeError('init command failed')
    click.secho('Remove messages.pot...', fg='green')
    os.remove('../messages.pot')

@click.command()
def update():
    """Update all languages."""
    click.secho('Extract placeholders from templates...', fg='green')
    if os.system('pybabel extract -F ../babel.cfg -k _l -o ../messages.pot ../'):
        raise RuntimeError('extract command failed')
    click.secho('Update language files...', fg='green')
    if os.system('pybabel update -i ../messages.pot -d ../translations'):
        raise RuntimeError('update command failed')
    click.secho('Remove messages.pot...', fg='green')
    os.remove('../messages.pot')
    
cli.add_command(compile)
cli.add_command(init)
cli.add_command(update)

if __name__ == '__main__':
    cli()