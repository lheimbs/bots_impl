import numpy

x = -2
y = -3

fov = 5
size = 12

map = numpy.zeros((size, size))
view = numpy.ones((fov, fov))

# slices map
smxa=slice(0,fov+x) #0,2
smxb=slice(size+x, size) #9,12

smya=slice(0,fov+y) #0,2
smyb=slice(size+y, size) #9,12

# slices view
svxa=slice(x*-1,fov) #3,5
svxb=slice(0, x*-1) #0,3

svya=slice(y*-1,fov) #3,5
svyb=slice(0, y*-1) #0,3

map[smxa, smya] = view[svxa, svya] #schwarz
map[smxa, smyb] = view[svxa, svyb] #rot
map[smxb, smyb] = view[svxb, svyb] #blau
map[smxb, smya] = view[svxb, svya] #grün

print(map)