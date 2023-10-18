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

