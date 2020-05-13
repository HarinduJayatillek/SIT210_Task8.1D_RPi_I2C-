import smbus
import time

bus = smbus.SMBus(1)

bus.write_byte_data(0x53, 0x2C, 0x0A)
bus.write_byte_data(0x53, 0x2D, 0x08)
bus.write_byte_data(0x53, 0x31, 0x08)

time.sleep(0.5)
while True:

	# X-Axis LSB, X-Axis MSB
	xdata0 = bus.read_byte_data(0x53, 0x32)
	xdata1 = bus.read_byte_data(0x53, 0x33)

	# Convert the data 
	xAccl=((xdata1 & 0x03)*256)+xdata0

	if xAccl > 511:
		xAccl -= 1024

	# Y-Axis LSB, Y-Axis MSB
	ydata0 = bus.read_byte_data(0x53, 0x34)
	ydata1 = bus.read_byte_data(0x53, 0x35)

	# Convert the data 
	yAccl=((ydata1 & 0x03)*256)+ydata0

	if yAccl > 511:
		yAccl -= 1024

	# Z-Axis LSB, Z-Axis MSB
	zdata0 = bus.read_byte_data(0x53, 0x36)
	zdata1 = bus.read_byte_data(0x53, 0x37)

	# Convert the data 
	zAccl=((zdata1 & 0x03)*256)+zdata0

	if zAccl > 511:
		zAccl -= 1024

	# Output data 
	print "Acceleration in X-Axis : %d" %xAccl
	print "Acceleration in Y-Axis : %d" %yAccl
	print "Acceleration in Z-Axis : %d" %zAccl
	print "\n"

	time.sleep(2)
