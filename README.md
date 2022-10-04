# Growth Accounting

In this repository we analyze the economic growth Accounting for hypothetical countries.

First, we have a data set of the GDP per capita for each country. All countries start at the same level.

We define the average growth rate per capita for each country as:

$$r_i= ( \dfrac{GDP_{i,t=0}}{GDP_{i,T}}) ^{\dfrac{1}{i,t=0-i,T}} -1$$

Then, we define the tendency that each country should follow with their respective average growth rate:

$$Tendency_{i,t}=GDP_{i,t}( 1+r_{i}) $$

After doing this we take the logarithm of the GPD per capita and Tendency per capita of each country and substract them. The logarithmic difference is the cycle and is defined as:

$$cycle_{i,t}=\ln GDP_{i,t}-\ln Tendency_{i,t}$$

We calculate the average of the economic cycles for each country.

For the second part: We have a dataset for 2 countries with their Labor (L), Wages(W), Capital (K), and GDP (Y) for each year $t$.

We suppose that all economies follow a typical Cobb-Douglas production function:

$$Y=AK_t^{\alpha }L_t^{\alpha -1}$$

We calculate the share of production ($\alpha$) as:

$$\alpha =1-\dfrac{W_tL_t}{Y_t}$$

With this we can know compute the TPF as a Solow Residual:

$$A=\dfrac{Y_t}{K_t^{\alpha}L_t^{1-\alpha}}$$

We take the logarithm for each parameter: K, L, A, Y. And proceed to compute the logarithmic difference ($\Delta$) for $t-1$ and $t$

With this $\Delta$ we take the average for the first 25 years and the last 25 years for each variable

Finally, We define the contribution of each variable to the GDP growth for the first and last 25 years as

$$\gamma variable_{2,25}=\dfrac{\sum_{t=2}^{25} \alpha\overline{\Delta}variable}{\sum_{t=2}^{25} \overline{\Delta}Y}$$

and:

$$\gamma variable_{26,50}=\dfrac{\sum_{t=26}^{50} \alpha\overline{\Delta}variable}{\sum_{t=26}^{50} \overline{\Delta}Y}$$
