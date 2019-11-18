import time, os

from bluesky import RunEngine
RE = RunEngine({})

from bluesky.plans import count, scan
from bluesky.callbacks import LivePlot

from ophyd.sim import noisy_det
from databroker import Broker
db = Broker.named('temp')
RE.subscribe(db.insert)
RE(count([noisy_det], num=20, delay = 0.1), LivePlot('noisy_det'))




header =db[-1]
data = header.table()

path = "/home/blctrl/"
file_directory = path + "blcg_data/"
if not os.path.exists(file_directory):
	os.mkdir(file_directory)

file_time = time.strftime('%Y%m%d_%H%M%S')

data.to_csv(file_directory + "blcg-" + file_time + ".csv")



