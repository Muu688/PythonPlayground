

def isValidOperation(operation):
  validOperations=['/','+','-','*']
  if(operation not in validOperations):
    print('{operation} is not a valid operation. Please try a valid input.'.format(operation=operation))
    return False
  else:
    return True

def math(number1, number2, operation):
  try:
    number1=float(number1)
  except:
    print('Cannot convert {number1} to a number'.format(number1=number1))
  try:    
     number2=float(number2)
  except:
    print('Cannot convert {number2} to a number'.format(number2=number2))
  try:
    if(operation == '/') :
      output=number1 / number2

    if(operation == '*') :
      output=number1 * number2

    if(operation == '+') :
      output=number1 + number2

    if(operation == '-') :
      output=number1 - number2

    print(output)

  except:
    print('Math Operation was Unsuccessful. Please review inputs...')
    print('Math is {number1} {operation} {number2}'.format(operation=operation, number1=number1, number2=number2))

def getInputs():
    number1=input('Please input the first number for your {operation} operation'.format(operation=operation))
    number2=input('Please input the second number for your {operation} operation'.format(operation=operation))

print('Hello... Welcome to the Calculator....')

operation = ''
isValidOp = False
while not isValidOp:
  operation=input('Please input the operation (/ * + -) or type -help for help!')

  if(operation == '-help') :
    print('The / indicates division')
    print('The * indicates multiplication')
    print('The + indicates addition')
    print('The - indicates subtraction')

  isValidOp = isValidOperation(operation)  

# print('Math is {number1} {operation} {number2}'.format(operation=operation, number1=number1, number2=number2))

getInputs()
math()