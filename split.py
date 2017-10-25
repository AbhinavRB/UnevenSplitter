import json

EVERYONE_ELSE = "__rest"

class Splitter:

	def __init__(self, total, num_sharers, claimed_items):
		self.total = float(total)
		self.num_sharers = int(num_sharers)
		self.claimed_items = claimed_items	

	def calc_split(self):
		self.__calculate_claimed_total()
		self.__calculate_base()
		self.__split()
		return self.__round_and_finish()

	def __calculate_claimed_total(self):		
		self.claimed_total = sum([float(item['price']) for item in self.claimed_items])		

	def __calculate_base(self):
		"""calculate base amount that everyone has to pay"""

		self.base_total          = self.total - self.claimed_total
		self.base_total_per_head = self.base_total / self.num_sharers

	def __split(self):
		"""calculate everyone's total share"""

		self.share = {}
		
		for item in self.claimed_items:	
			for claimer in item['claimers'].split():
				if(claimer in self.share):
					self.share[claimer] += float(item['price']) / len(item['claimers'].split())
				else:			
					self.share[claimer] = float(item['price']) / len(item['claimers'].split())

		for claimer in self.share:
			self.share[claimer] += self.base_total_per_head

		# if some people didn't participate in any claim
		if(len(self.share) < self.num_sharers):
			self.num_base_sharers = self.num_sharers - len(self.share)
			self.share[EVERYONE_ELSE] = self.base_total_per_head


	def __round_and_finish(self):
		"""round up final shares to two decimal places and print answer"""

		total_after_rounding = 0
		for claimer in self.share:
			if claimer == EVERYONE_ELSE:
				total_after_rounding += round(self.num_base_sharers * self.share[claimer], 2)
			else:
				total_after_rounding += round(self.share[claimer], 2)
			# print("{} pays ${:.2f}".format(claimer, round(self.share[claimer], 2)))
			self.share[claimer] = "{:.2f}".format(round(self.share[claimer], 2))

		# print("Total amount after rounding off = ${:.2f}\n".format(round(total_after_rounding, 2)))		

		total_after_rounding = "{:.2f}".format(round(total_after_rounding, 2))
		return json.dumps({'share': self.share, 'total': total_after_rounding})

if __name__ == '__main__':	
	splitter = Splitter()
	splitter.calc_split()