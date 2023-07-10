import telebot
from telebot import types

bot = telebot.TeleBot("6332328061:AAG2r6n888T7wb7WT9xa9RwZI-KUpN5oBoE")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
    bot.send_message(message.from_user.id,
                     '👋 Преветствую вас Оля, Саша, тетя Марина и Даша!\nНапишите свои имена по отдельности, и я расскажу что вас сегодня ждет!',
                     reply_markup=markup)  # ответ бота


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == "Марина":
        bot.send_message(message.from_user.id,
                         "Я виджу, что в вашем будущем наступают перспективные и радостные события.\nВам улыбнется удача и вы будете встречать новые возможности и вызовы с открытым сердцем и уверенностью.\nВы достигнете больших успехов в своей карьере или профессиональной сфере.\nВаши усилия и преданность принесут вам признание и возможность реализовать свои таланты.\nБудьте готовы к новым проектам, повышению в должности или даже возможности заняться собственным делом.\nВ личной жизни у вас также будут положительные изменения.\nВы можете встретить человека, который станет вашим истинным партнером и поддержкой.\nВместе вы будете строить гармоничные и доверительные отношения, основанные на взаимопонимании и любви. Если вы уже находитесь в отношениях, то они могут укрепиться и стать еще более прочными.\nВаше здоровье также будет в порядке, но не забывайте о заботе о себе.\nРегулярные физические упражнения, здоровое питание и время для отдыха помогут вам сохранить энергию и жизненную силу.\nВажно помнить, что предсказания не являются абсолютной гарантией будущего, а лишь указывают на потенциальные возможности.\nВаше собственное решение и усилия будут иметь решающее значение для достижения успеха. Будьте открытыми к новому, верьте в себя и следуйте своим сердцем.\nЖелаю вам удачи и счастья в вашем будущем, Марина!")
    elif message.text == "Саша" or message.text == "Александра":
        bot.send_message(message.from_user.id,
                         "Ваше будущее будет полно новых возможностей и успехов.\nВы обладаете сильной решительностью и умением преодолевать препятствия, что поможет вам достичь своих целей.\nВаш талант и преданность своей работе принесут вам признание и возможность проявить свои способности.\nБудьте готовы к новым вызовам и возможностям для карьерного роста.\nВ личной жизни ожидается положительное развитие.\nВозможно, вы встретите человека, который будет важным для вашего сердца и станет вашим надежным партнером.\nВаши отношения будут основаны на взаимном уважении и поддержке.\nПомните, что вы обладаете силой и ресурсами, чтобы создать яркое будущее для себя. Верьте в себя, следуйте своим мечтам и примите вызовы, которые появятся на вашем пути.\nУдачи, Александра, во всех ваших начинаниях!")
    elif message.text == "Оля" or message.text == "Ольга":
        bot.send_message(message.from_user.id,
                         "Ваше будущее наполнено возможностями и успехом.\nВы будете встречать новые вызовы с решительностью и энтузиазмом, что приведет вас к достижению ваших целей.\nВаша талантливая и трудолюбивая натура принесет вам признание и возможность реализовать свой потенциал.\nБудьте готовы использовать свои умения и знания в новых проектах или возможностях карьерного роста.\nВ личной жизни ожидается положительное развитие.\nВозможно, вы встретите особенного человека, который станет вашим партнером и союзником. Вместе вы будете строить гармоничные отношения, основанные на взаимопонимании и взаимной поддержке.\nПомните, что вы имеете силу и ресурсы, чтобы сделать свое будущее ярким и успешным. Верьте в себя, следуйте своим мечтам и стремитесь к саморазвитию.\nУдачи, Оля, во всех ваших начинаниях!")
    elif message.text == "Даша" or message.text == "Дарья":
        bot.send_message(message.from_user.id, "Замуж пора!")
    else:
        bot.send_message(message.from_user.id, "Для этого имени нет предсказания, 😕 блин...")


bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть
