#!/usr/bin/python3

#
# Access 2102 SRAM memory chip via GPIO
#

class Sram2102:

	def __init__(self):
		self.memarray = [ [0] * 32] * 32
		self.valid = False

	def dump(self):
		if (not self.valid):
			print("chip not read")
			return
		print("2102 RAM")
		for row in self.memarray:
			for bit in row:
				print(bit, end=" ")
			print()

	def setbit(self, address):
		if (address > 1023):
			raise IndexError("max address is 0x3FF")

	def clrbit(self, address):
		if (address > 1023):
			raise IndexError("max address is 0x3FF")

	def getbit(self, address):
		if (address > 1023):
			raise IndexError("max address is 0x3FF")

	def write(self):
		raise NotImplementedError

	def read(self):
		raise NotImplementedError
#
# main
#

chip = Sram2102()

# chip.read()

# chip.dump()

chip.clrbit(0x400);
