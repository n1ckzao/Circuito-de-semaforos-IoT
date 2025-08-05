from machine import Pin
from utime import sleep

print("Hello World!")

ledVerde = Pin(16, Pin.OUT)
ledAmarelo = Pin(17, Pin.OUT)
ledVermelho = Pin(18, Pin.OUT)


while True:
  ledVerde.on()
  print("Led verde ON!")
  sleep(20)
  ledVerde.off()
  print("Led verde OFF")
  sleep(0.5)

  ledAmarelo.on()
  print("Led amarelo ON!")
  sleep(10)
  ledAmarelo.off()
  print("Led amarelo OFF")
  sleep(0.5)

  ledVermelho.on()
  print("Led vermelho ON!")
  sleep(7)
  ledVermelho.off()
  print("Led vermelho OFF")
  sleep(0.5)