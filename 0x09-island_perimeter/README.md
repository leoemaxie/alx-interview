# Island Perimeter

This is a solution to the "Island Perimeter" problem from the ALX interview preparation project.

## Problem Description

Given a 2D grid map of `1`s (land) and `0`s (water), compute the perimeter of the island. The grid is surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length `1`. The grid is rectangular, width and height don't exceed `100`. Determine the perimeter of the island.

## Example

Input:

```
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
```

Output:

```
16
```

## Approach

To solve this problem, we can iterate over each cell in the grid and count the number of neighboring cells that are either water or outside the grid boundaries. The sum of these counts will give us the perimeter of the island.

## Complexity Analysis

The time complexity for this approach is `O(m * n)`, where `m` is the number of rows and `n` is the number of columns in the grid. The space complexity is `O(1)`.
