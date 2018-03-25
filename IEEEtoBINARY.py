def sign(num):
    if num[0] == '-':
        return 1
    else:
        return 0

def convert(num, mantissa,e):
    # check if there is a decimal, if so, split it into two parts
    intPart = num
    decimal = 0
    mantissa = int(mantissa)
    if '.' in num:
        intPart = int(num[:num.find('.')])
        decimal = float(num[num.find('.'):])
    # convert the integer part into binary, or use the exponent (if it has no integer part)
    convertInt = "0"
    if intPart != 0:
        convertInt = str("{0:b}".format(int(intPart)))
    # convert the decimal part (if there is one)
    if decimal != 0:
        numAfterOne = 0
        # find the first 1 (if there is an integer part)
        if intPart != 0:
            numAfterOne = len(convertInt)-(convertInt.find('1')+1)
        elif intPart == 0:
            numAfterOne = -e
        # is the numAfterOne == mantissa
        if (numAfterOne > mantissa) or (numAfterOne == mantissa):
            return convertInt[convertInt.find('1')+1:convertInt.find('1')+1+mantissa]
        while numAfterOne < mantissa:
            tempDecimal = decimal * 2
            print(decimal, tempDecimal)
            if (tempDecimal > 1) or (tempDecimal == 1):
                convertInt += "1"
                decimal = tempDecimal - 1
            else:
                decimal = tempDecimal
                convertInt += "0"
            numAfterOne+=1
    if intPart !=0:
        return convertInt[convertInt.find('1')+1:int(convertInt.find('1')+1+(mantissa))]
    else:
        return convertInt[convertInt.find('1')+1:int(convertInt.find('1')+1+(mantissa)+int(e))]

def exponent(num, bias, exponentSize):
    exponent = 0
    newNum = float(num)
    # get the number to a number between 1 and 2 with an exponent
    # if its greater than 1
    if float(newNum) > 1:
        tempNum = newNum
        while(newNum > 2):
            exponent += 1
            tempNum = newNum/(2**exponent)
            if ((tempNum > 1) or (tempNum == 1)) and (tempNum < 2):
                newNum = tempNum
    # if its less than 0
    if float(newNum) < 1:
        tempNum = newNum
        while(newNum < 1):
            exponent += 1
            tempNum = newNum/(2**(-exponent))
            if ((tempNum > 1) or (tempNum == 1)) and (tempNum < 2):
                newNum = tempNum
        exponent = -exponent
    # now add the bias to the exponent
    exponent = exponent + int(bias)
    # convert the number to binary
    convertExponent = "{0:b}".format(exponent)

    # limit the size of the exponent
    # if the exponent is larger, make it smaller
    if len(str(convertExponent)) > int(exponentSize):
        convertExponent = convertExponent[:int(exponentSize)]
    # if the exponent is smaller, make it larger (via sign extension w/ 0's)
    elif len(str(convertExponent)) < int(exponentSize):
        numZeroes = int(exponentSize) - (len(str(convertExponent)))
        convertExponent = numZeroes*"0"+convertExponent
    return (-(exponent-int(bias))),convertExponent

def main():
    # get the number from the user
    num = input("Enter the number: ")

    # get the mantissa max width allowed
    mantissa = input("Enter the size of mantissa: ")

    # get the exponent max width allowed
    exponentSize = input("Enter the size of exponent: ")

    # get the bias
    bias = input("Enter the excess/bias: ")

    # determine the sign (s)
    s = sign(num)
    # find the exponent
    expon = 0
    e = 0
    if s == 0:
        expon, e = exponent(num, bias, exponentSize)
    elif s == 1:
        expon, e = exponent(num[1:], bias, exponentSize)
    # convert the number to obtain mantissa
    m = 0
    if s == 0:
        m = convert(num, mantissa, expon)
    elif s == 1:
        m = convert(num[1:], mantissa,expon)

    # put it all together
    binary = str(s)+e+m
    print(binary)

    compareNum = input("Enter the number to compare to:")
    if(compareNum == binary):
        print("They match!")
    else:
        print("Nope :(")

main()
