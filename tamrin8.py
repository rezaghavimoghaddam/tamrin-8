def div(x , y):
    result = {}
    result['s'] = x['s'] * y['m']
    result['m'] = x['m'] * y['s']
    return result

def mul(x, y):
    result = {}
    result['s'] = x['s'] * y['s']
    result['m'] = x['m'] * y['m']
    return result

def sum(x, y):
    result = {}
    result['s'] = (x['s']*y['m']) + (x['m']*y['s'])
    result['m'] = x['m']*y['m']
    return result

def dif(x , y):
    result = {}
    result['s'] = (x['s']*y['m']) - (x['m']*y['s'])
    result['m'] = x['m']*y['m']
    return result


def show(f):
    print(f['s'], '/', f['m'])
    op = input("enter * or + or - or / :")
    if op == "*":
            mul_R = mul(a , b)
            show(mul_R)

    if op == "+":
            sum_R = sum(a , b)
            show(sum_R)

    if op == "-":
            dif_R = dif(a , b)
            show(dif_R)

    if op == "/":
            div_R = div(a, b)
            show(div_R)
while True:
    sk1 = int(input("Sorat kasr aval: "))
    mk1 = int(input("Makhrag kasr aval : "))
    sk2 = int(input("Sorat kasr dovom : "))
    sm2 = int(input("Makhrag kasr dovom : "))

    a = {'s':sk1, 'm':mk1}
    b = {'s':sk2, 'm':sm2}
    show(a)
    show(b)
    