slope,intercept,r,p,std_err=std_err.linregress(years , profit)
print("slope",slope , "intercept",intercept , "r",r , "p",p , "std_err",std_err)
def futurerevpro(years):
    return slope*years+intercept
print(futurerevpro(2025))
