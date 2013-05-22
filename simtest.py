from drivers import SimulatorDriver


driver = SimulatorDriver('simulator1')
driver.open()
while True:
	print driver.recv()
driver.close()
