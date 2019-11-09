ESP32 can communicate with other device via Bluetooth using the module HC-06 as slave.

# Schematics
![esp32_HC06_bb](https://user-images.githubusercontent.com/20991217/68524333-7654aa00-02ce-11ea-8a7c-faf674b3c781.png)

# HC-06 configuration
You can configuring the module HC-06 by runnig the file BT_setup.py
In this progran you can verify that the hardware is working.In this program you can modify parameters such as name, PIN code and communication speed in baudrate.
![bt1](https://user-images.githubusercontent.com/20991217/68524521-adc45600-02d0-11ea-971d-c3fee5254bec.png)

# Pairing Bluetooth module HC-06
To pair the module HC-06 to the device run the file BT_hc06.py 

# Connecting 2 ESP32 via serial communication (RS-232)
You can communicate between 2 controllers using the code example: BT_hc06_READ_DATA.py and BT_hc06_SEND_DATA.py
![esp32_UART_bb](https://user-images.githubusercontent.com/20991217/68524611-a487b900-02d1-11ea-9bab-0c39e2ec8508.png)

