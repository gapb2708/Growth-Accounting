# Growth Accounting

In this repository we analyze the economic growth of 4 hypothetical countries.

First, we have a data set of the GDP per capita for each country. All countries start at the same level.

We define the average growth rate per capita for each country as:

$$r_i= ( \dfrac{GDP_{i,t=0}}{GDP_{i,T}}) ^{\dfrac{1}{i,t=0-i,T}} -1$$

Then, we define the tendency that each country should follow with their respective average growth rate:

$$Tendency_{i,t}=GDP_{t}( 1+r_{i,t}) $$

After doing this we take the logarithm of the GPD per capita and Tendency per capita of each country and substract them. The logarithmic difference is the cycle and is defined as:

$$cycle_{i,t}=\ln GDP_{i,t}-\ln Tendency_{i,t}

We calculate the average of the economic cycles for each country
