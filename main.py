import sys

def printTree(printString):
    try:
        if len(sys.argv)>1:
            with open(sys.argv[1],"w+") as out:
                out.write(printString)
        else:
            with open("output.txt","w+") as out:
                out.write(printString)
    except:
        print("FEHLER! Textfile konnte nicht geschrieben werden.")
    print(printString)

def treeNode(parent):
    left = input(f"Linkes Kind von {parent}?\n")
    right = input(f"Rechtes Kind von {parent}?\n")

    if left=="" or left.replace(" ","")=="-":
        left = "edge from parent [draw=none]"
    else:
        left = "node{"+left+"} " + treeNode(left)

    if right=="" or right.replace(" ","")=="-":
        right = "edge from parent [draw=none]"
    else:
        right = "node{"+right+"} " + treeNode(right)
    return "child{"+left+"}\nchild{"+right+"}\n"

def worker():
    root = input("Wurzel?\n")
    if root=="" or root.replace(" ","")=="-":
        print("Leerer Baum. Unzulässig.")
        return worker()
    left = input(f"Linkes Kind von {root}?\n")
    right = input(f"Rechtes Kind von {root}?\n")

    if left=="" or left.replace(" ","")=="-":
        left = "edge from parent [draw=none]"
    else:
        left = "node{"+left+"} " + treeNode(left)

    if right=="" or right.replace(" ","")=="-":
        right = "edge from parent [draw=none]"
    else:
        right = "node{"+right+"} " + treeNode(right)

    out = "child{"+left+"}\nchild{"+right+"}\n"
    levelstyles = [
    "every node/.style={circle, draw=black}",
    "level 1/.style={circle, draw=black,sibling distance=15em}",
    "level 2/.style={circle, draw=black,sibling distance=10em}",
    "level 3/.style={circle, draw=black,sibling distance=7em}",
    "level 4/.style={circle, draw=black,sibling distance=3em}",
    "level 4+/.style={circle, draw=black,sibling distance=3em}"
    ]
    tree = "\\begin{center}\n\\begin{tikzpicture}[\n"+ ",\n".join(levelstyles) +"]\n\\node{"+root+"}\n"\
        + out + \
        ";\n\\end{tikzpicture}\n\\end{center}\n"
    printTree(tree)

if __name__ == '__main__':
    worker()
