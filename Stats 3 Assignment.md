
Problem Statement 1:
    
    
Blood glucose levels for obese patients have a mean of 100 with a standard deviation of 15. A researcher thinks that a diet high in raw cornstarch will have a positive effect on
blood glucose levels. A sample of 36 patients who have tried the raw cornstarch diet
have a mean glucose level of 108. Test the hypothesis that the raw cornstarch had an
effect or not.
Solution:

H0:  raw cornstarch will not have a effect on blood glucose levels
    
H1: raw cornstarch will have a effect on blood glucose levels ; at α = 0.05
    
    
    
z-test = ((108-100)/(15/(36)^0.5)) = 3.2


z(α = 0.05) = 1.64


z(α = 0.05) < z-test. The test statistic value is greater than critical value. So we reject null hypothesis. Therefore we can say that raw cornstarch will have a effect on blood glucose levels.


Problem Statement 2:
    
    
    
In one state, 52% of the voters are Republicans, and 48% are Democrats. In a second
state, 47% of the voters are Republicans, and 53% are Democrats. Suppose a simple
random sample of 100 voters are surveyed from each state.
What is the probability that the survey will show a greater percentage of Republican
voters in the second state than in the first state?
p1 = proportions of voters are Republicans in state one
p2 = proportions of voters are Republicans in state two


p1 = 0.52
p2 = 0.47


n1P1 = 100 * 0.52 = 52

n1(1 - P1) = 100 * 0.48 = 48

n2P2 = 100 * 0.47 = 47

n2(1 - P2) = 100 * 0.53 = 53


The above four are each greater than 10, the sample size is large enough. Hence we use Z test

mean of the difference in sample proportions: E(p1 - p2) = P1 - P2 = 0.52 - 0.47 = 0.05.

standard deviation of the difference = ([ P1(1 - P1) / n1 ] + [ P2(1 - P2) / n2 ])^2 = 0.0706

z = (0-0.05)/0.0706 = -0.7082

p(x<-0.7082) = 0.24


The probability that the survey will show a greater percentage of Republican voters in the second state than in the first state = 0.24

Problem Statement 3:
    
You take the SAT and score 1100. The mean score for the SAT is 1026 and the standard
deviation is 209. How well did you score on the test compared to the average test taker?
x = 1100

mean = 1026

sd = 209

z = (1100-1026)/209 = 0.354 


prob(x<=0.354) = 0.6368 = 63.68% this states 63% of test takers scored below you.






```python

```
