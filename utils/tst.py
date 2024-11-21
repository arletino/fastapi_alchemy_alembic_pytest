with open('tmp.txt', 'wb') as f:
    f.truncate(10000024)
with open('tmp.txt', 'r') as f:
    b = f.readlines()
