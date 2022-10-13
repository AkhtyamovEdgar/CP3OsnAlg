username = str(input('Введите свое имя: '))
usersurname = str(input('Введите свою фамилию: '))
userdate = int(input('Введите свой год рождения: '))
print(username + '_' + usersurname + '_' + str(userdate))
replace = username
username = usersurname
usersurname = replace
userdate += 60
print(username + '_' + usersurname + '_' + str(userdate))