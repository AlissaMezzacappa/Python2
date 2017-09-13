def confidence_interval(v1, N, C):
    """Compute confidence interval for number of values, v1, out of a total sample, N , with confidence, C"""
x_avg=v1/N
s=((v1(1-x_avg)^2+(0-x_avg)^2)/(N-1))^.5    #sample variance
sd=s/(N)^.5     #std of sampling dist / standard error
import scipy.stats as st
z=st.norm.ppf(C) # no. of std   #FYRI: C=st.norm.cdf(z)
int=z*sd
print( 'We are 99% confident that the population proportion, p=x_avg=',str(x_avg),'is within ',str(int),' of sample mean')