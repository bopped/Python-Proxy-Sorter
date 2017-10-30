with open('proxies.txt') as Proxies:
    proxies = Proxies.read().splitlines()


for proxysplit in proxies:
    proxy = proxysplit.split(':')
    ips = proxy[0]
    port = proxy[1]
    user = proxy[2]
    password = proxy[3]
    with open('proxy.txt', 'a') as f:
        f.write('%s:%s@%s:%s' % (user, password, ips, port) + '\n')
        f.close()
