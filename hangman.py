# Hangman Game 
# PPO
import random

# Board 
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Class
class Hangman:
     def __init__(self, word):
          self.word = word
          self.correct_letters = []
          self.wrong_letters = []

     # Método para adivinhar a letra
     def guess(self, letter):
          if letter in self.word and letter not in self.correct_letters:
               self.correct_letters.append(letter)
          elif letter not in self.word and letter not in self.wrong_letters:
               self.wrong_letters.append(letter)
          else:
               return False
          return True

     # Método para verificar se o jogo terminou
     def hangman_over(self):
            lost = False
            won = self.hangman_won()
            if len(self.wrong_letters) == 6:
                lost = True
            return won or lost

     # Método para verificar se o jogador venceu
     def hangman_won(self):
          if '_' not in self.hide_word():
               return True
          else:
               return False

     # Método para não mostrar a letra no board
     def hide_word(self):
          w = ''
          for letter in self.word:
               if letter not in self.correct_letters:
                    w += '_ '
               else:
                    w += letter
          return w

     # Método para checar o status do game e imprimir o board na tela
     def print_game_status(self):
          print (board[len(self.wrong_letters)])
          print ('\nWord: ' + self.hide_word())
          iw = 0
          ic = 0 
          for letter in self.wrong_letters:
               if iw == 0:
                   print ('\nWrong Letters: ',)
               print (letter)
               iw+=1
          for letter in self.correct_letters:
               if ic == 0:
                    print ('Correct Letters: ',)
               print (letter)
               ic+=1

# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
     with open("palavras.txt", "rt") as f:
           bank = f.readlines()
     return bank[random.randint(0, len(bank))].strip()

# Método Main - Execução do Programa
def main():
# Object
     game = Hangman(rand_word())

     # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
     while not game.hangman_over():
          game.print_game_status()
          user_input = input('\nType a letter: ')
          game.guess(user_input)

     # Verifica o status do jogo
     game.print_game_status()

     # De acordo com o status, imprime mensagem na tela
     if game.hangman_won():
          print ('\nCongratulations! you won!')
     else:
          print ('\nGame over! You Lost.')
          print ('The word is ' + game.word)

# Executa o programa
if __name__ == "__main__":
     main()
