import subprocess

def get_ip_addresses():
    ip_addresses = []
  
    output = subprocess.run(['ipconfig'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    lines = output.split('\n')

    for line in lines:
      if 'IPv4' in line:
        parts = line.split(':')
        ip_addresses.append(parts[1].strip())
    return ip_addresses

print(get_ip_addresses())
