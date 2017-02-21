from colorconsole import terminal

def resetcolor():
	#term.reset does not appear to be resetting the color correctly
	#set the terminal back to lt grey on black
	term.cprint(7,0,'')

term = terminal.get_terminal(conEmu=False)

term.clear()
term.cprint(5, 0, " test\n")
resetcolor()
#term.test()


#colors
'''
          "BLACK": 0,
          "BLUE": 1,
          "GREEN": 2,
          "CYAN": 3,
          "RED": 4,
          "PURPLE": 5,
          "BROWN": 6,
          "LGREY": 7,
          "DGRAY": 8,
          "LBLUE": 9,
          "LGREEN": 10,
          "LCYAN": 11,
          "LRED": 12,
          "LPURPLE": 13,
          "YELLOW": 14,
          "WHITE": 15
 '''