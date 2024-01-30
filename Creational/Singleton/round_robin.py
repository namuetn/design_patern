"""
Ứng dụng:
- Quản lý tài nguyên chung
- dữ liệu cấu hình
- quản lý tài nguyên global

"""

class RoundRobin():
    def __init__(self) -> None:
        self.servers = []
        self.index = 0

    def add_server(self, server):
        self.servers.append(server)

    def get_next_server(self):
        if len(self.server) == 0:
            raise ValueError("No server available")
        
        SERVER = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)

        return SERVER
    
