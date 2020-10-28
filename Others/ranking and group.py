import pandas as pd
import datetime

left_team =pd.DataFrame({
             'rank':  [1,2,3,4,5,6,7,8],
              'team':  [
                       'England','India','NewZealand','SouthAfrica',
                       'Pakistan','Australia', 'Bangladesh', 'SriLanka'
                      ],
              'rating':['126','121','112','111','102','100','93','79']
            })

right_team =pd.DataFrame({
              'rank':[1,2,3,4,5,6,7,8],
              'team': [ 
                        'India','England','SouthAfrica','NewZealand',
                         'Australia', 'SriLanka', 'Pakistan','WestIndies'
                       ],
              'rating':['126','121','112','111','102','100','93','79']
             })
outer_join_result=left_team.merge(right_team, left_on='team', right_on='team', how='outer')
print(outer_join_result)

right_join_result=left_team.merge(right_team, left_on='team', right_on='team', how='right')
print(right_join_result)

iner_join_result=left_team.merge(right_team, left_on='team', right_on='team', how='inner')
print(iner_join_result)

left_join_result=left_team.merge(right_team, left_on='team', right_on='team', how='left')
print(left_join_result)