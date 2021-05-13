import threading


def hello_world():
      # called every minute
    print("Hello, World!")
    threading.Timer(5, hello_world).start()


print('tsttt')
hello_world()
