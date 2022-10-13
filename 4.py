count_years = int(input('Введите количество лет: '))
count_exhibits = int(input('Введите количество экспонатов: '))
res_exhibits = count_years * 35040
res_years = count_exhibits // 35040
res_minutes = count_exhibits * 5
res_seconds = count_exhibits * 300
print('За', count_years, 'лет будет просмотрено', res_exhibits, 'экспонатов')
print('Для просмотра', count_exhibits, 'экспонатов понадобится', res_years, 'лет')
print('Для просмотра', count_exhibits, 'экспонатов понадобится', res_minutes, 'минут')
print('Для просмотра', count_exhibits, 'экспонатов понадобится', res_seconds, 'секунд')

#В год при 8-восьми часовом нахождении в музее и рассматривая каждую картину не более чем 5 минут,
#в год человек может просмотреть 35040
# за один час человек может посмотреть 12 картин
# за одну минуту человек может посмотреть 1/5 картин
# за одну секунду человек может посмотреть 1/300 картин



