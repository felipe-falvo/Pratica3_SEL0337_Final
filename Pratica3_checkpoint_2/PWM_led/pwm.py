import RPi.GPIO as GPIO # biblioteca para os pinos da raspberry
import time # biblioteca de tempo

# definindo o pino 18 o LED
pino_LED = 18

# configurando para broadcom (BCM)
GPIO.setmode(GPIO.BCM)

# configurando o pino do LED como saída (OUTPUT)
GPIO.setup(pino_LED, GPIO.OUT)

# configurando o pwm no pino do LED com frequência de 50 Hz
led_com_pwm = GPIO.PWM(pino_LED, 50)

# inicia o pwm com um duty cycle de 0% (LED começa desligado)
led_com_pwm.start(0)

print("Aperta CRTL+C para desligar")


try:
    # manter o ciclo do pwn funcionando
    while True:
    
        # aumenta o brilho de 0 a 100 com incrementos de 5
        for i in range(0, 101, 5):
            led_com_pwm.ChangeDutyCycle(i) # Atualiza o duty cycle do PWM
            time.sleep(0.5) # 0.5 segundos para cada intensidade
            
        # diminui o brilho de 100 a 0 com decrementos de 5    
        for i in range(100, -1, -5):
            led_com_pwm.ChangeDutyCycle(i) # Atualiza o duty cycle do PWM
            time.sleep(0.5) # 0.5 segundos para cada intensidade

# programa desliga quando aperta CTRL+C
except:
    led_com_pwm.stop() # para com o sinal pwm
    GPIO.cleanup() # limpa as configurações feitas durante o código
