# password = 12345
n = 0
while n < 3:
		password = input('請輸入密碼: ')
		if password == '12345':
			print('你答對囉')
			break
		else:
			if n == 2:
				print('你沒機會囉')
				break
			else:
				n = n + 1
				print('你還有', 3-n, '次機會')