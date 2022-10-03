from MyKeysightB2902B import KeysightB2902B

from utilities import *

vset = -3
vreset = 3
setpulse_width = 6e-2
resetpulse_width = 5e-2
readV = 0.2
npulse = 5
current_limit = 1e-3
navg = 5
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
smu.avg = navg
smu.configure_pulse(baseV=readV, pw1=setpulse_width, pw2=resetpulse_width)
smu.enable_source()
whole_writeData = []
whole_readData = []
print("Started...")
i = 0
while i < npulse:
    smu.set_pulse1(setpulse_width, vset)
    smu.start_buffer()
    smu.wait_till_done()
    setData = smu.get_trace_data()
    smu.set_pulse2(resetpulse_width, vreset)
    smu.start_buffer()
    smu.wait_till_done()
    resetData = smu.get_trace_data()
    setData = np.reshape(np.array(setData.split(','), dtype=float), (-1, 4))
    resetData = np.reshape(np.array(resetData.split(','), dtype=float), (-1, 4))
    volt = [setData[0][0], resetData[0][0]]  # actual voltage applied
    avgreadData_set = np.mean(setData[1:], axis=0)
    avgreadData_reset = np.mean(resetData[1:], axis=0)
    rc = np.array([avgreadData_set[1], avgreadData_reset[1]])  # read current
    rc[rc==0] = 1e-20
    resistance = np.divide(readV , rc)
    whole_writeData.extend([setData[0], resetData[0]])
    whole_readData.extend([avgreadData_set, avgreadData_reset])
    i += 1
print("Finished")
whole_writeData = np.array(whole_writeData)
whole_readData = np.array(whole_readData)
smu.source_voltage = 0
smu.disable_source()