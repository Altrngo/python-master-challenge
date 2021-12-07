import typer

app = typer.Typer()

def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"), extension: str = typer.Argument("txt", help="Extension à rechercher")):
  typer.echo(f"Recherche des fichiers avec l'extension {extension}")
  
if __name__ == "__main__":
  typer.run(main)