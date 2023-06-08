# ## 1 vazifa
# user_name = input('Ismingizni kiriting: ')
# print(f'Assalomu alaykum, {user_name}')
#
# ## 2 vazifa
# num1 = input('Birinchi sonni kiriting: ')
# num2 = input('Ikkinchi sonni kiriting: ')
# num3 = int(input('Uchinchi sonni kiriting: '))
# result = int(num1) + int(num2) + num3
# print(f"Kiritilgan sonlar yig'indisi {result}")

### 3 vazifa
# olma = 50
# student = 6
# print('Har bir oquvchi uchun ' + str(olma // student) + 'tadan olma tegadi')
# print(f'Har bir oquvchi uchun {olma // student}tadan olma tegadi')
# print(f"Savatda {olma % student}ta olma qoldi")
#
# ### 4vazifa

# num = int(input('Son kiriting: '))
# print(f"{num} raqamidan kegin {num + 1} keladi")
# print(f"{num} raqamidan oldin {num - 1} keladi")

# print(str(num) + " raqamidan kegin " + str(num + 1) + " keladi")
# print(str(num) + " raqamidan oldin " + str(num - 1) + " keladi")

# str_1 = "bObUR MURTazoyEV"

# print(str_1.lower())  ### lower() -- barcha harflarni kichik holatga keltirib beradi
# print(str_1.capitalize())  ### capitalize() -- bu birinchi harfni katta qilib qaytaradi
# print(str_1.upper())  ### upper() -- barcha harflarni katta holatga keltirib beradi
# print(str_1.title())  ### title() -- har bir so'zdegi birinchi harfni katta qilib beradi

# print('O\'zbekiston')
# print("O\"zbekiston")
# print("O\tzbekiston")
# print("O\nzbekiston")

# num1 = 10  ### = o'zlashtiruvchi operator
# num2 = 14
# num3 = 17
#
# print(num1 > num2)
# print(num1 < num2)
# print(num1 <= num2)
# print(num1 >= num2)
# print(10 >= 10)

# print('a' > 'A')

# print(ord('a'))   ### ord -- simvolni ascii tartib raqamini chiqaradi
# print(chr(65))   ### chr -- tartib raqami ostidagi simvolni chiqaradi

# num1 = int(input('1 sonni kiriting: '))
# num2 = int(input('2 sonni kiriting: '))
#
# if num2 > num1:
#     print(f'{num2} {num1}dan katta')
# elif num2 < num1:
#     print(f"{num1} {num2}dan katta")
# else:
#     print(f"{num1} va {num2} teng")
########ABDURAHMON  == > abdurahmon
#
# name = input('Isningizni kiriting: ')
# if name.lower() == 'abdurahmon':
#     print('Xush kelibsiz')
# elif name.lower() == 'abdulloh':
#     print('Xush kelibsiz')
# if name.lower() == 'abdurahmon' or name.lower() == 'abdulloh':
#     print('Xush kelibsiz')
# else:
#     print('Siz admin emassiz!')

login = input('Loginizni kiriting: ')
password = input('Parolingizni kiriting: ')

if (login.lower() == 'abdurahmon' and password.lower() == '0203gh') or (login.lower() == "suhrob" and password.lower() == '12345a'):
    print('Xush kelibsiz')
else:
    print('Noto\'g\'ri login yoki parol kiritildi!')


