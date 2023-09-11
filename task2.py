# Базовый класс обработчика, содержащий ссылку на следующий обработчик в цепочке (если есть)
class Handler:
    def __init__(self, successor=None):
        self.successor = successor  # преемник (следующий обработчик в цепочке)

    def handle_request(self, currency):
        pass


# Конкретный обработчик для долларов США
class USDHandler(Handler):
    def handle_request(self, currency):
        # Если валюта - USD, обработаем ее
        if currency == "USD":
            print("Обработка долларов США")
        # Если это не USD и у нас есть преемник, передаем запрос дальше
        elif self.successor:
            self.successor.handle_request(currency)


# Конкретный обработчик для евро
class EURHandler(Handler):
    def handle_request(self, currency):
        # Если валюта - EUR, обработаем ее
        if currency == "EUR":
            print("Обработка евро")
        # Если это не EUR и у нас есть преемник, передаем запрос дальше
        elif self.successor:
            self.successor.handle_request(currency)


# Конкретный обработчик для британских фунтов
class GBPHandler(Handler):
    def handle_request(self, currency):
        # Если валюта - GBP, обработаем ее
        if currency == "GBP":
            print("Обработка британских фунтов")
        # Если это не GBP и у нас есть преемник, передаем запрос дальше
        elif self.successor:
            self.successor.handle_request(currency)


# Создаем обработчики
usd_handler = USDHandler()
eur_handler = EURHandler(usd_handler)  # передаем usd_handler как преемника для eur_handler
gbp_handler = GBPHandler(eur_handler)  # передаем eur_handler как преемника для gbp_handler

# Посылаем запрос на обработку GBP
# Запрос будет передан от gbp_handler к eur_handler, затем к usd_handler, пока он не будет обработан
gbp_handler.handle_request("EUR")
