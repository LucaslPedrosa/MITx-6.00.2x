# Suppose you are given the following data and are asked to fit a curve to this data.

A = [1,2,3,4,5,6,7,8,9,10]
L = [0.59,18.38, 33.01, 54.14, 72.48, 89.8, 97.07, 112.6, 142.87, 199.84]

# ==============================================================================
# REFERENCE: image_48ecc0.png
# ==============================================================================

# --- QUESTION 1: Match plots with polynomial fits ---

# Fit 1: [ / ] Linear
# --------------------------------------------------
# Description: A straight line (Degree 1). 
# It follows the general upward slope but misses the curvature of the points.

# Fit 2: [ J ] Polynomial of degree 2
# --------------------------------------------------
# Description: A smooth quadratic curve. 
# Better fit for the data's natural acceleration/bend.

# Fit 3: [ ~ ] Polynomial of degree 5
# --------------------------------------------------
# Description: High-frequency oscillations. 
# The line snakes through every individual point.


# --- QUESTION 2: Is each fit an example of overfitting? ---

# Fit 1: Overfitting? NO
# Reason: Simple model, high bias but low variance. 
# It doesn't try to "hug" the noise in the data.

# Fit 2: Overfitting? NO
# Reason: Balanced model. 
# Captures the non-linear trend without reacting to specific outliers.

# Fit 3: Overfitting? YES
# Reason: The model is too complex (Degree 5). 
# It's memorizing the noise in image_48ecc0.png instead of learning the pattern.
