import json
import os


def outSeparator(f):
    def wrapper(*args, **kwargs):
        print('================')
        rez = f(*args, **kwargs)
        print('----------------\n')
        return rez
    return wrapper


@outSeparator
def mainMenu():
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')


@outSeparator
def addAcc(persAcc, history):
    # пополнение счета
    s = float(input('Введите сумму пополнения счёта (руб):'))
    persAcc, _ = setAccount(persAcc, s)
    history = setHistory('Пополнение', s, persAcc, history, 'одобрено')

    return persAcc


@outSeparator
def goShop( persAcc, history ):
    p = input('Введите, что покупаете:')
    t = float(input('Введите сумму покупки (руб):'))
    persAcc, isOK = setAccount( persAcc, t, input=False)
    if not isOK:
        print('На счету мало средств!\n')
        history = setHistory(p, t, persAcc, history, 'отказ')
    else:
        history = setHistory(p, t, persAcc, history, 'одобрено')

    return persAcc


@outSeparator
def setAccount(persAcc, money, input=True):
    rez = True
    if input:
        persAcc += money
    else:
        if persAcc < money:
            rez = False
        else:
            persAcc -= money

    return persAcc, rez


@outSeparator
def getHistory( history ):
    print('История покупок: ')
    lst = list_history(history)
    for v in lst:
        print(v)
    input('Нажмите любую клавишу...')

def setHistory( product, money, pers_acc, history, accept ):
    dic={}
    dic['step'] = product
    dic['money'] = str(money)
    dic['account'] = str(pers_acc)
    dic['accept'] = accept

    history.append( dic )
    return history


def list_history( history ):
    lst = []
    for d in history:
        lst.append( d['step']+', '+d['money']+'руб., остаток:'+d['account']+'руб., - '+d['accept']  )
    return lst
# *********************************************


def getAccount( history ):
    if len( history ) > 0:
        d = history[-1]
        r = float( d['account'] )
    else:
        r = 0
    return r


def read_history():
    if os.path.exists( 'history.json' ):
        with open( 'history.json', 'r' ) as f:
            history = json.load( f )
    else:
        history = []

    return history


def write_history( h ):
    if len(h) > 0:
        with open( 'history.json', 'w' ) as f:
            json.dump( h, f  )


def outError( s ):
    print(s)

@outSeparator
def selectMenu():
    choice = input('Выберите пункт меню: ')
    return choice