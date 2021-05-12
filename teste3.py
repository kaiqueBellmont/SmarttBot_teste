import threading


def hello_world():
    threading.Timer(5, hello_world).start()  # called every minute
    print("Hello, World!")


print('tsttt')
hello_world()
