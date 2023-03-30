## Algorithim
Initiaslise a set called vidited to keep track of the boxes which have been visited
Initialise a stack to keep track of the boxes to visit and push the first box
Loop through the stack and pop out the top element and add it to the visited if the box has not been visited yet ,find out the keys associated with the box ,loop through the keys to make sure they are within the boxes.length and add it to the stack.
Check if all the bxes have been visited by comparing the length of visited by n.
If they are equal return true else false
