<h1>The Grandest Staircase Of Them All</h1>

<p>With her LAMBCHOP doomsday device finished, Commander Lambda is preparing for her debut on the galactic stage - but in order to make a grand entrance, she needs a grand staircase! As her personal assistant, you've been tasked with figuring out how to build the best staircase EVER.</p>

<p>Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so she can pick the one with the most options.</p>

<p>Each type of staircase should consist of 2 or more steps.  No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)</p>

<p>
#<br />
##<br />
21
</p>

<p>When N = 4, you still only have 1 staircase choice:</p>

<p>
#<br />
#<br />
##<br/>
31
</p>

<p>But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:</p>

<p>
#<br />
#<br />
#<br />
##<br />
41
</p>

<p>
#<br />
##<br />
##<br />
32
</p>

<p>Write a function called answer(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!</p>

<h2>Test cases</h2>

<p><b>Inputs:</b>(int) n = 3
<br />
<b>Output:</b>(int) 1</p>

<p><b>Inputs:</b>(int) n = 200
<br />
<b>Output:</b>(int) 487067745</p>
