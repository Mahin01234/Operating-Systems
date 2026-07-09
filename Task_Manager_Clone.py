import psutil
import time
import os
import sys





def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




try:
    while True:
        clear_screen()
        print("{:<30} {:<10} {:<10} {:<10}".format("Process Name", "PID", "CPU %", "Memory %"))
        print("-" * 70)





        # Get list of processes (snapshot)
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
            try:
                # Get CPU percent with a short interval (non-blocking)
                cpu = proc.cpu_percent(interval=0.0)  # or 0.1 for better accuracy
                mem = proc.info['memory_percent']
                processes.append((
                    proc.info['name'][:25],
                    proc.info['pid'],
                    cpu,
                    mem
                ))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue





        # Sort by CPU usage (descending) to show busiest first
        processes.sort(key=lambda x: x[2], reverse=True)




        for name, pid, cpu, mem in processes[:50]:  # limit to top 50
            print("{:<30} {:<10} {:<10.2f} {:<10.2f}".format(
                name, pid, cpu, mem
            ))




        time.sleep(5)





except KeyboardInterrupt:
    clear_screen()
    print("Monitoring stopped.")
    sys.exit(0)