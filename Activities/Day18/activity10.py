data={'a':1,'b':2,'c':1}
print({v:tuple(k for k in data if data[k]==v) for v in set(data.values())})