import easygui
import img

easygui.msgbox(
    'Приходя домой после рабочего дня, мы пытаемся обрести покой. И в этом нам помогает сон.\n'
    'Но возбуждённое подсознание,не даёт нам покоя,поэтому появляются сноведения.\n'
    'Во сне с нами могут происходить разные события, ситуации, встречи, в которых мы '
    'можем увидеть решение наших проблем.\n'
    'И вот идя по лесу мы встречаем облако комаров и дятла, который неугомонно стучит подереву.\n\n'
    'Чтобы разогнать комаров нужно специальное зелье ,которое находится в сказочном ларце.'
    'И чтобы достать зелье оттуда, нужно разгадать загадку.\n'
    'Дятла можно успокоить, дав ему червяков. Добыть их можно, выкопав в земле, '
    'или найти под упавшими деревьями.', title=("Квест"), image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/лес_jpg.jpg"))
step_1 = easygui.buttonbox("Что вы выбирете?", title=("Квест"),
                           choices=["разогнать комаров", "прогнать дятла"],image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/вопрос.jpg"))
if step_1 == "разогнать комаров":
    easygui.msgbox(
        "Вы выбрали разогнать комаров, тем самым отгадайте загадку!", title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/комар.jpg"))
    easygui.msgbox('Извивается, шипит,\nНе совсем не ядовит\nПроглотить он может разом\n'
          'Кабана иль дикобраза.\n', image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/много змей.jpg"))
    count = 0
    while True:
        a = easygui.buttonbox('Кто это?, у вас 3  попытки', choices=["Уж", "Питон", "Гадюка"], title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/много змей.jpg"))
        if a == "Питон":
            easygui.msgbox('Верно! Вы взяли зелье из ларца и открыли его возле облака '
                  'комаров.От противного запаха,комары сразу же разлетелись в разные'
                  ' стороны,открыв вам проход дальше.', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/зелье.jpg"))
            break
        count += 1
        if count == 3:
            easygui.msgbox('Неудача!', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/Неудача.jpg"))
            break
        easygui.msgbox('Пожалуйста, введите ёще раз!', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/попробуй снова.jpg"))
elif step_1 == 'прогнать дятла':
    while True:
        otv = easygui.buttonbox("Где будете искать червяков?", choices=["в земле", "под деревьями"], title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/почва.jpg"))
        if otv == "под деревьями":
            easygui.msgbox('Под упавшими деревьями вы нашли червяков. Собрав несколько, '
                  'вы пошли к дятлу.\nОн подлетел к вам и съел ваших червяков, после чего улетел. Открывая проход дальше.', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/черви.jpg"))
            break
        easygui.msgbox(
            'К сожалению, червяков тут не оказалось, попробуй найти в другом '
            'месте.', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/Неудача.jpg"))
easygui.msgbox('Пройдя дальше мы подходим к бурной реке,чтобы пройти на другой берег,можно пройти, через мост,\n'
      'но его охраняет Гриффон и чтобы через него пройти,нужно решить 2 загадки. \n'
      'Также можно переплыть реку,построим плот.Для его постройки нужно выбрать верные материалы для его создания.', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/мост через бурную реку.jpg"))
a = easygui.buttonbox("Что вы выбирете?", choices=["1 - пойти через мост", "2 - построить плот"],title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/вопрос.jpg"))
if a == "1 - пойти через мост":
    easygui.msgbox('Вы подошли к мосту, Гриффон загородил вам путь.\n'
          'Но он может пропустить вас .если решите его загадки. Вы согласились', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/грифон.jpg"))
    easygui.msgbox('1-ая загадка.\n'
        'Нет того,кто не боится\n'
        'Этой грозной хищной птицы.\n'
        'Кто, куда бы не забрёл,\n'
        'Сверху видит всё...', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/загадка.png"))
    count = 0
    while True:
        otv = easygui.buttonbox('Кто это?, у вас 3  попытки', choices=["Ястреб", "Чайка", "Орёл"], title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/хищные птицы.jpg"))
        if otv == "Орёл":
            easygui.msgbox("Правильно!", title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/верно.png"))
            break
        count += 1
        if count == 3:
            easygui.msgbox("Неудача!", title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/Неудача.jpg"))
            break
        easygui.msgbox("Пожалуйста, введите ёще раз!", title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/попробуй снова.jpg"))
    easygui.msgbox('2-ая загадка.\n'
        'Я-король. Я - царь зверей.\n'
        'Парикмахера скорей!\n'
        'Удивлю всех королев,\n'
        'Пышной гривой. Я же - ...', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/загадка.png"))
    count = 0
    while True:
        otv1 = easygui.buttonbox('Кто это?, у вас 3  попытки', choices=["Лев", "Тигр", "Гепард"], title=("Квест"))
        if otv1 == "Лев":
            easygui.msgbox("Верно!", title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/верно.png"))
            break
        count += 1
        if count == 3:
            easygui.msgbox('Неудача!', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/Неудача.jpg"))
            break
        easygui.msgbox('Пожалуйста, введите ёще раз!', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/попробуй снова.jpg"))
if a == "2 - построить плот":
        easygui.msgbox("Вы собираетесь построить плот! Для того ,чтобы построить плот нужно из перечня материалов , выбрать правильные, какие же из них правильные?", title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/плот.webp"))
        count = 0
        while True:
            otv3 = easygui.buttonbox('Какие это материаты?, у вас 3  попытки!\n' 
                                     "Вот список материалов:\n('Древесина-1','лиана-2','кремень-3','палкa-4','бумага-5','верёвки-6','листья-7')",
                                     choices=["1,2,3,4,5,6,7", "1,2,4,6,7", "1,2,5,7"], title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/материалы для плота-200x150.jpg"))
            if otv3 == "1,2,4,6,7":
                easygui.msgbox("Верно!", title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/верно.png"))
                break
            count += 1
            if count == 3:
                easygui.msgbox('Неудача!', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/Неудача.jpg"))
                break
            easygui.msgbox('Пожалуйста, введите ёще раз!', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/попробуй снова.jpg"))
easygui.msgbox('Перебравшись на другой берег мы попадаем на поляну, где нас окружают\n'
            'Лиса, Медведи и Крыса. И чтобы пройти дальше надо с кем-то из них договориться:', title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/лиса,медведь,крыса.jpg"))
count = 0
while True:
    otv4 = easygui.buttonbox(
        'Кого из зверей выберешь ты?, у вас 3  попытки!\n',
        choices=["Лиса", "Крыса", "Медведь"], title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/лиса,медведь,крыса.jpg"))
    if otv4 == "Крыса":
        easygui.msgbox("Вы выбрали правильный ответ, хитрая крыса помогла вам выбраться из леса", title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/крыса.jpg"))
        break
        count += 1
    if count == 3:
        break
    easygui.msgbox('Вы выбрали неправильного зверя, вас растерзали и вы просыпаетесь в холодном поту!!!\n', "Попробуйте ещё раз",image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/страшный сон.jpg"))
easygui.buttonbox("Вы просыпаетесь с кучей мыслей и удовольствием от приключения!", choices=["Закончить квест"], title=("Квест"),image=("/Users/mac/PycharmProjects/pythonProject/stas test/textqest/easygui img/хороший сон.jpg"))


