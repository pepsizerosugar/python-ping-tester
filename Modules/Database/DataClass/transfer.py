from dataclasses import dataclass


@dataclass
class transfer:
    server_name: str
    server_region: str
    server_ip: str
    server_list: []
