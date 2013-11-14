x1 = 10
y1 = 10
x2 = 20
y2 = 20

x = 0
y = 50 

if (x<=x1 and y<=y1) or (x>=x2 and y>=y2):
	print 'punkt ({},{}) asub piirkonnas.'.format(x, y)	
else:
	print 'punkt ({},{}) ei asu piirkonnas.'.format(x, y)
