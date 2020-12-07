products = []
while True:
	p_n = input('plese insert products name: ')
	if p_n == 'q':
		break
	p_p = input('please insert products price: ')
	s_p = []
	s_p.append(p_n)
	s_p.append(p_p)
	products.append(s_p)
	#更快速的清单写法是 products.append([p_n, p_p])
print(products)
print(products[0][0])


#for loop搞清楚每个东西,在 products 里的每一个p 是大清单里的小清单 [['rice', '1.5'], ['meat', '2.5']] ，['rice', '1.5'] 为一个p
for p in products:
	print(p[0])