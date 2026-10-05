import RPi.GPIO as GPIO
import time
import threading

# definindo os pinos
pino_led = 11 # Pino 11 no LED
botao = 13  # Pino 13 no botão

# variável para o tempo de ficar piscando do LED
tempo_pisca = 1  # valor: 1 segundo (Modo Lento)

# mutex para a variável compartilhada
mutex = threading.Lock()

# chamada após o término da contagem regressiva
def fim_contar():
    print("\nFIM\n")

# executada em uma thread separada para contagem regressiva
def thread_contagem(duracao):
    # contagem decrescente partindo da duração até 0
    for t in range(duracao, -1, -1):
        # tempo total em minutos e segundos
        minutos, segundos = divmod(t, 60)
        
        # seção protegida por mutex para ler o modo atual
        with mutex:
            opcao = "Opcao 1 (Lento)" if tempo_pisca == 1 else "Opcao 2 (Rapido)"
            # atualiza a contagem na mesma linha
            print(f"\rBotao: {opcao} / Tempo: {minutos:02d}:{segundos:02d}", end="", flush=True)
            
        time.sleep(1) # 1 segundo entre cada iteração
        
    print() 
    fim_contar()

# callback de interrupção quando o botão é apertado
def mudar_frequencia(canal):
    global tempo_pisca
    
    # Seção protegida por mutex para alternar a frequência
    with mutex:
        if tempo_pisca == 1:
            tempo_pisca = 0.2  # alterna para o modo rápido (0.2s)
        else:
            tempo_pisca = 1    # alterna para o modo lento (1s)

try:
    # configura os pinos
    GPIO.setmode(GPIO.BOARD)
    
    # configura o pino do LED como saída
    GPIO.setup(pino_led, GPIO.OUT)
    
    # configura o pino do botão como entrada com pull-Up
    GPIO.setup(botao, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # interrupção na borda de descida, filtro bounce de 300ms
    GPIO.add_event_detect(botao, GPIO.FALLING, callback=mudar_frequencia, bouncetime=300)

    # inicia a thread da contagem (15s)
    t_tempo = threading.Thread(target=thread_contagem, args=(15,))
    print("\nInciado BLINK\n")
    t_tempo.start()

    # thread principal: liga o LED
    while True:
        # tempo de ficar piscando protegido por mutex
        with mutex:
            tempo_atual = tempo_pisca
            
        # acende o LED
        GPIO.output(pino_led, GPIO.HIGH)
        time.sleep(tempo_atual)
        
        # apaga o LED
        GPIO.output(pino_led, GPIO.LOW)
        time.sleep(tempo_atual)

except KeyboardInterrupt:
    print("\nDesligado")

finally:
    # limpa os pinos da gpio
    GPIO.cleanup()
