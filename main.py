def printTree(printString):
    with open("output.txt","w+") as out:
        out.write(printString)
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
    tree = "\\begin{center}\n\\begin{tikzpicture}[sibling distance=5em,\nevery node/.style={shape=circle,draw,align=center,}]]\n\\node{"+root+"}\n"\
        + out + \
        ";\n\\end{tikzpicture}\n\\end{center}\n"
    printTree(tree)

if __name__ == '__main__':
    worker()
