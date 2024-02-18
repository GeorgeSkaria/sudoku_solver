'''gridip=[]
for i in range(9):
    row=input().split()
    gridip.append(row)'''

gridd=[
  [7,8,0,4,0,0,1,2,0],
  [6,0,0,0,7,5,0,0,9],
  [0,0,0,6,0,1,0,7,8],
  [0,0,7,0,4,0,2,6,0],
  [0,0,1,0,5,0,9,3,0],
  [9,0,4,0,6,0,0,0,5],
  [0,7,0,3,0,0,0,1,2],
  [1,2,0,0,0,7,4,0,0],
  [0,4,9,2,0,6,0,0,7],
]



def print(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ")
    

def empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if int(grid[i][j])==0:
                return (i,j)
    return None


def insert(grid):
    find = empty(grid)
    if not find:
        return True  
    else:
        row,col=find

    for i in range(1, 10):
        if valid(grid,i,(row, col)):
            grid[row][col]=i
            if insert(grid):
                return True 
            grid[row][col]=0 
    return False 


def valid(grid,c,pos):
    for i in range(len(grid[0])):
        if int(grid[pos[0]][i])==c and pos[1]!=i:
            return False
        
    for i in range(len(grid)):
        if int(grid[i][pos[1]])==c and pos[0]!=i:
            return False

    suba=pos[1]//3
    subb=pos[0]//3

    for i in range(subb*3,subb*3+3):
        for j in range(suba*3,suba*3+3):
            if int(grid[i][j])==c and (i,j)!=pos:
                return False
    return True


'''insert(gridip)
for i in range(9):
    for j in range(9):
        print(gridip[i][j],end=' ')
    print()'''

print(gridd)
insert(gridd)
print("___________________")
print(gridd)