#include <ButtonConstants.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>


#Region ### START Koda GUI section ### Form=

Global $gui_box = GUICreate("Move Analysis",288, 100)
GUICtrlCreateLabel("Analyze Probability of Winning & Best Next Move", 30,30)
Global $gui_button = GUICtrlCreateButton("Analyze", 96, 60, 75, 25)
GUICtrlSetCursor (-1, 2)

#EndRegion ### END Koda GUI section ###


Global Const $sleep_fast = 100
Global Const $sleep_slow = 800

Run('scid.exe')
Opt("WinTitleMatchMode",2)

WinWaitActive("(Example")
WinClose("List")
GUISetState(@SW_SHOW)

While 1

	$nMsg = GUIGetMsg()

	Switch $nMsg
	  Case $GUI_EVENT_CLOSE
			Exit

	  Case $gui_button
			current_board()
			;prob()
			next_move()
			Exit

	EndSwitch

WEnd

Func current_board()

   WinActivate("(Example")
   Send('{LALT}{s}{c}')

   Sleep($sleep_fast)
   Send('{ENTER}')
   Sleep($sleep_slow)
   Send('!{F4}')
   Sleep($sleep_fast)

EndFunc

Func prob()

   WinActivate("(Example")
   Send('^{i}')
   Sleep($sleep_fast)

   WinActivate("Filter")
   Sleep($sleep_fast)
   Send('!{f}{p}')

   Sleep($sleep_fast)
   Send("self_stats.txt")
   Send('{ENTER}')

EndFunc

Func next_move()

   Sleep($sleep_slow)
   WinActivate("(Example")
   Send('^{t}')
   Sleep($sleep_fast)

   WinActivate("Tree")
   Sleep($sleep_fast)
   Send('!{f}{o}')
   WinClose("Tree")

   Run("notepad.exe")
   WinWaitActive("Untitled - Notepad")
   Send('^{v}')
   Sleep($sleep_fast)
   Send('!{f}{a}')
   Sleep($sleep_fast)
   Send("D:\Developer\Chess\Scid-4.6.4\bin\self_prob.txt")
   Sleep($sleep_fast)
   Send('{ENTER}')
   Sleep($sleep_fast)
   WinClose("Notepad")

EndFunc