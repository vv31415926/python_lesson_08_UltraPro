import myLibAcc


def goGame():
    history = myLibAcc.read_history()

    persAcc = myLibAcc.getAccount(history)

    while True:
        myLibAcc.mainMenu()

        choice = myLibAcc.selectMenu()

        if choice == '1':    # пополнение счета
            persAcc = myLibAcc.addAcc(persAcc, history)

        elif choice == '2':  # Покупка
            persAcc = myLibAcc.goShop(persAcc, history)

        elif choice == '3':   # История
            myLibAcc.getHistory(history)

        elif choice == '4':   # выход
            myLibAcc.write_history(history)
            break
        else:
            myLibAcc.outError('Неверный пункт меню')


if __name__ == '__main__':
    goGame()
