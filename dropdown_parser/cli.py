import click
from dropdown_parser import Parser, OutputTypes
from typing import get_args


@click.command()
@click.argument("file_path", required=True, type=str)
@click.option(
    "--output",
    "-o",
    default="csv",
    type=click.Choice(get_args(OutputTypes)),
    show_default=True,
)
def cli(file_path: str, output: OutputTypes = "csv") -> None:
    parser = Parser(file_path)
    parser.parse(output)


if __name__ == "__main__":
    cli()
