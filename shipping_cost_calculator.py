
# This is a program that asks the user for the weight of their package and 
# then tells them which method of shipping is cheapest and how much it will 
# cost to ship their package

# The cheapest way to ship 4.8 pound package is using ground shipping and it will cost $34.40.
# The cheapest way to ship a 41.5 pound package is using premium ground shipping and it will cost $125.00.

def ground_shipping(weight):
  flat_charge = 20.00
  premium_shipping = 125.00
  if (weight <= 2):
    cost = (weight * 1.50) + flat_charge
  elif (2 < weight <= 6):
    cost = (weight * 3.00) + flat_charge
  elif (6 < weight <= 10):
    cost = (weight * 4.00) + flat_charge
  else:
    cost = (weight * 4.75) + flat_charge
  return cost,premium_shipping

def drone_shipping(weight):
  flat_charge = 0.00
  if (weight <= 2):
    cost = weight * 4.50
  elif (2 < weight <= 6):
    cost = weight * 9.00
  elif (6 < weight <= 10):
    cost = weight * 12.00
  else:
    cost = weight * 14.25
  return cost

def cheapest_shipping(weight):
  ground, premium = ground_shipping(weight)
  drone = drone_shipping(weight)
  if (ground < premium) and (ground <drone):
    return ("ground shipping = $ " + str(ground))
  elif (drone < premium) and (drone < ground):
    return ("drone shipping = $ " + str(drone))
  else:
    return ("premium shipping = $ " + str(premium))

#ground_shipping, premium_shipping = ground_shipping(8.4)
#rone_shipping = drone_shipping(1.5)
cheapest_shipping = cheapest_shipping(41.5)
#print("Ground shipping cost = $" + str(ground_shipping))
# should print "Ground shipping cost = $53.60"
#print("Premium shipping cost = $" + str(premium_shipping))
# should print "Premium shipping cost = $125.00"
#print("Drone shipping cost = $" + str(drone_shipping))
# should print "Drone shipping cost = $6.75"
print("Cheapest shipping is " + str(cheapest_shipping))
# should print "Cheapest shipping is premium shipping = $125.00"
