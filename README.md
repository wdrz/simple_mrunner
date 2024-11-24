# Simple mrunner example

Run locally
```
python3 mrun.py --ex specs/exp_0.py
```

## Remotely run a grid of experiments

Add mrunner config to `~/.config/mrunner/config.yaml` and run
```
mrunner --context athena run specs/exp_grid.py
```

Or alternatively specify the path and run:

```
mrunner --config mrunner_config.yaml --context athena run specs/exp_grid.py
```
