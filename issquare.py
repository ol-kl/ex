class Node:
    def __init__(self, x, y, left=None, right=None, down=None, up=None):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.x = x
        self.y = y

def count_squares(nodes):
    squares = 0
    for node in nodes:
        top_left = node
        top_right = node.right
        while(top_right):
            bottom_right = top_right.down
            side_len = top_right.x - top_left.x
            while(bottom_right and (top_right.y - bottom_right.y <= side_len)):
                if top_right.y - bottom_right.y == side_len:
                    bottom_left = bottom_right.left
                    while(bottom_left and (bottom_right.x - bottom_left.x <= side_len)):
                        if bottom_right.x - bottom_left.x == side_len:
                            while(bottom_left.up and bottom_left.up is not top_left):
                                bottom_left = bottom_left.up
                            if (bottom_left.up):
                                squares = squares + 1
                        bottom_left = bottom_left.left
                bottom_right = bottom_right.down
            top_right = top_right.right
    return squares
            
            
task = [Node(5,60), Node(10,60), Node(15,60),
        Node(5,55), Node(10,55), Node(15,55),
        Node(5,50), Node(10,50), Node(15,50)]
task[0].right = task[1]
task[0].down = task[3]
task[1].left = task[0]
task[1].down = task[4]
task[1].right = task[2]
task[2].left = task[1]
task[2].down = task[5]
task[3].up = task[0]
task[3].right = task[4]
task[3].down = task[6]
task[4].left = task[3]
task[4].up = task[1]
task[4].right = task[5]
task[4].down = task[7]
task[5].left= task[4]
task[5].up = task[2]
task[5].down = task[8]
task[6].up = task[3]
task[6].right = task[7]
task[7].left = task[6]
task[7].up = task[4]
task[7].right = task[8]
task[8].left = task[7]
task[8].up = task[5]
        
def main():
    print("Squares:", count_squares(task))

if __name__ == "__main__":
    main()
