import socket
import pickle

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print(f"Server running on port {PORT}")

while True:
    conn, addr = s.accept()
    print("Connected by", addr)

    data = conn.recv(4096)
    task = pickle.loads(data)

    A = task['A']
    B = task['B']

    # Matrix multiplication logic
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    conn.send(pickle.dumps(result))
    conn.close()
