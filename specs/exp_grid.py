import os

from mrunner.helpers.specification_helper import create_experiments_helper

experiments_list = create_experiments_helper(
    experiment_name="Basic experiments grid",
    base_config={
        "num_epochs": 10,
    },
    params_grid={
        "matrix_size": [100, 1000],
    },
    script="python3 mrun.py",
    python_path=".",
    exclude=["singularity.sif", "__pycache__"],
    tags=["eval"],
    project_name=os.environ["NEPTUNE_PROJECT_NAME"],
)
