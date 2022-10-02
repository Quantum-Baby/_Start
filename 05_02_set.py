'''
THe game() function in a program lets a user play a game and returns 
the score as an integer. You need to read a file 'hiscore.txt' which
 is either blank or contains the previous hiscore. You need to write 
 a program to update the hiscore whereas gamea() breaks the hiscore
'''



def game():
    return 2

score = game()
with open('hiscore.txt') as f :
    hiscorestr = f.read()

if hiscorestr=='':
    with open('hiscore.txt', 'w') as f :
        f.write(str(score))

elif int(hiscorestr)<score :
    with open('hiscore.txt', 'w') as f :
        f.write(str(score))
