### Running the multivariate regression for all variables in the years 2013 - 2017

                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      W   R-squared:                       1.000
Model:                            OLS   Adj. R-squared:                  1.000
Method:                 Least Squares   F-statistic:                 6.611e+25
Date:                Fri, 23 Jun 2017   Prob (F-statistic):               0.00
Time:                        01:50:19   Log-Likelihood:                 3606.5
No. Observations:                 150   AIC:                            -7133.
Df Residuals:                     110   BIC:                            -7013.
Df Model:                          40                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Age         4.524e-13   7.31e-13      0.619      0.537   -9.96e-13     1.9e-12
W              0.3500   8.17e-12   4.29e+10      0.000       0.350       0.350
L             -0.1500   8.72e-12  -1.72e+10      0.000      -0.150      -0.150
PW             0.1000   1.96e-12    5.1e+10      0.000       0.100       0.100
PL             0.1000    1.9e-12   5.25e+10      0.000       0.100       0.100
MOV         8.242e-13   1.88e-10      0.004      0.997   -3.72e-10    3.73e-10
SOS         5.258e-12   1.89e-10      0.028      0.978   -3.69e-10     3.8e-10
SRS         9.962e-12   1.89e-10      0.053      0.958   -3.65e-10    3.85e-10
ORtg       -1.689e-11   1.21e-11     -1.394      0.166   -4.09e-11    7.12e-12
DRtg       -4.405e-12   1.06e-11     -0.417      0.678   -2.54e-11    1.65e-11
Pace        1.079e-11    1.1e-11      0.983      0.328    -1.1e-11    3.25e-11
FTr        -1.819e-12    1.8e-09     -0.001      0.999   -3.58e-09    3.57e-09
3PAr        1.023e-12   9.88e-10      0.001      0.999   -1.96e-09    1.96e-09
TS%         4.547e-12   2.36e-09      0.002      0.998   -4.68e-09    4.69e-09
Off eFG%   -6.821e-12   2.55e-09     -0.003      0.998   -5.06e-09    5.04e-09
Off TOV%     4.05e-13   2.48e-11      0.016      0.987   -4.87e-11    4.95e-11
Off ORB%    1.605e-11   5.74e-12      2.795      0.006    4.67e-12    2.74e-11
Off FT/FGA  1.455e-11   2.14e-09      0.007      0.995   -4.23e-09    4.26e-09
Def eFG%   -2.387e-12   7.24e-10     -0.003      0.997   -1.44e-09    1.43e-09
Def TOV%   -6.535e-12   6.36e-12     -1.027      0.307   -1.91e-11    6.08e-12
Def DRB%    1.005e-12   2.68e-12      0.376      0.708    -4.3e-12    6.31e-12
Def FT/FGA -2.274e-12   2.33e-10     -0.010      0.992   -4.64e-10     4.6e-10
G              0.2000   3.58e-12   5.59e+10      0.000       0.200       0.200
W.1            0.3500   8.17e-12   4.29e+10      0.000       0.350       0.350
L.1           -0.1500   8.72e-12  -1.72e+10      0.000      -0.150      -0.150
WIN%       -6.366e-12   2.71e-09     -0.002      0.998   -5.38e-09    5.36e-09
MP          6.449e-14    5.4e-14      1.194      0.235   -4.26e-14    1.72e-13
FG           1.47e-13   1.15e-13      1.282      0.203   -8.03e-14    3.74e-13
FGA         3.352e-13   1.04e-13      3.229      0.002    1.29e-13    5.41e-13
FG%        -7.276e-12   2.72e-09     -0.003      0.998   -5.39e-09    5.37e-09
3P         -1.252e-13   1.16e-13     -1.078      0.283   -3.55e-13    1.05e-13
3PA        -5.489e-13   1.22e-13     -4.495      0.000   -7.91e-13   -3.07e-13
3P%         1.137e-13   3.16e-10      0.000      1.000   -6.25e-10    6.26e-10
2P         -1.714e-13    1.3e-13     -1.316      0.191    -4.3e-13    8.68e-14
2PA        -5.495e-13   7.78e-14     -7.063      0.000   -7.04e-13   -3.95e-13
2P%         6.708e-12   6.66e-10      0.010      0.992   -1.31e-09    1.33e-09
FT          8.993e-15   3.11e-13      0.029      0.977   -6.07e-13    6.25e-13
FTA        -1.128e-13   2.98e-13     -0.379      0.705   -7.03e-13    4.77e-13
FT%         1.805e-12   2.97e-10      0.006      0.995   -5.87e-10     5.9e-10
ORB        -2.393e-13    8.4e-14     -2.847      0.005   -4.06e-13   -7.27e-14
DRB        -2.555e-13   5.11e-14     -5.000      0.000   -3.57e-13   -1.54e-13
TRB          1.35e-13   4.06e-14      3.326      0.001    5.46e-14    2.15e-13
AST        -2.172e-14   1.07e-14     -2.036      0.044   -4.28e-14   -5.83e-16
STL         9.021e-16   3.59e-14      0.025      0.980   -7.02e-14     7.2e-14
BLK        -3.678e-14    2.1e-14     -1.754      0.082   -7.83e-14    4.77e-15
TOV        -3.285e-13   2.68e-13     -1.228      0.222   -8.59e-13    2.02e-13
PF         -1.622e-14   2.61e-14     -0.622      0.535   -6.79e-14    3.55e-14
PTS          1.86e-13   1.12e-13      1.654      0.101   -3.68e-14    4.09e-13
==============================================================================
Omnibus:                        0.710   Durbin-Watson:                   2.029
Prob(Omnibus):                  0.701   Jarque-Bera (JB):                0.813
Skew:                          -0.071   Prob(JB):                        0.666
Kurtosis:                       2.669   Cond. No.                     1.00e+16
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 8.76e-22. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.

### The VIFs are enormous! 

[547.08140904759125, inf, inf, inf, inf, 1103997.9392964593, 9460.0846325117345, 1070484.6251542657, 
 2403283.3370706425, 1827546.3472287781, 1544720.8582422109, 358439.50962472218, 109165.06991046559, 
 2347691.1948015643, 2356674.1173225571, 156276.56747070106, 29603.321120974528, 290576.4604219821, 
 189869.27643212632, 10338.745653194004, 58135.498153276785, 3427.2404515029007, inf, inf, inf, 
 2887804.7819686295, 1648455.777616126, inf, inf, 2179355.562842322, inf, inf, 18101.756544083571, 
 inf, inf, 153557.92563108518, inf, 458231.35447415133, 72989.52603473136, inf, inf, inf, 
 546.04223362418509, 755.95470136963445, 103.21615113277581, 143763.43669050193, 2692.6167686943186, inf]

### Narrow down the variables into: 
    ['Off ORB%', 'FGA', '3PA', '2PA', 'ORB', 'DRB', 'TRB', 'AST']

                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      W   R-squared:                       0.963
Model:                            OLS   Adj. R-squared:                  0.962
Method:                 Least Squares   F-statistic:                     631.0
Date:                Fri, 23 Jun 2017   Prob (F-statistic):          1.01e-100
Time:                        02:00:03   Log-Likelihood:                -528.67
No. Observations:                 150   AIC:                             1069.
Df Residuals:                     144   BIC:                             1087.
Df Model:                           6                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Off ORB%       5.2808      0.782      6.756      0.000       3.736       6.826
FGA           -0.0111      0.002     -4.734      0.000      -0.016      -0.006
3PA           -0.0005      0.002     -0.270      0.787      -0.004       0.003
2PA           -0.0106      0.001     -7.493      0.000      -0.013      -0.008
ORB           -0.0892      0.015     -5.912      0.000      -0.119      -0.059
DRB            0.0627      0.008      8.354      0.000       0.048       0.078
TRB           -0.0266      0.009     -3.008      0.003      -0.044      -0.009
AST            0.0251      0.005      4.602      0.000       0.014       0.036
==============================================================================
Omnibus:                        1.019   Durbin-Watson:                   2.190
Prob(Omnibus):                  0.601   Jarque-Bera (JB):                1.098
Skew:                          -0.188   Prob(JB):                        0.577
Kurtosis:                       2.815   Cond. No.                     3.57e+17
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 1.17e-25. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.


### Will the structure coefficient indicate any significance for the 3PA? 
### Is the league actually transitioning to 3PAs? If yes, for 2016 and 2017, the significance of the 3PA should increase. 
### The VIFs are still enormous!

[547.08140904759125, inf, inf, inf, inf, 1103997.9392964593, 9460.0846325117345, 1070484.6251542657, 
 2403283.3370706425, 1827546.3472287781, 1544720.8582422109, 358439.50962472218, 109165.06991046559, 
 2347691.1948015643, 2356674.1173225571, 156276.56747070106, 29603.321120974528, 290576.4604219821, 
 189869.27643212632, 10338.745653194004, 58135.498153276785, 3427.2404515029007, inf, inf, inf, 
 2887804.7819686295, 1648455.777616126, inf, inf, 2179355.562842322, inf, inf, 18101.756544083571, 
 inf, inf, 153557.92563108518, inf, 458231.35447415133, 72989.52603473136, inf, inf, inf, 
 546.04223362418509, 755.95470136963445, 103.21615113277581, 143763.43669050193, 2692.6167686943186, inf]

### Calculate the structure coefficients

             Y-Hat  Off ORB%
Y-Hat     1.000000 -0.050229
Off ORB% -0.050229  1.000000
          Y-Hat       FGA
Y-Hat  1.000000 -0.330891
FGA   -0.330891  1.000000
         Y-Hat      3PA
Y-Hat  1.00000  0.32032
3PA    0.32032  1.00000
          Y-Hat       2PA
Y-Hat  1.000000 -0.537071
2PA   -0.537071  1.000000
          Y-Hat       ORB
Y-Hat  1.000000 -0.287629
ORB   -0.287629  1.000000
          Y-Hat       DRB
Y-Hat  1.000000  0.402271
DRB    0.402271  1.000000
          Y-Hat       TRB
Y-Hat  1.000000  0.159225
TRB    0.159225  1.000000
          Y-Hat       AST
Y-Hat  1.000000  0.510356
AST    0.510356  1.000000


    strcoef  strcoef^2     x-var
0 -0.050229   0.002523  Off ORB%
1 -0.330891   0.109489       FGA
2  0.320320   0.102605       3PA
3 -0.537071   0.288445       2PA
4 -0.287629   0.082730       ORB
5  0.402271   0.161822       DRB
6  0.159225   0.025353       TRB
7  0.510356   0.260463       AST


### Code that was used: 

        ### Set everything up and convert everything into a number
        year = 'total'
        print('\n' + year)
        df = makeframe(str(dir_path + '/league all stats/' + year + '.csv'))
        df1 = df.drop('Team', axis=1)
        df1 = df1.convert_objects(convert_numeric=True)
        y = df[['W']] 
        
        xvar = ['Off ORB%', 'FGA', '3PA', '2PA', 'ORB', 'DRB', 'TRB', 'AST']
        x1 = df1[xvar]
        
        # Run the Regression
        result = sm.OLS(y, x1).fit()
        print(result.summary())
        
        
        #Calculate the VIF
        #vif = [variance_inflation_factor(x.values, i) for i in range(x.shape[1])]
        #print(vif)
        
        
        df1['Beta*Off ORB%'] = 5.2808 * df1[['Off ORB%']]
        df1['Beta*FGA'] = -0.0111 * df1[['FGA']]
        df1['Beta*3PA'] = -0.0005 * df1[['3PA']]
        df1['Beta*2PA'] = -0.0106 * df1[['2PA']]
        df1['Beta*ORB'] = -0.0892 * df1[['ORB']]
        df1['Beta*DRB'] = 0.0627 * df1[['DRB']]
        df1['Beta*TRB'] = -0.0266 * df1[['TRB']]
        df1['Beta*AST'] = 0.0251 * df1[['AST']]
        
        df1['Y-Hat'] = (
                df1['Beta*Off ORB%'] +
                df1['Beta*FGA'] + 
                df1['Beta*3PA'] + 
                df1['Beta*2PA'] +
                df1['Beta*ORB'] +
                df1['Beta*DRB'] +
                df1['Beta*TRB'] +
                df1['Beta*AST']
                )
        
        # Run correlation between y-hat and prediction variables
        for x in xvar: 
            a = df1[['Y-Hat', x]].corr()    
            print(a)
        
        b = [-0.050229,         #Off ORB%
             -0.330891,         #FGA
             0.32032,           #3PA
             -0.537071,         #2PA
             -0.287629,         #ORB
             0.402271,          #DRB
             0.159225,          #TRB
             0.510356,          #AST
             ]
        
        c = []
        for b1 in b: 
            c.append(b1 * b1)
        
        corr = pd.DataFrame(
            {'x-var': xvar,
             'strcoef': b,
             'strcoef^2': c
            })
        
        print('\n')
        print(corr)

### 3PA suddenly becomes significant. 
### Get rid of Off ORB%, because structure coefficient-squared was so low 

                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      W   R-squared:                       0.952
Model:                            OLS   Adj. R-squared:                  0.950
Method:                 Least Squares   F-statistic:                     572.0
Date:                Fri, 23 Jun 2017   Prob (F-statistic):           1.59e-93
Time:                        02:32:50   Log-Likelihood:                -549.32
No. Observations:                 150   AIC:                             1109.
Df Residuals:                     145   BIC:                             1124.
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
FGA           -0.0175      0.002     -7.148      0.000      -0.022      -0.013
3PA           -0.0056      0.002     -3.011      0.003      -0.009      -0.002
2PA           -0.0119      0.002     -7.428      0.000      -0.015      -0.009
ORB            0.0061      0.006      0.995      0.321      -0.006       0.018
DRB            0.0212      0.005      4.298      0.000       0.011       0.031
TRB            0.0273      0.004      6.298      0.000       0.019       0.036
AST            0.0401      0.006      7.049      0.000       0.029       0.051
==============================================================================
Omnibus:                        0.393   Durbin-Watson:                   1.922
Prob(Omnibus):                  0.822   Jarque-Bera (JB):                0.218
Skew:                           0.089   Prob(JB):                        0.897
Kurtosis:                       3.059   Cond. No.                     2.98e+17
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 1.67e-25. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.

          Y-Hat       FGA
Y-Hat  1.000000  0.044136
FGA    0.044136  1.000000
          Y-Hat       3PA
Y-Hat  1.000000  0.409152
3PA    0.409152  1.000000
          Y-Hat       2PA
Y-Hat  1.000000 -0.405865
2PA   -0.405865  1.000000
          Y-Hat       ORB
Y-Hat  1.000000 -0.208001
ORB   -0.208001  1.000000
          Y-Hat       DRB
Y-Hat  1.000000  0.672396
DRB    0.672396  1.000000
          Y-Hat       TRB
Y-Hat  1.000000  0.448763
TRB    0.448763  1.000000
          Y-Hat       AST
Y-Hat  1.000000  0.695643
AST    0.695643  1.000000


    strcoef  strcoef^2 x-var
0  0.044136   0.001948   FGA
1  0.409152   0.167405   3PA
2 -0.405865   0.164726   2PA
3 -0.208001   0.043264   ORB
4  0.672396   0.452116   DRB
5  0.448763   0.201388   TRB
6  0.695643   0.483919   AST

### Choose to remove ORB or FGA? 
### ORB is deemed insigificant by the P>|t|
### FGA explains very little of the R-squared

                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      W   R-squared:                       0.952
Model:                            OLS   Adj. R-squared:                  0.950
Method:                 Least Squares   F-statistic:                     572.0
Date:                Fri, 23 Jun 2017   Prob (F-statistic):           1.59e-93
Time:                        02:37:24   Log-Likelihood:                -549.32
No. Observations:                 150   AIC:                             1109.
Df Residuals:                     145   BIC:                             1124.
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
3PA           -0.0231      0.004     -5.716      0.000      -0.031      -0.015
2PA           -0.0295      0.004     -7.952      0.000      -0.037      -0.022
ORB            0.0061      0.006      0.995      0.321      -0.006       0.018
DRB            0.0212      0.005      4.298      0.000       0.011       0.031
TRB            0.0273      0.004      6.298      0.000       0.019       0.036
AST            0.0401      0.006      7.049      0.000       0.029       0.051
==============================================================================
Omnibus:                        0.393   Durbin-Watson:                   1.922
Prob(Omnibus):                  0.822   Jarque-Bera (JB):                0.218
Skew:                           0.089   Prob(JB):                        0.897
Kurtosis:                       3.059   Cond. No.                     2.92e+16
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 9.12e-24. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
         Y-Hat      3PA
Y-Hat  1.00000  0.41181
3PA    0.41181  1.00000
          Y-Hat       2PA
Y-Hat  1.000000 -0.409204
2PA   -0.409204  1.000000
          Y-Hat       ORB
Y-Hat  1.000000 -0.209466
ORB   -0.209466  1.000000
          Y-Hat       DRB
Y-Hat  1.000000  0.672004
DRB    0.672004  1.000000
          Y-Hat       TRB
Y-Hat  1.000000  0.447439
TRB    0.447439  1.000000
          Y-Hat       AST
Y-Hat  1.000000  0.695002
AST    0.695002  1.000000


    strcoef  strcoef^2 x-var
0  0.411810   0.169587   3PA
1 -0.409204   0.167448   2PA
2 -0.209466   0.043876   ORB
3  0.672004   0.451589   DRB
4  0.447439   0.200202   TRB
5  0.695002   0.483028   AST

### Above: Getting rid of FGA; ORB is still insigificant and accounts for a tiny part of R-squared. 

                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      W   R-squared:                       0.952
Model:                            OLS   Adj. R-squared:                  0.950
Method:                 Least Squares   F-statistic:                     572.0
Date:                Fri, 23 Jun 2017   Prob (F-statistic):           1.59e-93
Time:                        02:39:50   Log-Likelihood:                -549.32
No. Observations:                 150   AIC:                             1109.
Df Residuals:                     145   BIC:                             1124.
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
FGA           -0.0175      0.002     -7.148      0.000      -0.022      -0.013
3PA           -0.0056      0.002     -3.011      0.003      -0.009      -0.002
2PA           -0.0119      0.002     -7.428      0.000      -0.015      -0.009
DRB            0.0151      0.010      1.476      0.142      -0.005       0.035
TRB            0.0334      0.009      3.556      0.001       0.015       0.052
AST            0.0401      0.006      7.049      0.000       0.029       0.051
==============================================================================
Omnibus:                        0.393   Durbin-Watson:                   1.922
Prob(Omnibus):                  0.822   Jarque-Bera (JB):                0.218
Skew:                           0.089   Prob(JB):                        0.897
Kurtosis:                       3.059   Cond. No.                     8.33e+15
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 2.13e-22. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
          Y-Hat       FGA
Y-Hat  1.000000  0.044136
FGA    0.044136  1.000000
          Y-Hat       3PA
Y-Hat  1.000000  0.409152
3PA    0.409152  1.000000
          Y-Hat       2PA
Y-Hat  1.000000 -0.405865
2PA   -0.405865  1.000000
          Y-Hat       DRB
Y-Hat  1.000000  0.672396
DRB    0.672396  1.000000
          Y-Hat       TRB
Y-Hat  1.000000  0.448763
TRB    0.448763  1.000000
          Y-Hat       AST
Y-Hat  1.000000  0.695643
AST    0.695643  1.000000


    strcoef  strcoef^2 x-var
0  0.044136   0.001948   FGA
1  0.409152   0.167405   3PA
2 -0.405865   0.164726   2PA
3  0.672396   0.452116   DRB
4  0.448763   0.201388   TRB
5  0.695643   0.483919   AST

### Above: Getting rid of ORB; FGA is very insigificant according to the strcoef^2
### From experience, DRB and TRB are multicollinear; but why does DRB account for 0.45 of the R-squared? 
### Try removing DRB. See if FGA improves or not


                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      W   R-squared:                       0.951
Model:                            OLS   Adj. R-squared:                  0.950
Method:                 Least Squares   F-statistic:                     708.7
Date:                Fri, 23 Jun 2017   Prob (F-statistic):           1.65e-94
Time:                        02:43:05   Log-Likelihood:                -550.44
No. Observations:                 150   AIC:                             1109.
Df Residuals:                     146   BIC:                             1121.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
FGA           -0.0175      0.002     -7.108      0.000      -0.022      -0.013
3PA           -0.0049      0.002     -2.702      0.008      -0.008      -0.001
2PA           -0.0126      0.002     -8.226      0.000      -0.016      -0.010
TRB            0.0438      0.006      7.021      0.000       0.031       0.056
AST            0.0430      0.005      8.056      0.000       0.032       0.054
==============================================================================
Omnibus:                        0.339   Durbin-Watson:                   1.935
Prob(Omnibus):                  0.844   Jarque-Bera (JB):                0.281
Skew:                           0.105   Prob(JB):                        0.869
Kurtosis:                       2.972   Cond. No.                     8.07e+15
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The smallest eigenvalue is 2.1e-22. This might indicate that there are
strong multicollinearity problems or that the design matrix is singular.
          Y-Hat       FGA
Y-Hat  1.000000  0.062236
FGA    0.062236  1.000000
          Y-Hat       3PA
Y-Hat  1.000000  0.412553
3PA    0.412553  1.000000
          Y-Hat       2PA
Y-Hat  1.000000 -0.398597
2PA   -0.398597  1.000000
          Y-Hat       TRB
Y-Hat  1.000000  0.464919
TRB    0.464919  1.000000
          Y-Hat       AST
Y-Hat  1.000000  0.706182
AST    0.706182  1.000000


    strcoef  strcoef^2 x-var
0 -0.078524   0.006166   FGA
1  0.356653   0.127201   3PA
2 -0.424004   0.179779   2PA
3  0.314951   0.099194   TRB
4  0.731561   0.535181   AST

### FGA still does not improve. Remove FGA. This makes sense, because a FGA is essentially a 2PA or a 3PA

                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      W   R-squared:                       0.951
Model:                            OLS   Adj. R-squared:                  0.950
Method:                 Least Squares   F-statistic:                     708.7
Date:                Fri, 23 Jun 2017   Prob (F-statistic):           1.65e-94
Time:                        02:45:53   Log-Likelihood:                -550.44
No. Observations:                 150   AIC:                             1109.
Df Residuals:                     146   BIC:                             1121.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
3PA           -0.0224      0.004     -5.550      0.000      -0.030      -0.014
2PA           -0.0302      0.004     -8.170      0.000      -0.037      -0.023
TRB            0.0438      0.006      7.021      0.000       0.031       0.056
AST            0.0430      0.005      8.056      0.000       0.032       0.054
==============================================================================
Omnibus:                        0.339   Durbin-Watson:                   1.935
Prob(Omnibus):                  0.844   Jarque-Bera (JB):                0.281
Skew:                           0.105   Prob(JB):                        0.869
Kurtosis:                       2.972   Cond. No.                         69.2
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
          Y-Hat       3PA
Y-Hat  1.000000  0.415238
3PA    0.415238  1.000000
          Y-Hat       2PA
Y-Hat  1.000000 -0.401985
2PA   -0.401985  1.000000
          Y-Hat       TRB
Y-Hat  1.000000  0.463572
TRB    0.463572  1.000000
         Y-Hat      AST
Y-Hat  1.00000  0.70554
AST    0.70554  1.00000


    strcoef  strcoef^2 x-var
0  0.415238   0.172423   3PA
1 -0.401985   0.161592   2PA
2  0.463572   0.214899   TRB
3  0.705540   0.497787   AST

### It looks like the variables that influence wins are: 
    3PA, 2PA, TRB, AST
    
### Try breaking down TRB into ORB and DRB. See how they contribute. 
    
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      W   R-squared:                       0.952
Model:                            OLS   Adj. R-squared:                  0.950
Method:                 Least Squares   F-statistic:                     572.0
Date:                Fri, 23 Jun 2017   Prob (F-statistic):           1.59e-93
Time:                        02:49:20   Log-Likelihood:                -549.32
No. Observations:                 150   AIC:                             1109.
Df Residuals:                     145   BIC:                             1124.
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
3PA           -0.0231      0.004     -5.716      0.000      -0.031      -0.015
2PA           -0.0295      0.004     -7.952      0.000      -0.037      -0.022
ORB            0.0334      0.009      3.556      0.001       0.015       0.052
DRB            0.0485      0.007      6.943      0.000       0.035       0.062
AST            0.0401      0.006      7.049      0.000       0.029       0.051
==============================================================================
Omnibus:                        0.393   Durbin-Watson:                   1.922
Prob(Omnibus):                  0.822   Jarque-Bera (JB):                0.218
Skew:                           0.089   Prob(JB):                        0.897
Kurtosis:                       3.059   Cond. No.                         86.5
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
         Y-Hat      3PA
Y-Hat  1.00000  0.41181
3PA    0.41181  1.00000
          Y-Hat       2PA
Y-Hat  1.000000 -0.409204
2PA   -0.409204  1.000000
          Y-Hat       ORB
Y-Hat  1.000000 -0.209466
ORB   -0.209466  1.000000
          Y-Hat       DRB
Y-Hat  1.000000  0.672004
DRB    0.672004  1.000000
          Y-Hat       AST
Y-Hat  1.000000  0.695002
AST    0.695002  1.000000


    strcoef  strcoef^2 x-var
0  0.411810   0.169587   3PA
1 -0.409204   0.167448   2PA
2 -0.209466   0.043876   ORB
3  0.672004   0.451589   DRB
4  0.695002   0.483028   AST

### Averaging the strcoef^2 for ORB and DRB produces the strcoef^2 for TRB (total rebounds)
### However, as seen from the strcoef^2, it appears that defensive* rebounds contribute to more wins. 
### The regression model doesn't explicity state that, despite the fact that the coefficient is indeed a bit greater. 


### Lets try to add predictive elements to the model. 
ORtg,DRtg,Pace,TS%,FG%,3P%,2P%,TRB,AST,TOV,PTS


