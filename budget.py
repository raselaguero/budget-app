class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        if amount > 0:
            self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        check = self.check_funds(amount)
        if check is True:
            if amount > 0:
                amount *= -1
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        result = 0
        for i in range(len(self.ledger)):
            result += self.ledger[i]["amount"]
        return result

    def transfer(self, amount, category):
        check = self.check_funds(amount)
        if check is True:
            if amount > 0:
                amount *= -1
                self.ledger.append({"amount": amount, "description": "Transfer to {}".format(category.name)})
            else:
                self.ledger.append({"amount": amount, "description": "Transfer to {}".format(category.name)})
            category.ledger.append({"amount": abs(amount), "description": "Transfer from {}".format(self.name)})
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if abs(amount) > balance:
            return False
        else:
            return True

    def budget_print(self):
        ini = self.ledger[0]["amount"]
        space = 15 - (len(str(ini)) + 3)
        print(self.name.center(30, '*'), 'initial deposit{space}{ini:.2f}'.format(ini=ini, space=' '*space)[:7], sep='\n')
        for l in range(1, len(self.ledger)):
            if str(self.ledger[l]['amount']).__contains__('.'):
                size = len(str(self.ledger[l]['amount']))
            else:
                size = len(str(self.ledger[l]['amount'])) + 3
            print(self.ledger[l]['description'][:23], '{amount:.2f}'.format(amount=self.ledger[l]['amount'])[:7].rjust(7 - size), sep=' '*(7 - size))
        print('Total: {total:.2f}'.format(total=self.get_balance())[:7])

def budget_average(lista):
    res = []
    suma = 0
    for i in range(0,len(lista)):
        for j in range(0, len(lista[i].ledger)):
            item = lista[i].ledger[j]['amount']
            if str(item).__contains__('-'):
                suma += abs(item)
        avg = suma * 100 / lista[i].ledger[0]['amount']
        suma = 0
        res.append(avg)
    return res

def create_spend_chart(lista):
    u = d = t = c = ''
    su = sd = st = 3
    maxi = 0
    avg = budget_average(lista)
    print('Percentage spent by category')
    for i in reversed(range(0,110,10)):
       print(str(i).rjust(3), '|', sep='', end=' ')
       for j in range(0, len(avg)):
           if avg[j] >= i and j == 0:
               u, su = 'o', 2
           if avg[j] >= i and j == 1:
               d, sd = 'o', 2
           if avg[j] >= i and j == 2:
               t, st = 'o', 2
           if avg[j] >= i and j == 3:
               c = 'o'
       print(u, sep='', end=' '*su)
       print(d, sep='', end=' '*sd)
       print(t, sep='', end=' '*st)
       print(c, sep='', end='\n')
    print('    -', '---'*len(lista), sep='')
    for i in range(0,len(lista)):
        if len(lista[i].name) > maxi:
            maxi = len(lista[i].name)
    for j in range(0,maxi):
        try:
            uno = lista[0].name[j]
        except:
            uno = ' '
        try:
            dos = lista[1].name[j]
        except:
            dos = ' '
        try:
            tres = lista[2].name[j]
        except:
            tres = ' '
        try:
            cuatro = lista[3].name[j]
        except:
            cuatro = ' '
        print('   ', uno, dos, tres, cuatro, sep='  ')