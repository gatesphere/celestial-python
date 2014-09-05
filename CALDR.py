#!/usr/bin/env python

import os 
def home():
  clear = 'cls' if os.name == 'nt' else 'clear'
  os.system(clear)
def tab(n):
  return ' '*n
def main():
  home()
  print_welcome_banner()
  while True:
    choose_mode()

  
def print_welcome_banner():
  print; print; print
  print tab(10) + '------------------'
  print tab(10) + 'I    CALENDAR    I'
  print tab(10) + '------------------'
  print; print; print
  print tab(2) + 'A PERPETUAL CALENDAR, DAY-OF-WEEK,'
  print tab(7) + 'AND HOLIDAY PROGRAM'
  print; print
  print tab(5) + 'BY ERIC BURGESS F.R.A.S.'

if __name__=='__main__':
  main() 
