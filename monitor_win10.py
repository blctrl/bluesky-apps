#monitor_win10

from bluesky import RunEngine
RE = RunEngine({})

from bluesky import RunEngine
RE = RunEngine({})

from bluesky.plans import count, scan
from bluesky.callbacks import LivePlot

from ophyd.sim import noisy_det

from bluesky.utils import install_kicker
install_kicker()

print("RE(count([noisy_det], num=50, delay = 0.1), LivePlot('noisy_det'))")



