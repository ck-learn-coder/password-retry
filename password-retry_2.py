password = 'a123456'
count = 1

while count < 4:
	usertest = input('請輸入密碼:')
	if usertest != password and count < 3:
	   print('密碼錯誤! 還有', 3 - count ,'次機會輸入密碼')
	   #print('還有可嘗試機會:', 3 - count)
	   count = count +1
	elif usertest != password and count == 3:
		print('不能再嘗試輸入密碼了!')
		break
	elif usertest == password:
		print('密碼正確')
		break