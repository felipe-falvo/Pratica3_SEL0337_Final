from gpiozero import DistanceSensor, LED, Buzzer # importando as bibliotecas do gpiozero
import time # importando a biblioteca de tempo

# configurando o sensor HC-SR04 nos pinos 24 (Echo) e 23 (Trigger) 
# max_distance -> indica que a distância máxima de alcance é de 2 metros
sensor = DistanceSensor(echo = 24, trigger=23, max_distance = 2)

# configurando o LED no pino 14
led = LED(14)

# configurando o buzzer no pino 25
buzzer = Buzzer(25)

print("Inicio:\n")

# função modularizada para ligar o LED e o Buzzer

def ativar_alerta():
    led.on() # acender o LED
    buzzer.on() # ligar o buzzer

# função modularizada para desligar o LED e o Buzzer

def desativar_alerta():
    led.off() # apagar o LED
    buzzer.off() # desligar o buzzer


try:
    # laço da leitura do sensor
    while True:
        time.sleep(0.1) # Aguarda 0.1 segundo entre cada medição
        
        distancia_cm = sensor.distance * 100 # Converte a distância de metros para centímetros
        
        # Mostra a distância atualizando na mesma linha (\r)
        print(f"\rdistância :{distancia_cm:.1f} cm", end="", flush=True)

        # Condições:
        # Se o objeto estiver a menos de 30 cm, liga o buzzer e o LED
        if distancia_cm < 30:
            ativar_alerta()
        # Caso contrário, o buzzer o LED fica desligado
        else:
            desativar_alerta()

# comando CTRL+C no terminal para desligar o programa
except KeyboardInterrupt:
    desativar_alerta() # garantindo que o LED e o buzzer desliguem ao parar o código
    print("\n")
