# Recall from the previous video the concept of the coefficient of
# determination, also known as the  value. This is computed by 1 -
# ((var_of_errors^2)/(var_of_data^2)). The variability of the errors is
# computed by taking the sum of the squares of (observed - predicted) errors.
# We normalize this variablity by dividing it by the variability of the data,
# which is sum of the squares of (observation - average_observation) for each
# observation.
#
# In this file, this  value is computed by the function rSquare.
#
# In that file, revise fitData and fitData3 to report the coefficient of
# determination for the fitted line in each case. Did this measure of the
# "goodness of fit" improve when we eliminated the measurements after the
# spring reached its elastic limit and Hooke's Law no longer applied?
#
# Ans: Yes, the R^2 value improved after eliminating the measurements after the
# spring reached its elastic limit, indicating a better fit of the data to the
# model.
#
# reasoning: The R^2 value is a measure of how well the model fits the data.
# When we eliminated the measurements after the spring reached its elastic
# limit, we removed data points that did not follow Hooke's Law, which likely
# had a significant impact on the variability of the errors. By removing these
# outliers, the model was able to fit the remaining data more accurately,
# resulting in an improved R^2 value.
