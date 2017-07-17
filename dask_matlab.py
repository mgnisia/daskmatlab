from dask.distributed import Client
list = [...] ##List with matlab files
client = Client()
def func1(self):
    import scipy.io as sio
    matfile = sio.loadmat(self)
    data = matfile['variable']['data'][0,0]
return data
client.gather(client.map(func1,list))
