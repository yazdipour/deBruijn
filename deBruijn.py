import os
import sys, traceback

#Clear console
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
clear()

#Print name and description
print '''
\033[1;31m
     $$$$    $$$$$$$     $$$$$   $$$$   $$  $$ $$ $$$$$$ $$   $$
     $$  $$  $$          $$   $$ $$  $$ $$  $$ $$     $$ $$   $$
     $$   $$ $$          $$   $$ $$  $$ $$  $$ $$     $$ $$$  $$
     $$   $$ $$$$        $$$$$   $$ $$  $$  $$ $$     $$ $$ $ $$
     $$   $$ $$          $$   $$ $$$$   $$  $$ $$     $$ $$  $$$
     $$  $$  $$          $$   $$ $$ $$  $$  $$ $$ $$  $$ $$   $$
     $$$$    $$$$$$$     $$$$$   $$  $$ $$$$$$ $$ $$$$$$ $$   $$
\033[1;m
\033[1;31m
Create a de Bruijn sequence of a k sized alphabet with string length of n. Please note that the sequence is circular. 
\033[1;m

 \033[1;32m+ -- -- +=[ Author: RenatoSilva | Github: github.com/Renato-Silva\033[1;m
'''


#deBruijn fuction
def deBruijn(n, k):

 
   a = [ 0 ] * (n + 1)
   
   def gen(t, p):
      if t > n:
         for v in a[1:p + 1]:
           yield v
      else:
         a[t] = a[t - p]
         
         for v in gen(t + 1, p):
           yield v
         
         for j in xrange(a[t - p] + 1, k):
            a[t] = j
            for v in gen(t + 1, t):
              yield v
   
   return gen(1, 1)



#Ask user input for n and k
_k = int(raw_input('Size of alphabet (k): '))
_n = int(raw_input('Length of string (n): '))

#Ask user what alphabet to output
flag_shift=int(raw_input('Alphabet of numbers(1) or letters(2): '))
alphabet='0'
if(flag_shift==2):
	alphabet='A'




#Calculate sequence length and print it
length=_k**_n
print '\nde Bruijn Sequence length: k^n=',_k,'^',_n,'=',length,'\n'


#Print de Bruijn Sequence
print '\nYour de Bruijn Sequence is:\n'
print ''.join([ chr(ord(alphabet) + x) for x in deBruijn(_n, _k) ]),'\n'
