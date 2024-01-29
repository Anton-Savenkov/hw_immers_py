import logging
import argparse

logging.basicConfig(filename='Log/Data_log_task02_01.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} в строке {lineno} '
                           'функция "{funcName}()" : {msg}',
                    style='{',
                    level=logging.ERROR)

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Поверка деления на ноль')
parser.add_argument('div_a', type=float, help='Задаем делимое')
parser.add_argument('div_b', type=float, help='Задаем делитель')

args=parser.parse_args()
print(args.div_a, args.div_b)
a=args.div_a
b=args.div_b


def division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logger.error(
            f'Ошибка деления на ноль! Число {a} нельзя поделить на число {b}')
        return float('inf')
    return res


if __name__ == '__main__':
    print(f'{division(a, b)}')