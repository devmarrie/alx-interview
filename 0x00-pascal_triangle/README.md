## ALgorithim to generte the pascal triangle

Start by defining the number of rows of the triangle you want to print.
Create a list of lists called triangle to store the triangle. The first element of the list should be [1].
Use a loop to iterate through the remaining rows of the triangle. For each row, create a list called current_row and add the first element (which is always 1) to it.
Use another loop to iterate through the elements of the previous row, starting from the second element (since the first element is already 1). For each element, add the sum of the current element and the previous element from the previous row to current_row.
Add the last element (which is always 1) to current_row.
Append current_row to triangle.
Finally, print the triangle.
