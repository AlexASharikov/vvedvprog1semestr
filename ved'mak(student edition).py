import random
health_pts = int(60)
food_pts = int(60)
starv_pts = 0
moral_pts = int(60)
study_pts = int(40)
money_pts = int(20)
lose = 0
day = 0
name = str(input("Как мне тебя называть? "))
print("Добро пожаловать в университет, ",name,".",sep = "")
for i in range(15):
    day += 1
    print("День",day)
    print("Очки Здоровья равны", health_pts)
    print("Очки Сытости равны", food_pts)
    print("Очки Морали равны", moral_pts)
    print("Очки Обучения равны", study_pts)
    print("Деньги", money_pts)
    print("Ты просыпаешься в общежитии, благодаря будильнику соседа. Чем сегодня займешься?")
    print("1. Пойти на занятия")
    print("2. Работать в супермаркете")
    print("3. Отдохнуть с друзьями в кафе")
    print("4. Поесть дома")
    if study_pts < 25:
        print("5. Сдать долги по предметам")
    if health_pts < 25:
        print("6. Сходить в аптеку")
    choise_day = int(input())
    if choise_day == 1:
        go_home = 0
        print("Ты проходишь мимо автобусной остановки. Подождёшь автобус или пойдёшь пешком?")
        print("1. Пойти пешком")
        print("2. Поехать на автобусе")
        choise_transport = int(input())
        if choise_transport == 1:
            walk_var = random.randint(1, 101)
            print("Очки Здоровья увеличены на 5")
            print("Очки Сытости уменьшились на 10")
            health_pts += 5
            food_pts -= 10
            if walk_var <= 15:
                print("Ты видишь одногруппника и, поздоровавшись, вы идете вместе.")
                print("Очки Морали увеличились на 10")
                moral_pts += 10
        if choise_transport == 2:
            bus_var = random.randint(1, 101)
            print("Очки Здоровья уменьшились на 5")
            print("Деньги уменьшились на 5")
            health_pts -= 5
            money_pts -= 5
            if bus_var <= 15:
                print("По радио в кабине водителя заиграл твой любимый трек.")
                print("Очки Морали увеличились на 5")
                moral_pts += 5
            elif bus_var > 90:
                print("Рядом с тобой сидел больной мужчина. Он чихнул в твою сторону и теперь ты тоже чувствуешь себя заболевшим.")
                print("Очки Здоровья уменьшились на 10")
                health_pts -= 10
                print("В таком виде в университет приезжать нельзя. Возвращайся в общежитие.")
                go_home = 1
        if go_home != 1:
            print("Ты в университете. Семь пар проходят на одном дыхании.")
            print("Очки обучения увеличились на 10")
            study_pts += 10
        go_home = 0
    elif choise_day == 2:
        work_var = random.randint(1,101)
        print("Таская продуктовые палеты и убирая просроченные товары, ты не заметил, как закончился день.")
        print("Деньги увеличились на 10")
        print("Очки Здоровья уменьшились на 5")
        print("Очки Морали уменьшились на 5")
        print("Очки Обучения уменьшились на 10")
        money_pts += 10
        health_pts -= 5
        moral_pts -= 5
        study_pts -= 10
        if work_var <= 20:
            print("Ты работал на пределе и получил заслуженную премию.")
            print("Деньги увеличились на 5")
            money_pts += 5
    elif choise_day == 3:
        chill_var = random.randint(1,101)
        if chill_var <= 15:
            print("Твои друзья предлагают пойти сегодня в кино.")
            print("1. Согласиться")
            print("2. Отказаться")
            choise_cinema = int(input())
            if choise_cinema == 1:
                print("Ты отлично провел время в кино, но накапливающиеся задолженности по учёбе не дают покоя")
                print("Очки Морали увеличены на 15")
                print("Очки Обучения уменьшились на 10")
                print("Деньги уменьшились на 10")
                moral_pts += 15
                study_pts -= 10
                money_pts -= 10
            elif choise_cinema == 2:
                print("Ты отказался и пошел домой спать")
                print("Очки Сытости уменьшились на 5")
                print("Очки Обучения уменьшились на 10")
                food_pts -= 5
                study_pts -= 10
        else:
            print("Ты посетил кафе с друзьями")
            print("Очки Сытости увеличились на 5")
            print("Очки Морали увеличились на 5")
            print("Очки Обучения уменьшились на 10")
            food_pts += 5
            moral_pts += 5
            study_pts -= 10
            if chill_var > 90:
                print("Один из твоих друзей пошёл сдавать долги в университет. Вы немного погрустили над трудностями обучения")
                print("Очки Морали уменьшились на 10")
                moral_pts -= 10
    elif choise_day == 4:
        food_var = random.randint(1,101)
        print("Готовка или доставка - вот в чем вопрос...")
        print("1. Готовить самому")
        print("2. Заказать еду с доставкой")
        choise_food = int(input())
        if choise_food == 1:
            print("Ты самостоятельно сварил макароны")
            print("Очки Сытости увеличились на 10")
            print("Очки Обучения уменьшились на 10")
            food_pts += 10
            study_pts -= 10
            if food_var <= 10:
                print("Ты умудрился отравиться макаронами.")
                print("Очки Здоровья уменьшились на 20")
                print("Очки Морали уменьшились на 10")
                health_pts -= 20
                moral_pts -= 10
        elif choise_food == 2:
            print("Ты заказал пиццу и съел её за просмотром летсплея Куплинова")
            print("Очки Сытости увеличились на 10")
            print("Очки Морали увеличились на 5")
            print("Очки Здоровья уменьшились на 5")
            print("Очки Обучения уменьшились на 10")
            print("Деньги уменьшились на 5")
            food_pts += 10
            moral_pts += 5
            health_pts -= 5
            study_pts -= 10
            money_pts -= 5
    elif choise_day == 5:
        debt_var = random.randint(1,101)
        print("Ты идешь закрывать долги. За какой долг возьмёшься?")
        print("1. Лёгкий долг")
        print("2. Обычный долг")
        print("3. Сложный долг")
        choise_debt = int(input())
        if choise_debt == 1:
            if debt_var <= 60:
                print("Ты застал преподавателя в хорошем настроении и закрыл долг.")
                print("Очки Обучения увеличились на 15")
                study_pts += 15
            else:
                print("Ты плохо подготовился и провалил сдачу долга")
                print("Очки Морали уменьшились на 5")
                moral_pts -= 5
        elif choise_debt == 2:
            if debt_var <= 35:
                print("Ты застал преподавателя в хорошем настроении и закрыл долг.")
                print("Очки Обучения увеличились на 25")
                print("Очки Сытости уменьшились на 5")
                study_pts += 25
                food_pts -= 5
            else:
                print("Ты плохо подготовился и провалил сдачу долга")
                print("Очки Морали уменьшились на 10")
                moral_pts -= 10
        elif choise_debt == 3:
            if debt_var <= 15:
                print("Ты ответил на все заковыристые вопросы преподавателя и закрыл долг.")
                print("Очки Обучения увеличились на 35")
                print("Очки Сытости уменьшились на 15")
                print("Очки Морали увеличились на 15")
                study_pts += 35
                food_pts -= 15
                moral_pts += 15
            else:
                print("Ты не справился со всеми вопросами и провалил сдачу долга")
                print("Очки Морали уменьшились на 10")
                moral_pts -= 10
    elif choise_day == 6:
        hp_var = random.randint(1,101)
        print("Накапливающийся стресс и большой трудообъём довёл тебя до невыносимой головной боли")
        print("Ты идёшь в местную аптеку за анальгином")
        if hp_var <= 50:
            print("Купленный тобой анальгин на время избавил тебя от головной боли")
            print("Очки Здоровья увеличились на 15")
            print("Очки Обучения уменьшились на 10")
            health_pts += 15
            study_pts -= 10
        elif hp_var > 50:
            print("Выяснилось, что головная боль терзает большое число студентов, и анальгина в аптеке не осталось")
            print("Очки Обучения уменьшились на 10")
            print("Очки Морали уменьшились на 5")
            study_pts -= 10
            moral_pts -= 5
    print("День подходит к концу. Чем займешься?")
    print("1. Спать")
    print("2. Делать задания и готовиться к парам")
    print("3. Играть всю ночь в Доту с друзьями")
    choise_night = int(input())
    if choise_night == 1:
        noise_var = random.randint(1,101)
        if noise_var <= 5:
            print("Соседи устроили вечер гитарной песни, и ты половину ночи ворочался.")
            print("Очки Здоровья уменьшились на 5")
            print("Очки Сытости уменьшились на 10")
            health_pts -= 5
            food_pts -= 10
        else:
            print("Ты хорошенько выспался и готов к новому дню.")
            print("Очки Здоровья увеличились на 10")
            print("Очки Сытости уменьшились на 5")
            print("Очки Морали увеличились на 5")
            health_pts += 10
            food_pts -= 5
            moral_pts += 5
    elif choise_night == 2:
        print("Ты всю ночь изучал основы МатАнализа, запивая кофе энергетиками")
        print("Очки Обучения увеличились на 10")
        print("Очки Здоровья уменьшились на 15")
        print("Очки Сытости уменьшились на 5")
        study_pts += 10
        health_pts -= 15
        food_pts -= 5
    elif choise_night == 3:
        print("Ты отыграл восемь игр подряд и твои нервные клетки уже не будут прежними.")
        print("Очки Морали увеличились на 10")
        print("Очки Здоровья уменьшились на 5")
        moral_pts += 10
        health_pts -= 5
    if health_pts > 100:
        health_pts = 100
    if food_pts > 100:
        food_pts = 100
    if moral_pts > 100:
        moral_pts = 100
    if study_pts > 100:
        study_pts = 100
    if money_pts > 50:
        money_pts = 50
    if health_pts <= 0:
        print("Ты не выдержал сложностей университетской жизни и серьезно заболел. Окончить первый семестр в этом году возможности уже не будет")
        lose = 1
        break
    if food_pts <= 0:
        starv_pts += 1
        if starv_pts == 1:
            print("Доведешь свой организм до такого голодного истощения ещё раз и поминай как звали.")
    if starv_pts == 2:
        print("Ну теперь всё, поминай как звали.")
        lose = 1
        break
    if moral_pts <= 0:
        print("Ты не выдержал сложностей университетской жизни и потерял тягу к учебе. Окончить первый семестр в этом году возможности уже не будет")
        lose = 1
        break
if lose == 1:
    print("Игра окончена. Ты проиграл.")
else:
    if study_pts >= 80:
        print("Первый семестр окончен без хвостов и с повышенной стипендией. Так держать.")
        print("Ты выиграл!")
    elif study_pts < 80 and study_pts >= 60:
        print("Первый семестр окончен и у нас даже осталась стипендия. Жизнь хороша.")
        print("Ты выиграл")
    elif study_pts < 60 and study_pts >= 40:
        print("Первый семестр кончился и нас не отчислили. Гуляем дальше.")
        print("Ты победил")
    elif study_pts < 40:
        print("Блин, оказывается на пары тоже ходить надо. Семестр окончен, а нас отчислили.")
        print("Игра окончена. Ты проиграл.")