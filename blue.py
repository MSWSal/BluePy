import bluetooth
import time
import bluetooth
import time

# List to store discovered devices
discovered_devices = []

# Start the overall discovery process
start_time = time.time()  # Record the overall start time

# Discover devices in a loop
for _ in range(5):  # Try multiple scans to increase chances of discovery
    print("Scanning for devices...")
    nearby_dev = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)

    for addr, name in nearby_dev:
        if (addr, name) not in discovered_devices:  # Check if device is already discovered
            # Record the start time for this device discovery
            device_start_time = time.time()
            
            # Simulating a delay for processing (you can replace this with actual processing)
            time.sleep(0.1)  # Small delay to simulate processing
            
            # Record the end time for this device discovery
            device_end_time = time.time()

            # Calculate the time taken for this specific device discovery
            device_time = device_end_time - device_start_time
            
            print(f"Discovered Device: Name = {name}, Address = {addr}, Discovery Time = {device_time:.4f} seconds")
            discovered_devices.append((addr, name))  # Add to discovered list

# Calculate total discovery time
total_time = time.time() - start_time

print(f"\nTotal discovery time for all devices: {total_time:.2f} seconds")

     
