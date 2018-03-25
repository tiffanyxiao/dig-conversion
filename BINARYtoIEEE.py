# need to change 32 later on
def hexConvert(value, width):
    width = int(width)
    b = bin(int(value, 16))
    s = b[2:].zfill(width)
    return ('{:0'+str(width)+'b}').format(int(value, 16))

def exponent(e, bias):
    # convert e to decimal number
    convertExponent = int(e, 2)
    # subtract bias
    return convertExponent - int(bias)

def mantissa(m, mantissaLength):
    result = 0
    m = '0.'+m
    for i in range(1,int(mantissaLength)):
        result += int(m[2+i])*(2**(-i))
    return result

def main():
    num = input("Input number: ")

    # convert to hex if needed
    hex = input("y for Hex, n for binary: ")
    if (hex == 'y'):
        width = input("Input width of number (32 by default): ")
        num = hexConvert(num, width)

    # get the sign
    s = int(num[0])

    # get the exponent
    exponentLength = input("Input width of exponent (8 by default): ")
    e = num[1:int(exponentLength)+1]
    # get the decimal value of the exponent
    bias = input("Input bias/excess (default 127): ")
    decE = exponent(e, bias)

    # get the mantissa
    mantissaLength = input("Input width of mantissa (23 by default): ")
    m = num[int(exponentLength):int(exponentLength)+int(mantissaLength)]
    decM = mantissa(m, mantissaLength)

    finalNum = ((-1)**(s))*(1+decM)*(2**decE)
    print(finalNum)

main()
