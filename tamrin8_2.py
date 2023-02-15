
def dif(t1 , t2):
    result = {}
    result['h'] = t2['h'] - t1['h']
    result['m'] = t2['m'] - t1['m']
    result['s'] = t2['s'] - t1['s']
    if result['s'] < 0:
        result['m'] -= 1
        result['s'] += 60
    if result['m'] < 0 :
        result['h'] -= 1
        result['m'] += 60
    if result['h'] >= 24:
        result['h'] -= 24
    return result
def sum(t1 , t2):
    result = {}
    result['h'] = t2['h'] - t1['h']
    result['m'] = t2['m'] - t1['m']
    result['s'] = t2['s'] - t1['s']
    if result['s'] >= 60:
       result['s'] -= 60
       result['m'] +=1
    if result['m'] >= 60:
       result['m'] -= 60 
       result['h'] += 1
    if result['h'] >= 24:
       result['h'] -= 24
    return result

def show(t):
    print(t['h'], ':', t['m'], ':', t['s'])
while True:
    t1_h = int(input("enter h1 : "))
    t1_m = int(input("enter m1: "))
    t1_s = int(input("enter s1 : "))
    t2_h = int(input("enter h2: "))
    t2_m = int(input("enter m2: "))
    t2_s = int(input("enter s2: "))
    t1 = {'h':t1_h, 'm':t1_m, 's':t1_s}
    t2 = {'h':t2_h, 'm':t2_m, 's':t2_s}
    show(t1)
    show(t2)
    
    op = input("+ or - :")
    if op == "+":
            sum_result = sum(t1, t2)
            show(sum_result)
    if op == "-":
            dif_result = dif(t1, t2)
            show(dif_result)       
        