## asana_buddy

This CLI application contains a library of asanas (AKA yoga poses). When the program starts, you can optionally view the library to learn about each pose. After that, it will prompt you for the amount of time you want to exercise in minutes, then create a randomized routine for you. 

### The conception

In order to develop a randomized routine which maintains a natural body flow, each asana has been assigned two categories. 
- Body position
  - standing
  - seated
  - supine
  - prone
  - arm & leg
- Body action
  - neutral
  - balancing
  - forward bend
  - back bend
  - twist

Based on these categories, the functions can better decide which pose to put next. For example, it would be quite awkward to transition from a standing/balancing pose to a prone/neutral pose (and most likely result in a face plant!).   

It also wouldn't be very fun to do an entire routine of back bends, or only seated poses. To combat this, the randomly generated routine is acutally a list of sequences. Each sequence contains 5 poses of the same body position category, and the last asana in the sequence will have a body action which makes sense for a transition into a new body position.  

The last major factor to consider is the amount of time for which you hold each pose in the routine. Since the user inputs the length of time they want to exercise in minutes, each sequence is meant to last 60 seconds, with each pose lasting anywhere between 8 and 15 seconds. It may sound short, but if you have ever tried to hold a back bend for more than 15 seconds, you'll be grateful! However, this application is better suited for shorter, fast-paced routines. Alongside each sequence list of poses is a sister list of numbers which represent the length in seconds to hold each pose.

### How it works

1. After a prompt, you type 'y' or 'n' to view the library and learn more about the poses
2. After a prompt, you type an integer between 3 and 120 to determine the length of the routine in minutes
3. After a valid integer is given, the routine build is initiated
4. a method of the class 'library' called _build_routine is called. It is passed a starting pose of 'mountain', and the user's chosen length
    - the first sequence is built will always be of category 'standing'
    - _build_routine will continue creating instances of the 'sequence' class until the length is reached
5. each sequence is passed the first pose, and generates the rest of the poses using methods of the 'library' class
    - each sequence will randomly generate the category for the next sequence, taking into account what the current category is
    - there is a get_next method for each body position category which considers the current category, the next category, and where it is in the sequence before deciding the next pose
6. After the routine is built as a list of sequences, another method of the libray class _get_routine_timing is called, which is passed the routine and the user's length
7. _get_routine_timing builds an list of arrays, with each array holding 5 randomized integers which add up to 60.
8. The final routine is printed in a user-friendly way including the amount of time to hold each pose
   
 
