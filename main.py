import time

print("\nДобро пожаловать в игру \"Виселица\"")
print("   _____  \n"
      "  |     |    ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██      ██████   █████  ███    ███ ███████ \n"
      "  |     |    ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██     ██       ██   ██ ████  ████ ██      \n"
      "  |     |    ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██     ██   ███ ███████ ██ ████ ██ ███████ \n"
      "  |     O    ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██     ██    ██ ██   ██ ██  ██  ██ ██      \n"
      "  |    /|\   ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████      ██████  ██   ██ ██      ██ ███████ \n"
      "  |    / \                                                                                                           \n"
      "__|__\n")                                                                                                    
firstPlayerName = input("Введите ваше имя (первый игрок): ")
secondPlayerName = input("Введите ваше имя (второй игрок): ")
print("Привет, "+firstPlayerName+" и "+secondPlayerName+"! Удачи вам!")
time.sleep(2)
print("Игра вот-вот начнётся!\nДавайте поиграем в Виселицу!")
time.sleep(3)

def main():
    global wins
    global count
    global display
    global word
    global alreadyGuessed
    global length
    global playGame
    global roundCount
    global usedLetter
    wins = [0, 0]
    roundCount = ""
    while (not roundCount.isdigit()):
        if roundCount != "":
            print("Неверный ввод, попробуйте ввести число.\n")
        roundCount = input("Введите количество раундов: ")
    roundCount = int(roundCount)
    if (roundCount % 2 == 0):
        word = input(secondPlayerName + " загадайте слово: ")
    else:
        word = input(firstPlayerName + " загадайте слово: ")
    length = len(word)
    count = 0
    display = '_' * length
    alreadyGuessed = []
    playGame = ""
    usedLetter = []

def playLoop ():
    global playGame
    global wins
    global roundCount
    global length
    global word
    global usedLetter
    length = len(word)
    if wins[0] + wins[1] == roundCount:
        if wins[0] > wins[1]:
            print("Победил "+firstPlayerName+" со счётом "+str(wins[0])+":"+str(wins[1])+".")
        elif wins[0] == wins[1]:
            print("Ничья со счётом "+str(wins[0])+":"+str(wins[1])+".")
        else:
            print("Победил "+secondPlayerName+" со счётом "+str(wins[0])+":"+str(wins[1])+".")
        playGame = input("Вы хотите сыграть снова? (да , нет) \n")
        while playGame not in ["да", "Да", "дА", "ДА", "нет", "Нет", "нЕт", "неТ", "НЕт", "НеТ", "нЕТ", "НЕТ"]:
            playGame = input("Вы хотите сыграть снова? (да , нет) \n")
        if playGame in ["да", "Да", "дА", "ДА"]:
            main()
        elif playGame in ["нет", "Нет", "нЕт", "неТ", "НЕт", "НеТ", "нЕТ", "НЕТ"]:
            print("Спасибо за игру!")
            exit()
    else:
        hangman()

def hangman():
    global count
    global display
    global word
    global alreadyGuessed
    global playGame
    global wins
    global roundCount
    global usedLetter
    limit = 5
    guess = input("Слово палача: " + display + " Введите ваше предположение: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Неверный ввод, попробуйте ввести букву\n")
        hangman()
    elif guess in word:
        alreadyGuessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        while word[index+1:].find(guess) >= 0:
            index = word[index+1:].find(guess) + index + 1
            word = word[:index] + "_" + word[index + 1:]
            display = display[:index] + guess + display[index + 1:]
        print("\n")
    elif guess in alreadyGuessed:
        print("Попробуйте другую букву. Так как вы её вводили.\n")
    else:
        alreadyGuessed.extend([guess])
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Неверное предположение. " + str(limit - count) + " попыток осталось\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Неверное предположение. " + str(limit - count) + " попыток осталось\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Неверное предположение. " + str(limit - count) + " попыток осталось\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Неверное предположение. " + str(limit - count) + " попыток осталось\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Неверное предположение. Вас повесили!!!\n")
            print("Слово:", display, word)
            if roundCount % 2 == 0:
                if wins[0]+wins[1] % 2 == 0:
                    wins[1] += 1
                else:
                    wins[0] += 1
            else:
                if wins[0]+wins[1] % 2 == 0:
                    wins[0] += 1
                else:
                    wins[1] += 1
            if wins[0] + wins[1] != roundCount:
                if roundCount % 2 == 0:
                    if wins[0]+wins[1] % 2 == 0:
                        word = input(secondPlayerName + " загадайте слово: ")
                    else:
                        word = input(firstPlayerName + " загадайте слово: ")
                else:
                    if wins[0]+wins[1] % 2 == 0:
                        word = input(firstPlayerName + " загадайте слово: ")
                    else:
                        word = input(secondPlayerName + " загадайте слово: ")
                count = 0
                display = '_' * len(word)
                alreadyGuessed = []
                playGame = ""
            playLoop()
        
    if word == '_' * length:
        print("Поздравляю! Вы угадали слово верно!")
        if roundCount % 2 == 0:
            if wins[0]+wins[1] % 2 == 0:
                wins[1] += 1
            else:
                wins[0] += 1
        else:
            if wins[0]+wins[1] % 2 == 0:
                wins[0] += 1
            else:
                wins[1] += 1
        if (wins[0] + wins[1] != roundCount):
            if roundCount % 2 == 0:
                if wins[0]+wins[1] % 2 == 0:
                    word = input(secondPlayerName + " загадайте слово: ")
                else:
                    word = input(firstPlayerName + " загадайте слово: ")
            else:
                if wins[0]+wins[1] % 2 == 0:
                    word = input(firstPlayerName + " загадайте слово: ")
                else:
                    word = input(secondPlayerName + " загадайте слово: ")
            count = 0
            display = '_' * len(word)
            alreadyGuessed = []
            playGame = ""
        playLoop() 

    elif count != limit:
        hangman()

main()

hangman()