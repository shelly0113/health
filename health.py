def get_bmi(height, weight):
    height = height/100
    bmi = round(weight/height**2, 1)
    print(f'你的BMI為{bmi}')


def get_bmr(sex, height, weight, age):
    if sex == '男':
        bmr = 66 + (13.7 * weight + 5 * height - 6.8 * age)
    elif sex == '女':
        bmr = 655 + (9.6 * weight + 1.8 * height - 4.7 * age)
    bmr = round(bmr, 2)
    return bmr


def get_tdee(times, weight, height, age, sex):
    bmr = get_bmr(sex, height, weight, age)
    tdee = bmr * times
    tdee = round(tdee, 2)
    return tdee


print('歡迎使用綜合健康計算機~')
print('(1)計算BMI')
print('(2)計算BMR')
print('(3)計算TDEE')
item = input('請輸入計算項目 (輸入1 or 2 or 3)')
if item == '1':
    height = float(input('請輸入身高: '))
    weight = float(input('請輸入體重: '))
    bmi = get_bmi(height, weight)
    print(bmi)
elif item == '2':
    sex = input('請輸入性別: ')
    height = float(input('請輸入身高: '))
    weight = float(input('請輸入體重: '))
    age = int(input('請輸入年齡: '))
    bmr = get_bmr(sex, height, weight, age)
    print(f'你的BMR: {bmr}')
else:
    sex = input('請輸入性別: ')
    height = float(input('請輸入身高: '))
    weight = float(input('請輸入體重: '))
    age = int(input('請輸入年齡: '))
    print('(1)久坐、幾乎沒運動')
    print('(2)每週低強度運動1~3次')
    print('(3)每週中強度運動3~5次')
    print('(4)每週高強度運動6~7次')
    print('(5)努力密集工作或是每天高強度運動')
    excercise = input('請輸入運動量: ')
    times = 0
    if excercise == '1':
        times = 1.2
    elif excercise == '2':
        times = 1.375
    elif excercise == '3':
        times = 1.55
    elif excercise == '4':
        times = 1.725
    else:
        time = 1.9
    tdee = get_tdee(times, weight, height, age, sex)
    print(f'你的TDEE: {tdee}')
