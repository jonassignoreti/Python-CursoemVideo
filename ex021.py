#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
import pygame #importar a biblioteca pygame
pygame.init() #iniciar o pygame
pygame.mixer.init() #iniciar mixer do pygame
pygame.mixer.music.load('ex021.mp3') #carregar o arquivo de som
pygame.mixer.music.play() #executar o mixer
pygame.event.wait() #para aguardar a música executar
