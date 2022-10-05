from typing import *

drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro",
              "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3",
              "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

# в drone по очереди попадает каждый дрон из списка drone_list
# for drone in drone_list:
#     print(drone)

# TODO1
# выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество.
# учтите, что:
# 1) DJI и Dji - это один и тот же производитель! Такие случаи тоже должны обрабатываться
# 2) при выводе исправьте название производителя, если допущена ошибка. Правильный вариант названия: DJI, Autel

producer: str = input()

result_1: List[str] = []

for drone in drone_list:
    index: int = drone.lower().find(producer.lower())
    if index != -1:
        if producer.upper() == "DJI":
            result_1.append(drone.replace(drone[index:index + len(producer)], producer.upper()))
        else:
            result_1.append(drone.replace(drone[index:index + len(producer)], producer.capitalize()))

print("Дроны производителя", producer, ":", result_1)
print("Количество дронов производителя", producer, ":", len(result_1))

# TODO2
# подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine

producers: List[str] = ['DJI', 'Autel', 'Parrot', 'Ryze', 'Eachine']
result_2: Dict[str, int] = {prod: 0 for prod in producers}

for drone in drone_list:
    for prod in producers:
        if prod.lower() in drone.lower():
            result_2[prod] += 1
            break

print(result_2)


# TODO3
# выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество.
# сделайте то же самое для всех дронов, которые не нужно регистрировать
# для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
# как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь
# for drone, weight in zip(drone_list, drone_weight_list):
#     print(drone, weight)

result_3_1: List[str] = []
result_3_2: List[str] = []

for drone, weight in zip(drone_list, drone_weight_list):
    if weight > 150:
        result_3_1.append(drone)
    else:
        result_3_2.append(drone)

print(result_3_1)
print(len(result_3_1))
print(result_3_2)
print(len(result_3_2))


# TODO4
# для каждого дрона из списка выведите, нужно ли согласовывать полет при следующих условиях:
# высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
# помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!

height = 100
closed_area = False
vlos = True

for drone, weight in zip(drone_list, drone_weight_list):
    if height <= 150 and vlos and not closed_area and weight < 150:
        print("Для дрона", drone, "Не нужно согласовывать, летайте спокойно!")
    else:
        conditions = ""
        if not vlos:
            conditions += "/полет вне зоны видимости"
        if height > 150:
            conditions += "/высота более 150 м"
        if closed_area:
            conditions += "/полет в закрытой зоне"
        if weight > 150:
            conditions += "/дрон тяжелее 150 г"
        print("Для дрона", drone, f"Нужно согласовывать, т.к. {conditions}")


# TODO5*
# модифицируйте решение задания TODO1:
# теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
# например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
# производители те же: DJI, Autel, Parrot, Ryze, Eachine

prod_5: str = input()

result_5: List[str] = []

for drone in drone_list:
    index_5: int = drone.lower().find(prod_5.lower())
    if index_5 != -1:
        if prod_5.upper() == "DJI":
            result_5.append(drone.replace(drone[index_5:index_5 + len(prod_5)], ""))
        else:
            result_5.append(drone.replace(drone[index_5:index_5 + len(prod_5)], ""))

print("Дроны производителя", prod_5, ":", result_5)
print("Количество дронов производителя", prod_5, ":", len(result_5))

