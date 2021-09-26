import socket
from datetime import datetime
import argparse
import sys

# Creates the parser
parser = argparse.ArgumentParser(prog="scanner", description="Scans the specified ports on the target host.")

# Add the arguments
parser.add_argument("--hostname", metavar="hostname", type=str, help="The hostname of the target.")
parser.add_argument("--hostIP", metavar="host ip", type=str, help="The name of the ")
parser.add_argument("startport", metavar="startport", type=int, help="Port number that you want to start scanning at.")
parser.add_argument("endport", metavar="endport", type=int, help="Port number that you want to stop scanning at.")

args = parser.parse_args()


if args.hostname:
    remoteServer = args.hostname
    remoteServerIP = socket.gethostbyname(remoteServer)
elif args.hostIP:
    remoteServerIP = args.hostIP
else:
    print("Please enter either the hostname or the host ip")
    sys.exit()

    
print("-" * 60)
print("Please wait, scanning remote host " + remoteServerIP)
print("-" * 60)

start_port = args.startport
end_port = args.endport

# Gets the time the scan started at.
t1 = datetime.now()

print("Started scanning ports {0} to {1} at ".format(start_port, end_port) + str(t1.replace(microsecond = 0)))


total_ports_open = 0
# Scans ports in user defined range.
try:
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {0}:          Open".format(port))
            total_ports_open += 1
        sock.close()

except KeyboardInterrupt:
    print("Forced exit confirmed. Exiting.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Could not connect to the server.")
    sys.exit()

# Gets the time after the scan is completed.
t2 = datetime.now()

total_time_taken = t2 - t1
print("Total ports open in the defined range: {0}".format(total_ports_open))
print("Scanning completed in " + str(total_time_taken.total_seconds() * 1000) + "ms.")
