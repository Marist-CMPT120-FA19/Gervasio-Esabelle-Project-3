#Esabelle Gervasio
#Building a hashtag tree

def main():
    height=int(input("Please enter the height of the tree: "))
    tag = 1
    h = height
    while height >0:
        print(' ' * (height-1) + "#" * (tag))
        height -=1
        tag +=2
    print(" " * (h-1) + "#")
main()

