class Calculation:
    """A class representing a math calculation consisting of 2 numbers and 1 operation"""
    def __init__(self, number1, number2, operation):
      self.number1 = number1
      self.number2 = number2
      self.operation = operation

    def getNumber1(self):
      return self.number1

    def getNumber2(self):
      return self.number2

    def getOperation(self):
      return self.operation

    def addition(self, number1, number2):
      return (number1 + number2)

    def multiplication(self, number1, number2):
      return (number1 * number2)

    def division(self, number1, number2):
      if(number2==0):
        return ('Cannot Divide by 0')

      return (number1 / number2)

    def subtraction(self, number1, number2):
        return (number1 - number2)                           

def isValidOperation(operation):
  validOperations=['/','+','-','*']
  if(operation not in validOperations):
    print('{operation} is not a valid operation. Please try a valid input.'.format(operation=operation))
    return False
  else:
    return True

def isValidNumber(number1, number2):
  if(not number1.isnumeric() or not number2.isnumeric()):
    print('{number1} or {number2} are not valid number(s). Please try a valid input.'.format(number1=number1, number2=number2))
    return False
  else:
    return True

def math(number1, number2, operation):
  calculator = Calculation(number1, number2, operation)
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
      output=calculator.division(number1, number2)

    if(operation == '*') :
      output=calculator.multiplication(number1, number2)

    if(operation == '+') :
      output=calculator.addition(number1, number2)

    if(operation == '-') :
      output=calculator.subtraction(number1, number2)

    print(output)

  except:
    print('Math Operation was Unsuccessful. Please review inputs...')
    print('Math is {number1} {operation} {number2}'.format(operation=operation, number1=number1, number2=number2))

def getInputs():
  operation = ''
  isValidOp = False
  isValidNum = False
  while not isValidOp:
    operation=input('Please input the operation (/ * + -) or type -help for help!   ')

    if(operation == '-help') :
      print('The / indicates division')
      print('The * indicates multiplication')
      print('The + indicates addition')
      print('The - indicates subtraction')

    isValidOp = isValidOperation(operation) 

  while not isValidNum :
    number1=input('Please input the first number for your {operation} operation   '.format(operation=operation))
    if(not number1.isnumeric()):
      print('{number1} is not valid number. Please try a valid input.'.format(number1=number1))
      continue
    number2=input('Please input the second number for your {operation} operation   '.format(operation=operation))
    if(not number2.isnumeric()):
      print('{number2} is not valid number. Please try a valid input.'.format(number2=number2))
      continue
    isValidNum=True # At this point the number is sanitised and is a valid input to perform maths on.
  return number1, number2, operation
      
print('Hello... Welcome to the Calculator....')

number1, number2, operation = getInputs()
math(number1, number2, operation)
