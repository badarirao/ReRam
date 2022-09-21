from MyKeysightB2902B import KeysightB2902B
from numpy import linspace, reshape, array
from time import sleep, time
from utilities import *
import matplotlib.pyplot as plt

vmin = -3
vmax = 3
delay_per_point = 10 #ms
scan_speed = 3 # fast
ilim = 1e-3 # A
nPoints = 500
nCycles = 1
voltages = linspace(vmin,vmax,nPoints,dtype=str)
voltages = ",".join(voltages)
smu = KeysightB2902B("USB0::0x2A8D::0x9201::MY61390641::INSTR")
smu.reset()
smu.apply_voltage()
smu.write(f"SOUR{smu.ch}:VOLT:MODE LIST")
smu.write(f"SOUR{smu.ch}:LIST:VOLT {voltages}")
smu.write(f":OUTP{smu.ch}:PROT 0")
smu.write(f"TRIG{smu.ch}:TRAN:DEL 0")
smu.write(f"TRIG{smu.ch}:ACQ:DEL {delay_per_point/1000}")
smu.nplc = 0.1
smu.measure_current()
smu.set_compliance(ilim)
smu.write(":trig:sour aint")
smu.write(f"trig:coun {nPoints}")
smu.write(":FORM:ELEM:SENS VOLT,CURR")
smu.write(f"TRAC{smu.ch}:CLEar")
smu.write(f"TRAC{smu.ch}:POIN {nPoints}")
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
    data = smu.ask(":TRAC:Data? CURR")
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
