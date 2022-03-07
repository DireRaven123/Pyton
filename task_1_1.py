user_number = int(input('Введите количество секунд '))
if user_number <= 60:
    print(user_number, 'секунд')
elif user_number <= 3600:
    min = user_number // 60
    sec = user_number % 60
    print(min, ' минут ', sec, 'секунд')
elif user_number <= 86400:
    hour = user_number // 3600
    min = user_number // 60 - 60 * hour
    sec = user_number % 60
    print(hour, 'часов', min,' минут ', sec,'секунд')
elif user_number >= 86400:
    day = user_number // 86400
    hour = user_number // 3600 - 24 * day
    min = user_number // 60 - 60 * (user_number // 3600)
    sec = user_number % 60
    print(day, 'дней', hour, 'часов', min, ' минут ', sec, 'секунд')



