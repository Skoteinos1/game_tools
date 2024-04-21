# Mastermind Solver
Helps to solve mastermind game.<br>
<br>
It is not that hard to solve, but I thought it would be nice project, program that can solve this game.<br>
<br>
It is very simple, it generates all possible combinations. if you enter your guess and its result, it will print you out all remaining possible combination.<br>
Repeat until game is solved.<br>
<br>
Steps which I used to solve game on picture:<br>
remaining_options = remove_wrong_possibilities((('pu', 'or', 'bl', 'ye'), (1, 1)))<br>
remaining_options = remove_wrong_possibilities((('re', 'br', 'gr', 'pi'), (1, 0)))<br>
remaining_options = remove_wrong_possibilities((('pu', 'gr', 'gr', 'or'), (0, 2)))<br>
<br>
![Picure of Mastermind Game](https://github.com/Skoteinos1/mastermind_solver/blob/main/masterm.png)
