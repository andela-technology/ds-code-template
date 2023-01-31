
"""
TODO: Replace this with a proper module description.
"""

from pathlib import Path

import click
import yaml


def my_function(value) -> str:
    """
    TODO: Replace this with a proper function description.
    Args:
        value (_type_): _description_
    Returns:
        _type_: _description_
    """

    return str(value)

@click.command()
@click.option("--run-config", "--config",
    type=click.Path(exists=True),
    help="The path to the runtime configuration file.",
    required=True,
)
def main(run_config: str):
    """
    The main method. This should be the entry point of the cli program.
    Args:
        run_config (str): Path to the runtime configuration file.
    """

    # read runtime configuration file
    run_config = yaml.safe_load(Path(run_config).read_text("utf-8"))

    # extract the variables of interest
    properly_named_variable = run_config["properly_named_variable"]

    # run our function
    my_function(properly_named_variable)


if __name__ == "__main__":

    # pylint: disable=no-value-for-parameter
    main()