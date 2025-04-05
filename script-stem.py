from stem import Signal
from stem.control import Controller
import time

with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    while True:
        controller.signal(Signal.NEWNYM)
        print("Novo IP requisitado")
        time.sleep(5)  # Alterar IP a cada 60 segundos
