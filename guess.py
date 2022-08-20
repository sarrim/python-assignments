num = 7
attempt = 0

while attempt < 3:
    inp = input('Guess Number: ')
    if(int(inp) == 7):
        print('Correct Number is', inp)
        break;
    # elif(input != 7):
    #     continue;
    
    if(attempt == 2):
        print('Maximum chances exceed')
    attempt = attempt+1
# print('Done')
    