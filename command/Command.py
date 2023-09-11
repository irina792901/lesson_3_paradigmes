from abc import ABC, abstractmethod
# Command (Команда): Это интерфейс для выполнения операции.#
# ConcreteCommand (Конкретная команда): Класс, реализующий интерфейс Command.
# Он связан с определенным получателем и вызывает метод этого получателя.#
# Receiver (Получатель): Это тот объект, над которым будет выполняться операция.
# Получатель делает реальную работу, когда команда выполняется.#
# Invoker (Вызывающий): Запрашивает команду для выполнения определенной операции.

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class Light:
    def turn_on(self):
        print("Свет включен")

    def turn_off(self):
        print("Свет выключен")


class RemoteControl:
    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()


light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()

remote.set_command(light_on)
remote.press_button()  # Вывод: Свет включен

remote.set_command(light_off)
remote.press_button()  # Вывод: Свет выключен