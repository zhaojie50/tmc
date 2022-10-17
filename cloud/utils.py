import os
import subprocess


def get_devices():
    """Get Devices."""
    dev_ids = []
    lists = subprocess.check_output(['adb', 'devices']).splitlines()
    for i in range(1, len(lists)-1):
        dev_ids.append(lists[i].decode('utf-8').split('\t')[0])
    return dev_ids


if __name__ == '__main__':
    print(get_devices())
