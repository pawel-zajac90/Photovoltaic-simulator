from pv_power import *


simulator = PVSimulator()
meter = Meter()
meter.run() # Starting Meter.run from meter_c.py, which send messages to rabbitMQ

# Creating lists
watts_value_list = simulator.read_from_rabbitMQ()
pv_power_value_list = simulator.main()
watts_PV_list = create_watts_pv_list(watts_value_list, pv_power_value_list)

save(watts_value_list, pv_power_value_list, watts_PV_list) # Saving data to the file.

