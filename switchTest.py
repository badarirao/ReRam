from MyKeysightB2902B import KeysightB2902B

from utilities import *

vset = -3
vreset = 3
setpulse_width = 5e-2
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
smu.configure_pulse_sweep(voltages,baseV=readV, pulse_width=setpulse_width)
smu.enable_source()
smu.clear_buffer((navg+1)*nPoints)
# get total points measured
# smu.ask(":TRAC:POIN:ACT?")
print("Started...")
smu.start_buffer()
data2 = []
wholeData = []
whole_writeData = []
whole_readData = []
buf = []
while smu.get_trigger_state() == 'RUNNING':
    data2 = buf
    buf = []
    while True:
        sleep(0.2)
        data = smu.ask(f"TRACe:data? curr").strip()
        data2.extend(np.reshape(np.array(data.split(','), dtype=float), (-1, 4)))
        data_length = len(data2)
        if data_length >= navg+1:
            trimmed_length = int(data_length/(navg+1))*(navg+1)
            buf = data2[trimmed_length:]
            data2 = np.array(data2[:trimmed_length])
            break
    writeData = np.array(data2[::smu.avg + 1])
    if smu.avg == 1:
        readData = data2[1::smu.avg + 1]
    else:
        readData = data2[np.mod(np.arange(len(data2)), smu.avg + 1) != 0]
        readData = np.reshape(readData, (-1, smu.avg, 4))
        readData = np.mean(readData, axis=1)
    whole_writeData.extend(writeData)
    whole_readData.extend(readData)
    wholeData.extend(data2)
    print(len(data2))
smu.source_voltage = 0
smu.disable_source()