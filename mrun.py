import os

from mrunner.helpers.client_helper import get_configuration, logger

from my_beautiful_code import main


def mrun():
    assert "NEPTUNE_API_TOKEN" in os.environ

    params = get_configuration(print_diagnostics=True, with_neptune=True)

    print(params)

    main(params)

if __name__ == "__main__":
    mrun()
