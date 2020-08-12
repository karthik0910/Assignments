
Problem Statement 1:
    
    
    
Is gender independent of education level? A random sample of 395 people were
surveyed and each person was asked to report the highest education level they
obtained. The data that resulted from the survey is summarized in the following table:
    
    
High School Bachelors Masters Ph.d. Total

Female 60 54 46 41 201

Male 40 44 53 57 194

Total 100 98 99 98 395



Question: Are gender and education level dependent at 5% level of significance? In
other words, given the data collected above, is there a relationship between the
gender of an individual and the level of education that they have obtained?
H0:  Gender and Education level are independent
H1:  Gender and Education level are dependent at 0.05
    
    
            High School Bachelors Masters   Ph.d.       Total

    Female     60         54        46       41           201

     Male      40         44        53       57           194

    Total     100         98        99       98           395
    
    




Expected values

          High School    Bachelors    Masters     Ph.d.       

  Female       50.8        49.86        50.3       49.86
  

  Male          49.1         48.1       48.6      48.1

                                          
    chi-square statistic  = 8.006
    
    
degrees of freedom = (4-1)*(2-1) = 3

critical value at df =3 is  7.815 ;  chi-square statistic>critical value 


Hence there is enough evidence to reject null hypothesis. Therefore we can say that there a relationship between the gender of an individual and the level of education.
Problem Statement 2:
    
    
Using the following data, perform a oneway analysis of variance using α=.05. Write
up the results in APA format.


[Group1: 51, 45, 33, 45, 67]

[Group2: 23, 43, 23, 43, 45]

[Group3: 56, 76, 74, 87, 56]
grand mean  = 48.2+35.4+69.8/3 = 51.1

Between Group Variability (SST) = 5*(48.2-51.1)^2+5*(35.4-51.1)^2+5*(69.8-51.1)^2 = 604.58

MeanSSbetween(MSST) = 604.58/(3-1) = 302.29

Within Group Variability (SSE) = 1511.45

Degree of Freedom for within variability= 15-3 = 12

MeanSSwithin(MSSE) = 1511.45/12 = 125.954


F-statistics = MSST/MSSE  = 302.29/125.954 = 2.4

At 5% significance and degree of freedom (2,12) critical F value = 3.89

critical F value > F-statistics

Reject Null Hypothesis
Problem Statement 3:
    
    
Calculate F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25.

For 10, 20, 30, 40, 50:
    
    


```python
import numpy as np
from scipy import stats

H0: the population variances are equal
H1: the population variances are not equal 

x = [10,20,30,40,50]
y=  [5,10,15,20,25]



def f_test(x, y):
    x = np.array(x)
    y = np.array(y)
    f = np.var(x, ddof=1)/np.var(y, ddof=1) #calculate F test statistic 
    dfn = x.size-1 #define degrees of freedom numerator 
    dfd = y.size-1 #define degrees of freedom denominator 
    p = 1-stats.f.cdf(f, dfn, dfd) #find p-value of F test statistic 
    return f, p

f_test(x, y)

Since this p-value>0.05, we accept the null hypothesis. This means we have sufficient evidence to say that the two population variances are  equal.
```




    (4.0, 0.10399999999999998)




```python

```
