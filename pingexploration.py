from pythonping import ping

print('test 1')
print(ping('127.0.0.1', count=1))
if ping('127.0.0.1', count=1):
    print('true')
else:
    print('false')


print('test 2')
print(ping('192.168.200.1', count=1))
if ping('192.168.200.1', count=1):
    print('true')
else:
    print('false')

holder = ping('192.168.200.1', count=1, verbose = False)
holder2 = ping('192.168.200.1', count=1, verbose = True)

print('holder = ', holder)
print('holder2 = ', holder2)

holder3 = ping('127.0.0.1', count=1, verbose = False)
holder4 = ping('127.0.0.1', count=1, verbose = True)

print('holder3 = ', holder3)
print('holder4 = ', holder4)

print(str(holder4)[0:4])