import bluetooth

def send_data_to_device(bd_addr, port, data_to_send):
    try:
        # Create a Bluetooth socket
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        
        # Connect to the known device
        print(f"Attempting to connect to {bd_addr} on port {port}...")
        sock.connect((bd_addr, port))
        print(f"Connected to {bd_addr}")

        # Send the data
        sock.send(data_to_send)
        print(f"Data sent: {data_to_send}")

    except bluetooth.btcommon.BluetoothError as e:
        print(f"Bluetooth error: {e}")
    
    finally:
        # Close the socket connection
        sock.close()
        print("Connection closed.")

# Replace with your known device address and port
known_device_address = "A0:27:B6:65:CE:64"  # Replace with the actual MAC address of your phone
port = 1  # Commonly used port for RFCOMM
data_to_send = "Hello from Python!"  # Replace with your actual data

# Call the function to send data
send_data_to_device(known_device_address.strip(), port, data_to_send)