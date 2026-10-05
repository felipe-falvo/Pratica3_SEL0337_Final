import RPi.GPIO as GPIO
import time

# Configuração do pino para o LED
pino_LED = 18
GPIO.setmode(GPIO.BCM)

# Define o pino 18 como saída (OUTPUT)
GPIO.setup(pino_LED, GPIO.OUT)
# LED começa apagado
GPIO.output(pino_LED, GPIO.LOW) 

# função modularizada
def contagem_LED(tempo):
    tempo_resto = tempo
    
    # While da contagem regressiva:
    while tempo_resto >= 0:
        # Separa o tempo em minuto e segundo
        minuto, segundo = divmod(tempo_resto, 60) 
        
        # formatado MM:SS e atualiza na mesma linha (end='\r')
        print('{:02d}:{:02d}'.format(minuto, segundo), end='\r')
        
        # espera de 1 segundo
        if tempo_resto > 0:
            time.sleep(1)
            
        tempo_resto = tempo_resto - 1
        
    # acende o LED enviando os 3.3V
    GPIO.output(pino_LED, GPIO.HIGH)
    print("\nContagem terminou")
    print("Led aceso\n")

# tratamento de exceções (try/except)
try:
    # Lógica para receber a entrada do usuário
    while True:
        entrada = input("Coloque o tempo (segundos) para contar: ")
        try:
            # type casting para converter a string de entrada para número inteiro
            tempo = int(entrada)
            
            # aceitar apenas números positivos
            if tempo > 0:
                contagem_LED(tempo)
                break
            else:
                print("Erro, pois numero deve ser positivo")
                
        except ValueError:
            # erro caso seja usado letras
            print("Erro, pois o valor deve ser um numero inteiro")
            
finally:
    # Apertar ENTER para poder desligar o LED
    input("Aperte enter para desligar: ")
    # limpa as configurações do hardware
    GPIO.cleanup()
