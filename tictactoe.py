"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #20 - Tic Tac Toe (tictactoe.py)


Author: Carter Berlind

Difficulty Level: 9/10

Prompt: Alexander challenges you to a game of Tic Tac Toe. Knowing the success of computers 
in games such as chess and go, you decide to give computers the much more challenging task of 
playing Tic Tac Toe. Your task is to create a function that, when given two positions on a 
Tic Tac Toe board, finds a square that completes it. If there is no square, return that 0. 
Inputs should be 2 integers from 1-9 representing position as shown below.

1   2   3
4   5   6
7   8   9

The output should be an integer representing a position on the board.

Constraints: If input integers are outside of this range, return the string “invalid”

Test Cases:
Input: 1,5;     Output: 9
Input: 2,3;     Output: 1
Input: 6,8;     Output: 0
Input: 7,3;     Output: 5
Input: 1,7;     Output: 4
"""

class Solution:
    def tic_tac_toe(self,a,b):
        # type a: int
        # type b: int
        # return type: int

        # TODO: Write code below to return an int with the solution to the prompt
        diag = [[1,3,5][3,5,7]]
        line = [[1,2,3][4,5,6][7,8,9]]
        column = [[1,4,7][2,5,8][3,6,9]]

        dist = abs(b-a)
        diagonal = False
        if dist%4 == 0 and b%2 == 1:
            for i in range(len(diag)):
                if a in diag[i]:
                    diag[i].remove(a)
                    diag[i].remove(b)
                    return diag[i][0]
        elif dist == 1:
            if a in [3,4,6,7] and b in [3,4,6,7]:
                return 0
            else:
                for i in range(len(line)):
                    if a in line[i]:
                        line[i].remove(a)
                        line[i].remove(b)
                        return line[i][0]
        elif dist == 2:
            if a in [3,5,6,8] or b in [3,5,6,8]:
                return 0
            else:
                for i in range(len(line)):
                    if a in line[i]:
                        line[i].remove(a)
                        line[i].remove(b)
                        return line[i][0]
        elif dist%3 == 0:
            for i in range(len(column)):
                    if a in column[i]:
                        column[i].remove(a)
                        column[i].remove(b)
                        return column[i][0]
        else:
            return 0





def main():
    num1 = int(input())
    num2 = int(input())

    tc1 = Solution()
    ans = tc1.tic_tac_toe(num1,num2)
    print(ans)

if __name__ == "__main__":
    main()