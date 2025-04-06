import pygame

print('Setup Start') #Aparece ae
pygame.init() #necessita dessa inicialização
window = pygame.display.set_mode(size=(600, 450)) #UMA JANELA TENTA SER ABERTA, PORÉM FECHA, PROGRAMA A ENCERRA
print('Setup End')
print('Loop Start')
while True: #loop de laço infinito, fica preso para sempre
   # pass/bug na tela, sendo necessário configurar botão de fechar a janela, trabalhando com eventos.
#check for all events
    for event in pygame.event.get(): #pegar os eventos e ficar checando
        if event. type == pygame.QUIT:
           print('Quitting...')
            pygame.quit() #close windown
            quit() # end game
