"""Slicing time series
Slicing is particularly useful for time series, since it's a common thing to want to filter for data within a date range. Add the date column to the index, then use .loc[] to perform the subsetting. The important thing to remember is to keep your dates in ISO 8601 format, that is, yyyy-mm-dd.

Recall from Chapter 1 that you can combine multiple Boolean conditions using logical operators (such as &). To do so in one line of code you'll need to add parentheses () around each condition.

pandas is loaded as pd and temperatures, with no index, is available.

Instructions
100 XP
Use Boolean conditions to subset for rows in 2010 and 2011, and print the results.
Set the index to the date column.
Use .loc[] to subset for rows in 2010 and 2011.
Use .loc[] to subset for rows from Aug 2010 to Feb 2011.
"""
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
print(temperatures[(temperatures["date"] >= "2010") & (temperatures["date"] < "2012")])

# Set date as an index
temperatures_ind = temperatures.set_index("date")

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08":"2011-02"])