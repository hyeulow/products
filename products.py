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
