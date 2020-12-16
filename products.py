#读档案
#strip 是把\n去掉
#split 是遇到豆点就切一刀，然后变成清单 or split切割完的结果是清单
#continue 的功能是跳到下一段，只能在if 或 with 用,而且通常会在最开始的时候写continue，不然执行完了在跳过就没有意义了
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,价格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])

print(products)

#让使用者输入
while True:
	p_n = input('plese insert products name: ')
	if p_n == 'q':
		break
	#这里是把东西装进小清单，然后在append进大清单
	p_p = input('please insert products price: ')
	s_p = []
	s_p.append(p_n)
	s_p.append(p_p)
	products.append(s_p)
	#更快速的清单写法是 products.append([p_n, p_p])
print(products)
#products[0][0]是大清单里第一个的小清单里的第一个
print(products[0][0])


#for loop搞清楚每个东西,在 products 里的每一个p 是大清单里的小清单 [['rice', '1.5'], ['meat', '2.5']] ，['rice', '1.5'] 为一个p
#p[0]是大清单里的小清单里的第一个东西

# 印出所有购买记录
for p in products:
	print(p[0],'price is:', p[1])

#f.write(p[0] + ',' + p[1] + '\n'):里面的逗号是把每个p都区隔开来
#with open('products.txt','w')as f: 没有products.txt会直接生成，有的话会直接覆盖
#with 解析：在电脑语言里有open就有close，with就是自动close，当程式码离开地28行后就会自动close了
#with 解析：离开了with就不能写入了，要在同一个block 

#写入档案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
