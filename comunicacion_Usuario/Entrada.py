import click
import Salida as Sl
import Main

CaractQuery = []
@click.command()
@click.argument("caract")
def add(caract):
    CaractQuery.append(str(caract))
    Sl.TComplt()

@click.command()
def search():
    Main.Busq()