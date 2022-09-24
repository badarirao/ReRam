from MyKeysightB2902B import KeysightB2902B
from numpy import linspace, reshape, array, around
from time import sleep, time
from utilities import *
import matplotlib.pyplot as plt

vmin = -3
vmax = 3
vstep = 0.1
pulse_width = 1e-3
scan_speed = 1
current_limit = 1e-3
readV = 0.1
numCycles = 1

nPoints = int(abs(vmax-vmin)/vstep)+1
nCycles = 1
voltages = around(linspace(vmin,vmax,nPoints),decimals = 4)
voltages = ",".join(voltages.astype('str'))
smu = KeysightB2902B("USB0::0x2A8D::0x9201::MY61390641::INSTR")
smu.reset()
smu.apply_voltage()
smu.write(f":sour{smu.ch}:func:shap puls")
smu.write(f"SOUR{smu.ch}:VOLT:MODE LIST")
smu.write(f"SOUR{smu.ch}:LIST:VOLT {voltages}")
smu.write(f":OUTP{smu.ch}:PROT 0")
smu.write(f"TRIG{smu.ch}:TRAN:DEL 0")
measurement_time = smu.get_measurement_time() + 20e-6 # assume 20 µs overhead, need to adjust appropriately
pulse_delay = 2e-5
acq_trigger_period = pulse_width + pulse_delay + 2e-5 # add buffer 20 µs
source_trigger_period = 2 * acq_trigger_period
smu.write(f"SOUR{smu.ch}:PULS:DEL {pulse_delay}") # 20 µs pulse delay
smu.nplc = 0.1
smu.measure_current()
smu.set_compliance(current_limit)
smu.write(":trig:sour TIM")
# set source trigger conditions
smu.write(f":trig:tran:tim {source_trigger_period}")
smu.write(f":trig:tran:coun {nPoints}")
# set acquire trigger conditions
smu.write(f":trig:acq:tim {acq_trigger_period}")
smu.write(f":trig:acq:coun {2*nPoints}") # one for write current, one for read current
smu.write(":FORM:ELEM:SENS VOLT,CURR")

smu.write(f"TRAC{smu.ch}:CLEar")
smu.write(f"TRAC{smu.ch}:POIN {2*nPoints}")
smu.write(f"TRAC{smu.ch}:FEED SENS")
smu.write(f"TRAC{smu.ch}:FEED:CONT NEXT")
smu.write(f"TRAC{smu.ch}:TST:FORM DELT")

# get total points measured
# smu.ask(":TRAC:POIN:ACT?")
smu.write(":outp on")

print("Started...")
smu.write(":init (@1)")
while smu.get_trigger_state() == 'RUNNING':
    sleep(2)
    data = smu.ask(":TRAC:Data?")
    data2 = reshape(array(data.split(','), dtype=float), (-1, 2))
    print(len(data2))
"""    
count = 0
start = time()
t = smu.inst.timeout
del smu.inst.timeout # now it will wait infinitely for a response
print(f"opc = {smu.ask('*OPC?')}")
smu.inst.timeout = t
end = time()
print(f"Total run time = {end-start}")
data = smu.ask(f":fetc:arr? (@{smu.ch})")
data2 = reshape(array(data.split(','), dtype=float), (-1, 6))

"""
v = data2[:,0]
i = data2[:,1]
smu.disable_source()
plt.plot(v, i)
plt.show()
