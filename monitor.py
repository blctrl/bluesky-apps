from bluesky import RunEngine
RE = RunEngine({})

from bluesky.plans import count, scan
from bluesky.callbacks import LivePlot

from ophyd.sim import noisy_det

RE(count([noisy_det], num=1000, delay = 0.1), LivePlot('noisy_det'))
