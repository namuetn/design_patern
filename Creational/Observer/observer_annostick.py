class Observer:
    def __init__(self, name) -> None:
        self.name_pick = name

    def update_status(self, location):
        self.goto_help(location=location)

    def goto_help(self, location):
        print(f'{self.name_pick}:::PING:::{location}')


class Subject:
    def __init__(self) -> None:
        self.observer_list = []

    def add_observer(self, observer):
        self.observer_list.append(observer)

    def notify(self, location):
        for observer in self.observer_list:
            observer.update_status(location)

SUBJECT = Subject()
RIKI = Observer('riki')
SNIPER = Observer('sniper')

# add RIKI and SNIPER to Team
SUBJECT.add_observer(RIKI)
SUBJECT.add_observer(SNIPER)

# push location
SUBJECT.notify({
    'longtitude': 123,
    'latitude': 345
})