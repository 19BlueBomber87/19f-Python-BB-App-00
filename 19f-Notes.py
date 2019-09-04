#1-09-19
##MARKK
###Book Notes
#http://begintocodewithpython.com/
#Below is a link to get the snaps Library
#https://github.com/Begintocodewithpython/samples
print('I <3 MoM')
print(2+3*4)
(2+3)*4
print('Hello', 'World')
print('Hello'+'World')
print('Hello'+'7')
print('Hello'*7)
ord('W')
chr(87)
chr(88)
bin(87), bin(0)
bin(1)
bin(2)
print('The Answer Is:', 2+2)
import random
print(random.randint(1,77))
print('You are thinking of the number is it?:', random.randint(1,777))
import time
print('Think of a Number_<@:D_\nI need time to calculate your guess.\n[Processing]')
time.sleep(3)
print('You guessed:\n', random.randint(1, 7777777))
time.sleep(5)
#py -m pip install pygame --user

import snaps
time.sleep(1)
snaps.display_message('<@:D_Pick a Number Between:\n7 and 77777_<@:D', size=50, color=(255,1,1))
time.sleep(3)
snaps.display_message('Need Time to Calculate Your Guess.\n[Processing]', size=60, color=(1,255,1))
time.sleep(3)
yourGuess = random.randint(7, 7777777)
snaps.display_message('<@:D\nYou Guessed the Number:\n<@:D', size=(70), color=(1,36,86))
time.sleep(3)
snaps.display_message(yourGuess)
time.sleep(3)
snaps.display_message('I <3 MoM')
time.sleep(3)
snaps.display_message('AK_4-Life', size=127, color=(51,255,255))
time.sleep(3)
snaps.display_message('{Niece + Nephew} = _<3_<3_<3_<3_', size=107,)
time.sleep(3)
snaps.display_message('BackGround Color: White\nForeGround Color: [Powershell Blue]\nAlign Text to the Top Left of Window', color=(1,36,86), size=50, horiz='Left', vert='top')
time.sleep(5)
snaps.display_image('mm2.jpg')
snaps.display_message ('Super Fighting\nRobot MegaMan!', color=(255,255,255), size=47, vert='top')
time.sleep(3)
snaps.play_sound('ding.wav')
time.sleep(5)