Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

======= RESTART: /Users/larrygrace/Documents/MakupProgram/make_up .py =======
           Speech Synonyms
1. Convert a Text file with synonyms
Q. Quit 
==> 
Traceback (most recent call last):
  File "/Users/larrygrace/Documents/MakupProgram/make_up .py", line 52, in <module>
    choice = show_menu(MAIN_MENU, MAIN_CHOICES)
  File "/Users/larrygrace/Documents/MakupProgram/make_up .py", line 42, in show_menu
    user_choice = input(menu).upper()
KeyboardInterrupt
>>> c = open_list()
>>> d = return_list_from_file(c)
>>> len(d)
1521
>>> d[0]
'April, Apr\n'
>>> d[0].strip().split(",")
['April', ' Apr']
>>> e = []
>>> for item in d:
	l = item.split(",")
	e.append(l)

	
>>> len(e)
1521
>>> e[0]
['April', ' Apr\n']
>>> l = e[0]
>>> for item in l:
	item.strip()

	
'April'
'Apr'
>>> l
['April', ' Apr\n']
>>> for idx, item in enumerate(l):
	item = item.strip()
	l[idx] = item

	
>>> l
['April', 'Apr']
>>> len(e)
1521
>>> e[0]
['April', 'Apr']
>>> my_list = [ e[0], e[1], e[2] ]
>>> my_list
[['April', 'Apr'], ['China', " People's Republic of China", ' mainland China', ' Communist China', ' Red China', ' PRC', ' Cathay\n'], ['December', ' Dec\n']]
>>> for row in my_list:
	for idx, syn in enumerate(row):
		syn = syn.strip()
		row[idx] = syn

		
>>> my_list
[['April', 'Apr'], ['China', "People's Republic of China", 'mainland China', 'Communist China', 'Red China', 'PRC', 'Cathay'], ['December', 'Dec']]
>>> 
