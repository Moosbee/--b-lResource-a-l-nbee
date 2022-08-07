





def int2roman(number):
    numerals={1:"I", 4:"IV", 5:"V", 9: "IX", 10:"X", 40:"XL", 50:"L",
              90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M", 9000:"MP", 10000:"P"}
    result=""
    for value, numeral in sorted(numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result






i=32768

#i=10

text="\n\n\n//Enchantments\n"
Roman="xxy"

for x in range(i):
    Roman=int2roman(x)
    text=text+'"enchantment.level.'+str(x)+'":"'+Roman+'",\n'


i=266

text=text+"\n\n\n//Potions\n"

for x in range(i):
    Roman=int2roman(x)
    text=text+'"potion.potency.'+str(x)+'":"'+Roman+'",\n'


f = open("./encant.txt", "w")
f.write(text)
f.close()



