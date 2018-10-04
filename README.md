This problem is a programming version of [Problem 185](https://www.hackerrank.com/external_redirect?to=https://projecteuler.net/problem=185 "Problem 185") from [projecteuler.net](https://www.hackerrank.com/external_redirect?to=https://projecteuler.net/ "projecteuler.net")

The game Number Mind is a variant of the well known game Master Mind.

Instead of coloured pegs, you have to guess a secret sequence of digits. After each guess you're only told in how many places you've guessed the correct digit. So, if the sequence was  and you guessed , you'd be told that you have one correct digit; however, you would NOT be told that you also have another digit in the wrong place.

For instance, given the following guesses for a -digit secret sequence,

90342; 2 correct 
70794; 0 correct 
39458; 2 correct 
34109; 1 correct 
51545; 2 correct 
12531; 1 correct

The correct sequence 39542  is unique.

Based on the some guesses, find the unique 12-digit secret sequence.

#### Input Format

First line of every input file contains a single integer   the number of guesses.  lines follow each containing the 12-digit guess sequence  and the number of correct digits for this guess `c_i`.

#### Constraints
 `20 <= n <= 30`
  `0 <= c_i 3 `


#### Output Format

Output the string with exactly 12 digits  the unique valid answer to the guesses.

#### Sample Input

20
228569150065 1
907564288621 0
496954400043 0
713459943615 0
211421327491 1
258317293172 0
919252724339 1
197103476352 0
151173430038 0
063794395936 0
504759866532 1
502906565456 0
790539816536 0
595873942664 1
346602334981 0
988808475766 1
559203789779 0
498580144863 1
441454897857 1
622818801178 0

#### Sample Input

884045122207
