import os
import json
import ipaddress


# json_path = os.getcwd() + '/'+'params.json'
# with open(json_path, mode='r') as f:
#     content = json.loads(f.read())
    
# print(content.get('repository_params1', None))

ip1 = '192.168.1.1'+'/24'
obj = ipaddress.ip_interface(ip1)

print(str(obj.ip))
print(obj.network)

