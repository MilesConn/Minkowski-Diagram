This was code written for my Modern Physics Lab. We were graded on presentation 
and not on quality of code as you might be able to tell. The program creates a graph 
of the space-time dilation at a point in space. 

##### Key:
+ Solid Red Lines - initial dilation of `ct'` at origin
+ Solid Blue Line - initial dilation of `x position` at origin
+ Solid Green Line - `C` in all intertial reference frames
+ Dashed Red Lines - simultaneity of time in moving reference frame
+ Dashed Blue Lines - simultaneity of position in moving reference frame
+ Intersection of Yellow Lines - point of occurence
+ Solid Yellow Lines - edge of light cone at a point
+ Yellow Area - indicates the possible places in time and space that could be the cause and effect of the graped point

##### Usage:

On the command line use `python3 Minkowski_Diagram.py v x-cord y-cord` where v is a float for the speed of the moving reference frame (between 0 and 1) and the `x-cords` and `y-cords` are integers betweeen -10 and 10.

For instance: `python Minkowski_Diagram.py .5 1 3  `

###### Future Updates:
 1. Comment and improve quality of code
 2. Improve CLI capabilities 

