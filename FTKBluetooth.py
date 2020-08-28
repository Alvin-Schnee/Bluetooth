import bluetooth

try:
    from gattlib import DiscoveryService
except ImportError:
    print("SYSTEM > Can't Import DiscoveryService. Bluetooth Low-Energy interactions will be deactivated.")
    DiscoveryService = None

def bluetooth_classic_scan(timeout=10):
    return bluetooth.discover_devices(duration=timeout, flush_cache=True, lookup_names=True, lookup_class=True)

def bluetooth_low_energy_scan(timeout=10):
    if DiscoveryService is None:
        print("SYSTEM > DiscoveryService disabled. Bluetooth Low-Energy interactions are deactivated.")
        return None

    svc = DiscoveryService()
    return svc.discover(timeout)