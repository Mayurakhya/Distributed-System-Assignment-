import socket
import pickle
from matrix_input import A, B

servers = [
    ('localhost', 5000),
    ('localhost', 5001),
    ('localhost', 5002)
]

results = []

for server in servers:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(server)

    task = {
        'A': A,
        'B': B
    }

    s.send(pickle.dumps(task))
    data = s.recv(4096)

    result = pickle.loads(data)
    results.append(result)

    s.close()

print("Received results from servers:")
for r in results:
    print(r)
