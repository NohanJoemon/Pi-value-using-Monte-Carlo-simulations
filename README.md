# Estimation of Pi using Monte-Carlo simulation
![image](https://user-images.githubusercontent.com/62956111/174017674-1ccdffd7-b7c4-48f8-bde3-6e805adbb0fb.png)

<br><br>
 This project is an illustration of finding the value of pi using Monte-Carlo simulation. Monte-Carlo simulation relies on repeated random sampling to obtain numerical results. In this case, we consider all points (x,y) that lie in the square marked by (-1,-1),(-1,1),(1,-1) and (1,1). Now. consider the unit circle centred at the origin. If we consider a random point inside the square, the probability that it lies inside the circle is given by π r2 / a2. Here, a=2 and r=1, hence the probability is π/4. To simulate this probability, we consider a large number of points inside the square and find the fraction of points that lie within the circle. This fraction is multiplied with 4 to give an estimate for pi. The accuracy of the estimate increases as we consider more points

