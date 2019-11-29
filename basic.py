from bluesky import RunEngine
RE = RunEngine({})

from bluesky.plans import count, scan
from bluesky.callbacks import LivePlot

from bluesky.utils import install_kicker
install_kicker()