import torch
from mrunner.helpers.client_helper import logger


def main(config):
    num_epochs = config.num_epochs
    matrix_size = config.matrix_size
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    print("Using device:", device)
    logger("device", str(device))

    for i in range(num_epochs):
        # Multiply two matrices on GPU
        a = torch.randn(matrix_size, matrix_size).to(device)
        b = torch.randn(matrix_size, matrix_size).to(device)

        c = a @ b
        res = c.mean()

        # log result
        print(f"Iteration {i}:", res)
        
        # log to neptune
        logger("result", res)

    print("Finished run.")