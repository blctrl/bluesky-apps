from bluesky import RunEngine
RE = RunEngine({})

from bluesky.plans import count, scan
from bluesky.callbacks import LivePlot

from ophyd.sim import noisy_det
from bluesky.utils import install_qt_kicker
install_qt_kicker()


RE(count([noisy_det], num=200, delay = 0.1), LivePlot('noisy_det'))
