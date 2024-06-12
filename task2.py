from threading import Thread
from time import sleep

ENEMI = 100


class Knight(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        battleday = 0
        enemi = ENEMI
        print('Sir Lancelot, на нас напали!')
        print('Sir Galahad, на нас напали!')

        for skill in range(self.skill):
            battleday += 1
            enemi -= self.skill
            print(f'{self.name}, сражается {battleday} день(дня)..., осталось {enemi} воинов.', flush=True)

            if enemi == 0:
                print(f'{self.name} одержал победу спустя {battleday} дней', flush=True)
                return
            sleep(5)


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print(f'Все битвы закончились!')
