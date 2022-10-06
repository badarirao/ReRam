from MyKeysightB2902B import KeysightB2902B
# NOT completed yet
from utilities import *

vstart = 0
vend = 1
current_limit = 1 #mA

nPoints = int(abs(vend-vstart)) * 10 + 1
if nPoints < 11:
    nPoints = 11
vPoints = np.linspace(vstart,vend,nPoints)
nIPoints = int(abs(current_limit)) * 10 + 1
if nIPoints < 11:
    nIPoints = 11
iPoints = np.linspace(0,current_limit,nIPoints)/1000

smu = KeysightB2902B("USB0::0x2A8D::0x9201::MY61390641::INSTR")
smu.reset()
smu.nplc = 2 # why 2?
smu.apply_voltage(compliance_current=current_limit)
smu.source_voltage = 0.1
smu.measure_current()
smu.set_read_back_on()
smu.write(":FORM:ELEM:SENS VOLT,CURR")
smu.enable_source()

iFlag = False
for v in vPoints[1:]:
    smu.source_voltage = v
    m = 0
    while True:
        if smu.is_compliance_tripped():
            if l < len(iPoints) - 1:
                l = l + 1
                i = iPoints[l]
                smu.set_compliance(i)
                m = 0
            else:
                iFlag = True  # if the user specified current limit is reached
                m = 11
        else:
            m = m + 1
        sleep(0.1)
        if m > 10:
            values = smu.get_one_shot()
            volt = float(values[0])
            current = float(values[1])
            break
    if iFlag:
        break
smu.source_voltage = 0
smu.disable_source()
