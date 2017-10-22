EVERYONE_ELSE = "Everyone (else)"

# classes 
class Item:

	def __init__(self, name, price, claimers):
		self.name = name
		self.price = price
		self.claimers = claimers

class Splitter:

	def __init__(self, total, num_sharers, claimed_items):
		self.total = total
		self.num_sharers = num_sharers
		self.claimed_items = claimed_items		

	def split(self):
		self.__calculate_claimed_total()
		self.__calculate_base()
		self.__split()
		self.__round_and_finish()

	def __calculate_claimed_total():
		self.claimed_total = sum([item.price for item in claimed_items])

	def __calculate_base(self):
		"""calculate base amount that everyone has to pay"""

		self.base_total          = self.total - self.claimed_total
		self.base_total_per_head = self.base_total / self.num_sharers

	def __split(self):
		"""calculate everyone's total share"""

		self.split = {}
		
		for item in self.claimed_items:	
			for claimer in item.claimers:			
				if(claimer in self.split):
					self.split[claimer] += item.price / len(item.claimers)
				else:			
					self.split[claimer] = item.price / len(item.claimers)

		for claimer in self.split:
			self.split[claimer] += self.base_total_per_head

		# if some people didn't participate in any claim
		if(len(self.split) < self.num_sharers):
			self.num_base_sharers = self.num_sharers - len(self.split)
			self.split[EVERYONE_ELSE] = self.base_total_per_head


	def __round_and_finish(self):
		"""round up final shares to two decimal places and print answer"""

		total_after_rounding = 0
		for claimer in self.split:
			if claimer == EVERYONE_ELSE:
				total_after_rounding += round(self.num_base_sharers * self.split[claimer], 2)
			else:
				total_after_rounding += round(self.split[claimer], 2)
			print("{} pays ${:.2f}".format(claimer, round(self.split[claimer], 2)))

		print("Total amount after rounding off = ${:.2f}\n".format(round(total_after_rounding, 2)))

if __name__ == '__main__':	
	splitter = Splitter()
	splitter.split()