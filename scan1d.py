#scan 1D

from  bluesky.plans import scan
from ophyd.sim import motor,det
from bluesky.callbacks import LivePlot
print("RE(scan([det],motor,0,10,10),LivePlot('det'))")