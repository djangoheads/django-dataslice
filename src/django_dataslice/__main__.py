"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Django Dataslice."""


if __name__ == "__main__":
    main(prog_name="django-dataslice")  # pragma: no cover
