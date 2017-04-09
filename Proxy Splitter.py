with open('proxies.txt') as Proxies:
    proxies = Proxies.read().splitlines()


for proxysplit in proxies:
    proxy = proxysplit.split(':')
    ips = proxy[0]
    port = proxy[1]
    user = proxy[2]
    password = proxy[3]
    with open('proxies.txt') as Proxies:
        proxies = Proxies.read().splitlines()
    with open('proxy.txt', 'a') as f:
        f.write('{}:{}@{}:{}'.format(user, password,ips,port) + '\n')
        f.close()


