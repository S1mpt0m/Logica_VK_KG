import csv

filename_wish = "ded_moroz_wish.csv"
filename_kids = "kids_wish.csv"
filename_result = "solution.csv"

amount_kids = 184000
amount_twins = 5520
amount_one_type_gifts = 250
amount_types_gifts = 1000


class Gift:
    def __init__(self):
        self.amount = amount_one_type_gifts
        self.kids = {}  # childId, priorityID (ключ, значение)


class Kid:
    def __init__(self):
        self.currentGiftId = 0  # присваивается, если при первой проверке был найден подарок в обоих списках
        self.check = 0  # значение для проверки (нашлось ли "комбо" при первом проходе)
        self.gifts = {}  # priorityID, giftId (ключ, значение)


gifts = [Gift() for _ in range(amount_types_gifts)]
kids = [Kid() for _ in range(amount_kids)]

with open(filename_wish, 'r') as file1:
    reader = csv.reader(file1)
    for line in reader:
        _id = int(line[0])
        priorityID = 1
        for childId in map(int, line[1:]):
            gifts[_id].kids[childId] = priorityID
            priorityID += 1

with open(filename_kids, 'r') as file2:
    reader = csv.reader(file2)
    for line in reader:
        _id = int(line[0])
        priorityID = 1
        for giftId in map(int, line[1:]):
            kids[_id].gifts[priorityID] = giftId
            priorityID += 1

with open(filename_result, 'w') as file3:
    file3.write("ChildId,GiftId\n")
    alluni = 0

    # подсчёт близнецов
    for i in range(0, amount_twins, 2):
        bestuni = -1.0
        bestGiftId = 0

        # подсчёт желаний первого ребёнка и сравнение с остальными
        for priorityGift, idGift in kids[i].gifts.items():
            if gifts[idGift].amount != 0 and gifts[idGift].amount != 1:
                happinessDed1 = -1.0
                if gifts[idGift].kids.get(i, 0) != 0:
                    happinessDed1 = 2 * (184.0 - float(gifts[idGift].kids[i]) + 1.0)
                happinessChild1 = -1.0
                if priorityGift != 0:
                    happinessChild1 = 2 * (100.0 - float(priorityGift) + 1.0)
                unisd1 = happinessChild1 / 184.0
                unisdm1 = happinessDed1 / 250.0
                uni1 = unisd1 + unisdm1

                happinessDed2 = -1.0
                happinessChild2 = -1.0
                if gifts[idGift].kids.get(i + 1, 0) != 0:
                    happinessDed2 = 2 * (184.0 - float(gifts[idGift].kids[i + 1]) + 1.0)
                for pair2_key, pair2_value in kids[i + 1].gifts.items():
                    if pair2_value == idGift:
                        happinessChild2 = 2 * (100.0 - float(pair2_key) + 1.0)

                unisd2 = happinessChild2 / 184.0
                unisdm2 = happinessDed2 / 250.0
                uni2 = unisd2 + unisdm2

                uni = uni1 + uni2
                if uni > bestuni:
                    bestuni = uni
                    bestGiftId = idGift

        # подсчёт желаний второго ребёнка и сравнение с остальными
        for priorityGift, idGift in kids[i + 1].gifts.items():
            if gifts[idGift].amount != 0 and gifts[idGift].amount != 1:
                happinessDed1 = -1.0
                if gifts[idGift].kids.get(i + 1, 0) != 0:
                    happinessDed1 = 2 * (184.0 - float(gifts[idGift].kids[i + 1]) + 1.0)
                happinessChild1 = -1.0
                if priorityGift != 0:
                    happinessChild1 = 2 * (100.0 - float(priorityGift) + 1.0)
                unisd1 = happinessChild1 / 184.0
                unisdm1 = happinessDed1 / 250.0
                uni1 = unisd1 + unisdm1

                happinessDed2 = -1.0
                happinessChild2 = -1.0
                if gifts[idGift].kids.get(i, 0) != 0:
                    happinessDed2 = 2 * (184.0 - float(gifts[idGift].kids[i]) + 1.0)
                for pair2_key, pair2_value in kids[i].gifts.items():
                    if pair2_value == idGift:
                        happinessChild2 = 2 * (100.0 - float(pair2_key) + 1.0)

                unisd2 = happinessChild2 / 184.0
                unisdm2 = happinessDed2 / 250.0
                uni2 = unisd2 + unisdm2

                uni = uni1 + uni2
                if uni > bestuni:
                    bestuni = uni
                    bestGiftId = idGift

        # поиск и подсчёт подарка деда мороза для первого ребёнка
        for j in range(amount_types_gifts):
            priorityChild = gifts[j].kids.get(i, 0)
            if priorityChild != 0 and gifts[j].amount != 0 and gifts[j].amount != 1:
                happinessChild1 = -1.0
                happinessDed1 = -1.0
                if priorityChild != 0:
                    happinessDed1 = 2 * (184.0 - float(priorityChild) + 1.0)
                for pair_key, pair_value in kids[i].gifts.items():
                    if pair_value == j:
                        happinessChild1 = 2 * (100.0 - float(pair_key) + 1.0)
                unisd1 = happinessChild1 / 184.0
                unisdm1 = happinessDed1 / 250.0
                uni1 = unisd1 + unisdm1

                happinessChild2 = -1.0
                happinessDed2 = -1.0
                priorityChild2 = gifts[j].kids.get(i + 1, 0)
                if priorityChild2 != 0 and gifts[j].amount != 0 and gifts[j].amount != 1:
                    happinessDed2 = 2 * (184.0 - float(priorityChild2) + 1.0)

                for pair_key, pair_value in kids[i + 1].gifts.items():
                    if pair_value == j:
                        happinessChild2 = 2 * (100.0 - float(pair_key) + 1.0)

                unisd2 = happinessChild2 / 184.0
                unisdm2 = happinessDed2 / 250.0
                uni2 = unisd2 + unisdm2
                uni = uni1 + uni2
                if uni > bestuni:
                    bestuni = uni
                    bestGiftId = j

        # поиск и подсчёт подарка деда мороза для второго ребёнка
        for j in range(amount_types_gifts):
            priorityChild = gifts[j].kids.get(i + 1, 0)
            if priorityChild != 0 and gifts[j].amount != 0 and gifts[j].amount != 1:
                happinessChild1 = -1.0
                happinessDed1 = -1.0
                if priorityChild != 0:
                    happinessDed1 = 2 * (184.0 - float(priorityChild) + 1.0)
                for pair_key, pair_value in kids[i + 1].gifts.items():
                    if pair_value == j:
                        happinessChild1 = 2 * (100.0 - float(pair_key) + 1.0)
                unisd1 = happinessChild1 / 184.0
                unisdm1 = happinessDed1 / 250.0
                uni1 = unisd1 + unisdm1

                happinessChild2 = -1.0
                happinessDed2 = -1.0
                priorityChild2 = gifts[j].kids.get(i, 0)
                if priorityChild2 != 0 and gifts[j].amount != 0 and gifts[j].amount != 1:
                    happinessDed2 = 2 * (184.0 - float(priorityChild2) + 1.0)

                for pair_key, pair_value in kids[i].gifts.items():
                    if pair_value == j:
                        happinessChild2 = 2 * (100.0 - float(pair_key) + 1.0)

                unisd2 = happinessChild2 / 184.0
                unisdm2 = happinessDed2 / 250.0
                uni2 = unisd2 + unisdm2
                uni = uni1 + uni2
                if uni > bestuni:
                    bestuni = uni
                    bestGiftId = j

        gifts[bestGiftId].amount -= 2
        file3.write(f"{i},{bestGiftId}\n")
        file3.write(f"{i + 1},{bestGiftId}\n")
        alluni = alluni + bestuni

    # первый проход
    # подсчёт если подарок есть в обоих списках (деда мороза и ребёнка)
    for i in range(amount_twins, amount_kids):
        bestuni = -1.0
        bestGiftId = 0

        for priorityGift, idGift in kids[i].gifts.items():
            if gifts[idGift].amount != 0:
                happinessDed = -1.0
                if gifts[idGift].kids.get(i, 0) != 0:
                    happinessDed = 2 * (184.0 - float(gifts[idGift].kids[i]) + 1.0)
                if bestuni == -1.0 or happinessDed != -1.0:
                    happinessChild = -1.0
                    if priorityGift != 0:
                        happinessChild = 2 * (100.0 - float(priorityGift) + 1.0)
                    unisd = happinessChild / 184.0
                    unisdm = happinessDed / 250.0
                    uni = unisd + unisdm
                    if uni > bestuni:
                        bestuni = uni
                        bestGiftId = idGift
                        if happinessDed != -1.0:
                            kids[i].check = 1
                        else:
                            kids[i].check = 0

        # "бронируем" подарок для ребёнка, далее мы его впишем
        if kids[i].check == 1:
            kids[i].currentGiftId = bestGiftId
            gifts[bestGiftId].amount -= 1
            alluni = alluni + bestuni

    # простой подсчёт с помощью обхода и поиск лучшего результата при помощи формул,
    # запись с предыдущего прохода в файл
    for i in range(amount_twins, amount_kids):
        if kids[i].check == 1:
            file3.write(f"{i},{kids[i].currentGiftId}\n")
        else:
            bestuni = -1.0
            bestGiftId = 0

            for priorityGift, idGift in kids[i].gifts.items():
                if gifts[idGift].amount != 0:
                    happinessDed = -1.0
                    if gifts[idGift].kids.get(i, 0) != 0:
                        happinessDed = 2 * (184.0 - float(gifts[idGift].kids[i]) + 1.0)
                    if bestuni == -1.0 or happinessDed != -1.0:
                        happinessChild = -1.0
                        if priorityGift != 0:
                            happinessChild = 2 * (100.0 - float(priorityGift) + 1.0)
                        unisd = happinessChild / 184.0
                        unisdm = happinessDed / 250.0
                        uni = unisd + unisdm
                        if uni > bestuni:
                            bestuni = uni
                            bestGiftId = idGift

            for j in range(amount_types_gifts):
                priorityChild = gifts[j].kids.get(i, 0)
                if priorityChild != 0 and gifts[j].amount != 0:
                    happinessChild = -1.0
                    happinessDed = 2 * (184.0 - float(priorityChild) + 1.0)
                    for pair_key, pair_value in kids[i].gifts.items():
                        if pair_value == j:
                            happinessChild = 2 * (100.0 - float(pair_key) + 1.0)
                    unisd = happinessChild / 184.0
                    unisdm = happinessDed / 250.0
                    uni = unisd + unisdm
                    if uni > bestuni:
                        bestuni = uni
                        bestGiftId = j

            gifts[bestGiftId].amount -= 1
            file3.write(f"{i},{bestGiftId}\n")
            alluni = alluni + bestuni

    print(alluni / 1000)
