<h1>Ion Flux Relabeling</h1>

<p>Oh no! Commander Lambda's latest experiment to improve the  efficiency of her LAMBCHOP doomsday device has backfired spectacularly. She had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. She's having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly - quickly enough, perhaps, to earn a promotion!</p>

<p>Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, she performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:</p>

<p>7 3 6 1 2 4 5</p>

<p>Write a function answer(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter. For example, answer(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].</p>

<p>The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth. The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.</p>

<h2>Test cases</h2>
<p><b>Inputs:</b> (int) h = 3, (int list) q = [7, 3, 5, 1]
<br />
<b>Output:</b> (int list)[-1, 7, 6, 3]</p>

<p><b>Inputs:</b> (int) h = 5, (int list) q = [19, 14, 28]
<br />
<b>Output:</b> (int list) [21, 15, 29]</p>

