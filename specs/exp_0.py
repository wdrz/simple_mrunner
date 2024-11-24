import os

from mrunner.experiment import Experiment
from munch import Munch


exp = Experiment(
    name="Basic experiment",
    script="python mrun.py",
    project=os.environ["NEPTUNE_PROJECT_NAME"],
    tags=["eval"],
    env={
        "NEPTUNE_API_TOKEN": os.environ["NEPTUNE_API_TOKEN"],
        "PYTHON_PATH": "$PYTHONPATH:.",
    },
    parameters=Munch(num_epochs=10, matrix_size=100),
)

# A specification file must contain this list
experiments_list = [exp]