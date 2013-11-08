import rpyc,sys

def rpyc_call():
    conn = rpyc.connect('localhost',8888)
    myval = conn.root.func1()   # Special 'root' of connection
    print myval


if __name__ == '__main__':
    rpyc_call()
