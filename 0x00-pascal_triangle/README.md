## ALgorithim to generte the pascal triangle

1. Start by defining the number of rows of the triangle you want to print.
2. Create a list of lists called triangle to store the triangle. The first element of the list should be [1].
3. Use a loop to iterate through the remaining rows of the triangle. For each row, create a list called current_row and add the first element (which is always 1) to it.
4. Use another loop to iterate through the elements of the previous row, starting from the second element (since the first element is already 1). For each element, add the sum of the current element and the previous element from the previous row to current_row.
5. Add the last element (which is always 1) to current_row.
6. Append current_row to triangle.
7. Finally, print the triangle.
