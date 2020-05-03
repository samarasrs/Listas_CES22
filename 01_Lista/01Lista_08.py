print('     ',end="")
for i in range(1,13):
    print(f'{i:4d}', end="")

print('\n  :--',end="")
n='----'
print(n*12,end="")
    
for i in range(1,13):
    print(f'\n{i:2d}:  ',end="")
    for k in range(1,13):
        print(f'{i*k:4d}',end="")
print('')
    