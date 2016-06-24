# global variable
roman_dict = {1:"I", 4:"IV", 5:"V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

# helper function
def convertToRomanNumerals(number, roman=[]):

    # base case
    if number == 0:
        return
    elif number in roman_dict:
        roman.append(roman_dict[number])
        number -= number
        convertToRomanNumerals(number, roman)
    elif number < 4:
        roman.append(roman_dict[1])
        number -= 1
        convertToRomanNumerals(number, roman)
    elif number < 9:
        roman.append(roman_dict[5])
        number -= 5
        convertToRomanNumerals(number, roman)
    elif number < 40:
        roman.append(roman_dict[10])
        number -= 10
        convertToRomanNumerals(number, roman)
    elif number < 50:
        roman.append(roman_dict[40])
        number -= 40
        convertToRomanNumerals(number, roman)
    elif number < 90:
        roman.append(roman_dict[50])
        number -= 50
        convertToRomanNumerals(number, roman)
    elif number < 100:
        roman.append(roman_dict[90])
        number -= 90
        convertToRomanNumerals(number, roman)
    elif number < 400:
        roman.append(roman_dict[100])
        number -= 100
        convertToRomanNumerals(number, roman)
    elif number < 500:
        roman.append(roman_dict[400])
        number -= 400
        convertToRomanNumerals(number, roman)
    elif number < 900:
        roman.append(roman_dict[500])
        number -= 500
        convertToRomanNumerals(number, roman)
    elif number < 1000:
        roman.append(roman_dict[900])
        number -= 900
        convertToRomanNumerals(number, roman)
    else:
        roman.append(roman_dict[1000])
        number -= 1000
        convertToRomanNumerals(number, roman)

    return ''.join(roman)

print convertToRomanNumerals(1, roman=[])
print convertToRomanNumerals(2, roman=[])
print convertToRomanNumerals(3, roman=[])
print convertToRomanNumerals(4, roman=[])
print convertToRomanNumerals(5, roman=[])
print convertToRomanNumerals(6, roman=[])
print convertToRomanNumerals(9, roman=[])
print convertToRomanNumerals(26, roman=[])
print convertToRomanNumerals(39, roman=[])
print convertToRomanNumerals(40, roman=[])
print convertToRomanNumerals(49, roman=[])
print convertToRomanNumerals(50, roman=[])
print convertToRomanNumerals(75, roman=[])
print convertToRomanNumerals(250, roman=[])
print convertToRomanNumerals(401, roman=[])
print convertToRomanNumerals(599, roman=[])
print convertToRomanNumerals(875, roman=[])
print convertToRomanNumerals(3900, roman=[])
print convertToRomanNumerals(634, roman=[])
