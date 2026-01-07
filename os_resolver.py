import platform
import sys

def get_os_info():
    os_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()

    print("="*40)
    print(f"Operating System: {os_name}")
    print(f"Release:          {os_release}")
    print(f"Full Version:     {os_version}")
    print("="*40)

    # OS-Specific detailed checks
    if os_name == "Windows":
        # Returns: (release, version, csd, ptype)
        # Example: ('10', '10.0.19041', 'SP0', 'Multiprocessor Free')
        win_ver = platform.win32_ver()
        print(f"Windows Details:  {win_ver[0]} (Build {win_ver[1]})")

    elif os_name == "Darwin":
        # Returns: (release, versioninfo, machine)
        # Example: ('10.15.7', ('', '', ''), 'x86_64')
        mac_ver = platform.mac_ver()
        print(f"macOS Version:    {mac_ver[0]}")

    elif os_name == "Linux":
        # Attempt to get Distribution Name (e.g., Ubuntu, CentOS)
        # 'freedesktop_os_release' is available in Python 3.10+
        try:
            if hasattr(platform, 'freedesktop_os_release'):
                os_info = platform.freedesktop_os_release()
                distro_name = os_info.get('PRETTY_NAME') or os_info.get('NAME')
                print(f"Distribution:     {distro_name}")
            else:
                # Fallback for older Python versions
                # Reading the common release file directly
                with open("/etc/os-release") as f:
                    for line in f:
                        if line.startswith("PRETTY_NAME="):
                            # CLEANER FIX: Process the string outside the f-string
                            dist_name = line.split('=')[1].strip().strip('"')
                            print(f"Distribution:     {dist_name}")
                            break
        except Exception:
            print("Distribution:     Could not determine specific distro")

if __name__ == "__main__":
    get_os_info()