#Collatz Sequencer from user input, uses Collatz conjecture to reduce any integer down to a value of 1.
#If n is even then n/2, if n is odd then 3n+1, repeating until the final value of 1 is achieved.

def collatz(number):

  if number % 2 == 0:
    print(number // 2)
    return number // 2
  else:
    print(3 * number + 1)
    return 3 * number + 1
  

                  
while True:
    try:
      n = input('Input an integer: ')
      original = n
      counter = 0
      while n != 1:
        n = collatz(int(n))
        counter += 1
      print('It took ' + str(counter) + ' iterations to get ' + str(original) + ' down to 1.')
    except ValueError:
      print('You must enter an integer')
      continue
          

