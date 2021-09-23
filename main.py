import pandas as pd

import math

if __name__ == '__main__':

    x0 = float(input('X координата нулевого пикета: '))
    y0 = float(input('Y координата нулевого пикета: '))
    angle = math.radians(float(input('Азимут профилей в градусах: ')) - 90)

    x_step = float(input('Шаг между пикетами: '))
    y_step = float(input('Шаг между профилями: '))

    pks = int(input('Количество пикетов на профиле: '))
    prs = int(input('Количество профилей: '))

    path = input('Путь для записи файла: ')

    data = []

    for y in range(prs):
        for x in range(pks):
            data.append({'X': x0 + math.cos(angle) * x * x_step - math.sin(angle) * y * y_step,
                         'Y': y0 - math.sin(angle) * x * x_step - math.cos(angle) * y * y_step,
                         'Pk': x,
                         'Pr': y})

    df = pd.DataFrame(data)
    print(df)

    df.to_excel(path, index=False)
