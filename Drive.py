import psutil

def get_disk_stats():
    disk_stats = []
    for partition in psutil.disk_partitions(all=True):
        usage = psutil.disk_usage(partition.mountpoint)
        total_gb = usage.total / (1024 ** 3)
        used_gb = usage.used / (1024 ** 3)
        used_percentage = (usage.used / usage.total) * 100
        threshold_80_percent_gb = total_gb * 0.80
        gb_to_80_percent_full = threshold_80_percent_gb - used_gb
        disk_stats.append((partition.device, total_gb, used_gb, used_percentage, gb_to_80_percent_full))
    return disk_stats

def print_disk_stats():
    disk_stats = get_disk_stats()
    for disk, total_gb, used_gb, used_percentage, gb_to_80_percent_full in disk_stats:
        print(f"Disk: {disk}, Total: {total_gb:.2f} GB, Used: {used_gb:.2f} GB ({used_percentage:.2f}%), To 80% full: {gb_to_80_percent_full:.2f} GB")
print_disk_stats()