"""
Возьмите любые 1-3 задания из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.

"""

import logging
import argparse

logging.basicConfig(filename='Log/Data_log_task02.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{asctime} - {levelname} - {msg}',
                    style='{',
                    level=logging.INFO)

parser = argparse.ArgumentParser(description='Проверка заданной даты.')
parser.add_argument('date', type=str, help=('Принемаем заданную дату в формате (дд.мм.гггг)'))

args = parser.parse_args()
input_date = args.date

def valid_date(date):
    try:
        day, month, year = map(int, date.split('.'))
        if year in range(1, 10000) and month in range(1, 13) and day in range(
                1, 32):
            if month == 2:
                if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                    if day in range(1, 30):
                        logging.info(f"{date} - корректная дата.")
                        return True, "Корректная дата."
                    else:
                        logging.error(
                            f"Недопустимый день, дата: {date} - некорректа.")
                        return False, "Недопустимый день."
                elif day in range(1, 29):
                    logging.info(f"{date} - корректная дата.")
                    return True, "Корректная дата."
                else:
                    logging.error(f"Недопустимый день, дата: {date} - некоректа.")
                    return False, "Недопустимый день."
            if month in [1, 3, 5, 7, 8, 10, 12]:
                logging.info(f"{date} - корректная дата.")
                return True, "Корректная дата."
            else:
                if day in range(1, 31):
                    logging.info(f"{date} - корректная дата.")
                    return True, "Корректная дата"
                else:
                    logging.error(
                        f"Недопустимый день, дата: {date} - некоректа.")
                    return False, "Недопустимый день."
        else:
            logging.error(f"Недопустимый день, дата: {date} - некоректа.")
            return False, "Недопустимый день."
    except ValueError:
        logging.error(
            f"Неверный формат даты. Пожалуйста, используйте формат 'дд.мм.гггг', дата: {date} - некоректа")
        return False, "Неверный формат даты. Пожалуйста, используйте формат 'дд.мм.гггг'"


#date_to_prove = '15.03.2023'

#is_valid, message = valid_date(date_to_prove)

is_valid, message = valid_date(input_date)

"""
def main():
    parser = argparse.ArgumentParser(description='Проверка корректности даты')
    parser.add_argument('date', type=str, help='Дата в формате дд.мм.гггг')
    args = parser.parse_args()
    input_date = args.date

    is_valid, message = valid_date(input_date)

    #print(f"Дата '{input_date}' корректна: {is_valid}. {message}")

if __name__ == "__main__":
    main()
"""
