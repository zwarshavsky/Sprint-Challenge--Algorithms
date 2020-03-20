#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) As input size increases, the runtime remains linear with increase in complexity due to increase in output. See proof. 

O(n)

b) Same as a above. A linear increase in complexity. See proofs.py for reasoning.  

O(n) 

c) This is what is called trivial recursion, because there is only one recursive call made per element, so time complexity remains steady (space does not, but that does not matter here) at O(n).

0(n)

## Exercise II

The most efficient way to go about this would be a binary search approach to determining the threshold at which floor the egg would not break. 

With x as total numbet of floors, I would try dropping egg at

floor x // 2 

If the egg breaks at this floor I would continue to apply binary search

so next floor I try is 

floor x // 4 

Once we have determine the approximate threshold with this approach, we would simply start dropping eggs above this floor until we find the floor at which the egg will break.   

The time complexity here is logarithmic because the time complexity is reduced with every subsequent iteration of the experiment.  

