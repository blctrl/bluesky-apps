from ophyd import EpicsMotor

m1 = EpicsMotor("m1",name="m1")

from ophyd import PVPositioner, EpicsSignal,EpicsSignalRO
from ophyd import Component as cpt

#define a device which can be scanned

class tmp(PVPositioner):
    setpoint = cpt(EpicsSignal,'.VAL')
    readback = cpt(EpicsSignalRO,'.RBV')
    done = cpt(EpicsSignalRO,'.DMOV')
    stop_signal = cpt(EpicsSignal,'.STOP')
    
#m2=tmp('m2',name='m2')  #m2 is a motor record