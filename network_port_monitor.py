import psutil
import pandas as pd
from datetime import datetime

def monitor_ports():
    # Fetch all network connections
    connections = psutil.net_connections(kind='inet')
    
    port_data = []
    
    for conn in connections:
        # Get process info safely
        try:
            process = psutil.Process(conn.pid)
            process_name = process.name()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            process_name = "Unknown/System"
            
        # Organize data
        port_info = {
            "Local Address": conn.laddr.ip,
            "Port": conn.laddr.port,
            "Remote Address": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A",
            "Status": conn.status,
            "PID": conn.pid,
            "Process Name": process_name
        }
        port_data.append(port_info)

    # Convert to a DataFrame for clean visualization
    df = pd.DataFrame(port_data)
    
    print(f"--- Network Port Report ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---")
    if not df.empty:
        # Sorting by Port number for readability
        print(df.sort_values(by="Port").to_string(index=False))
    else:
        print("No active connections found.")

if __name__ == "__main__":
    monitor_ports()