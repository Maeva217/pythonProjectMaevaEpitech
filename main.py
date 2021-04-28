# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name) -> object:
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Pycharm')



L = int(input("saisir nombre de lignes:"));
for i in range(L+1):
    for j in range(L*3-i+1):
       print(" ",end="")
    for j in range(L * 3 + 1):
           if j == L * 3 - i + 1:
               print("*", end="")
           else:
               print(" ", end="")
    for j in range(2*i-1+1):
        if j == 2*i-1 :
           print("*",end="")
        else:
           print(" ",end="")
    print()

