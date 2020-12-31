# Algorithm & Data Structure Fundamentals

## Overview
This is a collection of different algorithms I developed for my Introduction to Algorithms class (6.006). Specifically, I cover elementary data structures (dynamic arrays, heaps, balanced binary search trees, hash tables) and algorithmic approaches to solve classical problems (sorting, graph searching, dynamic programming).

## heaps.py:
Implementation of a database using min and max heaps to identify k items that are neither the [n−k]/2 largest nor the [n−k]/2 smallest. With this, we developed 2 methods:
1. record_item(s): adds item of size s to database
2. best_items(): determines k items as defined above

## AVL.py:
Implementation of an AVL tree (aka self-balancing BST), where each node has a “time” attribute and “value” attribute (either “good” or “bad”). With this, we developed 2 methods:
1. update(time, val): change “value” of node with time “time” to “val”
2. range_imbalance(t1, t2): return number difference of nodes with “good” values and nodes with “bad” values within range [t1, t2]

## poker_map.py:
Implementation of a direct access array involving hand frequency tables to determine the most likely Poker hand h(D,i,k) given a set of unique conditions:
1. The deck D starts in a pile face down in a known order. 
2. The deck is cut at random at some location i ∈ {0, . . . , n − 1}, i.e., move the top i cards in order to the bottom of the deck. 
3. You are dealt the top k cards from the top of the cut deck. 
4. You sort your k cards alphabetically, resulting in your hand.

## peg_solitaire.py:
Implementation of algorithm that determines a sequence of moves solving the current board state of a peg solitaire game (with 4 directions). Utilizes construction of a graph to explore board configurations, and also handles “inverse” moves.

## max_downhill.py:
Implementation of DFS algorithm with DAG relaxation that determines the “downhill” path with maximum “awesomeness” from a collection of different routes. A route connects a pair of nodes with different “height” attributes; “downhill” hence means going from higher to lower height. Each route also has its own “awesomeness” attribute, corresponding to the value of the route’s desirability.

## max_nested_boxes.py:
Implementation of DP algorithm that determines the maximum possible number of boxes that can be nested within one another. We want each “inner” box being oriented such that its dimensions are less than or equal to the previous box’s dimensions.
