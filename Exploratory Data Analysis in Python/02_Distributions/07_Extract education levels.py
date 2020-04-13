"""
Extract education levels
Let's create Boolean Series to identify respondents with different levels of education.

In the U.S, 12 years of education usually means the respondent has completed high school (secondary education). A respondent with 14 years of education has probably completed an associate degree (two years of college); someone with 16 years has probably completed a bachelor's degree (four years of college).

Instructions
100 XP
Complete the line that identifies respondents with associate degrees, that is, people with 14 or more years of education but less than 16.
Complete the line that identifies respondents with 12 or fewer years of education.
Confirm that the mean of high is the fraction we computed in the previous exercise, about 53%."""
# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = (educ >= 14) & (educ < 16)

# High school
high = (educ <= 12)
print(high.mean())