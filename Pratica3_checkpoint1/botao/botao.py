import RPi.GPIO as GPIO
import time

# escolhendo onde vão colocar o pino e o botão
pino_LED = 18
pino_botao = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(pino_LED, GPIO.OUT) # LED como saída

# colocando o botão como entrada e ativa o resistor Pull-Up
GPIO.setup(pino_botao, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(pino_LED, GPIO.LOW) # iniciando com o LED apagado


def estado_led(canal):

    # em configuração Pull-Up, o botão pressionado é ligado ao GND
    if GPIO.input(pino_botao) == GPIO.LOW:
        GPIO.output(pino_LED, GPIO.HIGH) # liga quando botão apertado
    else:
        GPIO.output(pino_LED, GPIO.LOW) # desligado quando botão não apertado

# detecção para saber quando o botão foi ou não apertado
GPIO.add_event_detect(pino_botao, GPIO.BOTH, callback=estado_led)

# programa para quando apertar CTRL+C
try:
    print("Aperte CTRL+C para desligar")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
