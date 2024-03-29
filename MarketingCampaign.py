'''
Marketing Campaign Success [Amazon Advanced] https://platform.stratascratch.com/coding/514-marketing-campaign-success-advanced?code_type=5

You have a table of in-app purchases by user. 
Users that make their first in-app purchase are placed in a marketing campaign where they see call-to-actions for more in-app purchases. 
Find the number of users that made additional in-app purchases due to the success of the marketing campaign.
The marketing campaign doesn't start until one day after the initial in-app purchase so users that only made one or multiple purchases on the first day do not count,
nor do we count users that over time purchase only the products they purchased on the first day.
'''
# Python Solution (SQL_Server is next)
import pandas as pd

df = marketing_campaign[['created_at', 'user_id']]
df['prev_date'] = df.groupby('user_id')['created_at'].shift(1)
df['purchase_day_rank'] = df.groupby('user_id')['created_at'].rank()
df['date_diff'] = (df['created_at'] - df['prev_date']).dt.days
df_final = df[(df['date_diff'] == 1) & (df['purchase_day_rank']==2)]

count = df_final.shape[0]
print(count)

# SQL Server Solution Main filtered table with items need:
with cte as (SELECT user_id, created_at,
	LAG(created_at,1) OVER ( PARTITION BY user_id ORDER BY created_at
	) as prev_day,
	ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY created_at) 
	AS purchase_number
FROM marketing_campaign),

users_second_day as (SELECT user_id
FROM cte
WHERE purchase_number = 2 
and datediff(day, created_at, prev_day) =-1
)

SELECT count(user_id) FROM users_second_day
;
