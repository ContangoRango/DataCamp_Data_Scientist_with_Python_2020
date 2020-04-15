"""====================MCQ================="""
# Joining by Index
# The DataFrames revenue and managers are displayed in the IPython Shell. Here, they are indexed by 'branch_id'.

# Choose the function call below that will join the DataFrames on their indexes and return 5 rows with index labels [10, 20, 30, 31, 47]. Explore each of them in the IPython Shell to get a better understanding of their functionality.

# Instructions
# 50 XP
# Possible Answers
# pd.merge(revenue, managers, on='branch_id').
# pd.merge(managers, revenue, how='left').
# revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer').
# managers.join(revenue, lsuffix='_mgn', rsuffix='_rev', how='left')

"""ANSWER
revenue.join(managers, lsuffix='_rev', rsuffix='_mng', how='outer').
"""
                    """DEVELOPER"""
                """BasitAminBhatti"""
                    """Github""""
        """https://github.com/basitaminbhatti"""