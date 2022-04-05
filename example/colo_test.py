import os


os.system('cls')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.BOLD+bcolors.FAIL+"[18:13] "+"\033[1;37;42m Alex "+bcolors.ENDC+": Hello")
print(bcolors.BOLD+bcolors.FAIL+"[18:14] "+"\033[1;37;46m Vova "+bcolors.ENDC+": Hi")


'''
print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
print('\033[2;31;43m CHEESY \033[0;0m')
print('\033[2;31;43m CHEESY \033[0;0m')
print('\x1b[1;37;41m' + 'Success!' + '\x1b[0m')
print('\x1b[41m' + 'Success!' + '\x1b[0m')
'''