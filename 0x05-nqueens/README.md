##  N non attacking queens on n*n algorithm
1. Start in the leftmost column
2. If all queens are placed
    return true
3. Try all rows in the current column.  Do following
   for every tried row.
    _If the queen can be placed safely in this row
       then mark this [row, column] as part of the 
       solution and recursively check if placing  
       queen here leads to a solution.
    _If placing queen in [row, column] leads to a
       solution then return true.
    _If placing queen doesn't lead to a solution 
       then unmark this [row, column] (Backtrack) 
       and go to step (a) to try other rows.
4. If all rows have been tried and nothing worked, 
   return false to trigger backtracking.
5.  For all cells in a particular left diagonal , their row + col  = constant.
    For all cells in a particular right diagonal, their row – col + n – 1 = constant.
