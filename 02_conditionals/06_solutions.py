distance = 10

if distance < 3:
    transport = "walk"
elif distance <= 15:
    transport = "bike"
else:
    transport = "car"

print("lord recommends you the transport:", transport)