
edge_list=['192.168.1.1','192.168.1.2']
f=open('hosts','a')

for i in range(100):
    for edge in edge_list:
        f.write(edge+f' domain{i}.com\n')