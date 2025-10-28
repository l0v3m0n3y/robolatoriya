import requests
class Client():
	def __init__(self):
		self.api="https://tools-api.robolatoriya.com"
	def compliment_for_girl(self):
		return requests.get(f"{self.api}/compliment?type=2").json()
	def compliment_for_men(self):
		return requests.get(f"{self.api}/compliment?type=3").json()
	def compliment_universal(self):
		return requests.get(f"{self.api}/compliment?type=1").json()