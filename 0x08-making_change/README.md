# 0-making_change

This repository contains the solution for the "Making Change" problem. The goal of this project is to implement an algorithm that calculates the minimum number of coins needed to make a certain amount of change.

## Problem Description

Given a set of coin denominations and a target amount, the task is to find the minimum number of coins needed to make the target amount. The set of coin denominations is provided as an array, and each coin can be used an unlimited number of times.

For example, if the target amount is 25 cents and the available coin denominations are [1, 5, 10, 25], the minimum number of coins needed to make 25 cents is 1 (a single 25 cent coin).

## Implementation

The solution to this problem can be implemented using dynamic programming. The algorithm maintains an array to store the minimum number of coins needed for each target amount from 0 to the given target amount. By iteratively calculating the minimum number of coins for each amount, the algorithm builds up the solution until the target amount is reached.

The implementation of the algorithm can be found in the `making_change.py` file.

## Usage

To use the algorithm, follow these steps:

1. Clone this repository: `git clone https://github.com/leoemaxie/0x08-making_change.git`
2. Navigate to the project directory: `cd 0x08-making_change`
3. Run the algorithm: `python making_change.py`

## Testing

The `tests` directory contains a set of test cases to verify the correctness of the algorithm. To run the tests, execute the following command:

```
python -m unittest discover tests
```

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
