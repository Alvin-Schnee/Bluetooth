from FTKBluetooth import bluetooth_classic_scan, bluetooth_low_energy_scan

if __name__ == "__main__":
    scan_duration = 5

    scanned_devices = bluetooth_classic_scan(scan_duration)
    if scanned_devices:
        for device in scanned_devices:
            print("fuwaaa ", device)

    dev_ble = bluetooth_low_energy_scan(scan_duration)
    if dev_ble:
        for u, n in dev_ble.items():
            print(u, n)