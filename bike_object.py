# Define a Bike class.

class Bike:
	def __init__(self, clour, frame_material):
		self.colour = clour
		self.frame_material = frame_material

	def brake (self):
		print (self.colour, "Braking!!!")

# Let's create instances.

red_bike = Bike('red', 'Carbon Fiber')
blue_bike = Bike('blue', 'Steel')

print (red_bike.colour)
print (red_bike.frame_material)
print (blue_bike.colour)
print (blue_bike.frame_material)

red_bike.brake()
blue_bike.brake()


