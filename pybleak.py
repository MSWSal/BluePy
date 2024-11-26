import asyncio
from bleak import BleakScanner
from datetime import datetime

async def discover_devices_with_time():
    print("Scanning for Bluetooth devices...")
    start_time = datetime.now()
    discovered_devices = {}

    def detection_callback(device, advertisement_data):
        # Calculate the time since scanning started
        elapsed_time = datetime.now() - start_time
        if device.address not in discovered_devices:
            discovered_devices[device.address] = device
            print(f"Discovered: {device.name} ({device.address}) at {elapsed_time.total_seconds():.2f} seconds")

    # Create scanner with callback
    scanner = BleakScanner(detection_callback)
    await scanner.start()
    await asyncio.sleep(5)  # Adjust scanning duration as needed
    await scanner.stop()

    print("\nScan complete. Devices discovered:")
    for device in discovered_devices.values():
        print(f"{device.name} ({device.address})")

# Run the discovery
asyncio.run(discover_devices_with_time())
