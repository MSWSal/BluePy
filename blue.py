import bluetooth

nearby_dev= bluetooth.discover_devices(lookup_names=True)

for addr,name in nearby_dev:
    print("name=",name)
    print("addr=", addr)

     
