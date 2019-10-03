<p align="center">
Photovoltaic power Simulator
=============================
Meter: This produce messages to the broker with random but continuous values from
0 to 9000 Watts. 
PV simulator: This listen to the broker for the meter values, generate a simulated PV
power value and the last step is to add this value to the meter value and output the result.

Result is saved in the file with all data: timestamp, meter power value, PV power value and the sum of the powers (meter + PV). 

Configuration
=============
1. Download and install rabbitMQ from https://www.rabbitmq.com/
2. Make sure, you've latest python and pip version: 'sudo apt-get update && sudo apt-get upgrade'
3. Install RabbitMQ library for Python: 'sudo pip install pika'
4. From console run file 'run.py': 'python run.py'
<\p>
