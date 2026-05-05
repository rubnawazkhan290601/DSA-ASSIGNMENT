# Assignment 01

## Student Details

* Name: Rubnawaz Khan
* GitHub Username: rubnawazkhan290601

---

# Problem 1: Cyclic Substring Maximum Sum

## Problem Statement

Given a string consisting of lowercase English letters, each character has a value equal to its alphabetical position:

* a = 1
* b = 2
* ...
* z = 26

Find the maximum possible sum of values from any cyclic substring such that no character repeats.

---

## Approach

* Duplicate the string to handle cyclic substrings.
* Use Sliding Window technique.
* Maintain:

  * current sum
  * unique characters
  * maximum sum

Time Complexity: O(N)

---

## Sample Input

```text id="j7pb43"
abca
```

## Sample Output

```text id="i0gkqt"
6
```

---

## Explanation

Possible cyclic substrings:

* abc → 6
* bca → 6
* cab → 6

Maximum sum = 6
# DSA-ASSIGNMENT
..# Problem 2: Array Transformation Cost Minimization

## Problem Statement

You are given an integer array of size N and a fixed integer K.

You can perform the following operation any number of times:

* Choose any index and replace:

  * A[i] with A[i] + K
  * or A[i] with A[i] - K

The goal is to make all array elements equal using the minimum number of operations.

If it is impossible, return -1.

---

## Approach

* Check whether all elements can be converted to a common value.
* The difference between elements must be divisible by K.
* Choose a target value that minimizes total operations.
* Count operations required for each element.

Time Complexity: O(N log N)

---

## Sample Input

```text id="0r9k0d"
4
1 3 5 7
2
```

## Sample Output

```text id="y4djlwm"
4
```

---

## Explanation

Using K = 2:

* 1 → 5 requires 2 operations
* 3 → 5 requires 1 operation
* 5 → 5 requires 0 operations
* 7 → 5 requires 1 operation

Total operations = 4

