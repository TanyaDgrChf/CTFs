import sympy

# Very long number
n = 2160489795493918825870689458820648828073650907916827108594219132976202835249425984494778310568338106260399032800745421512005980632641226298431130513637640125399673697368934008374907832728004469350033174207285393191694692228748281256956917290437627249889472471749973975591415828107248775449619403563269856991145789325659736854030396401772371148983463743700921913930643887223704115714270634525795771407138067936125866995910432010323584269926871467482064993332990516534083898654487467161183876470821163254662352951613205371404232685831299594035879

found = False
curr = 271
m = 7*(10**271)
while not found:
    curr -= 1
    print(f'7: ')
    print(n / (m + 7*(10**curr)))
    print(f'2: ')
    print(n / (m + 2*(10**curr)))
    inthing = input('7/2: ')
    inthing = inthing == '7'
    if inthing:
        m += 7*(10**curr)
    else:
        m += 2*(10**curr)