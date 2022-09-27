from MyKeysightB2902B import KeysightB2902B

from utilities import *

vset = -3
vreset = 3
setpulse_width = 5e-4
resetpulse_width = 5e-4
readV = 0.2
npulse = 5
current_limit = 1e-3

points = []
points.append(vset)
points.append(vreset)
points = np.tile(points, npulse)
voltages = ",".join(points.astype('str'))
smu = KeysightB2902B("USB0::0x2A8D::0x9201::MY61390641::INSTR")
smu.reset()
smu.write(f":OUTP{smu.ch}:PROT 0")
smu.apply_voltage(compliance_current=current_limit)
smu.measure_current()
nPoints = len(points)
smu.configure_pulse_sweep(voltages,baseV=readV, pulse_width=setpulse_width)
smu.enable_source()
smu.clear_buffer(2*nPoints)
# get total points measured
# smu.ask(":TRAC:POIN:ACT?")
print("Started...")
smu.start_buffer()
while smu.get_trigger_state() == 'RUNNING':
    sleep(0.2)
    data = smu.get_trace_data()
    data2 = reshape(array(data.split(','), dtype=float), (-1, 4))
    print(len(data2))
smu.source_voltage = 0
smu.disable_source()
