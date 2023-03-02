##A/B Testing for ShoeFly.com
##Our favorite online shoe store, ShoeFly.com is performing an A/B Test. 
##They have two different versions of an ad, which they have placed in emails, as well as in banner ads on Facebook, Twitter, and Google. They want to know how the two ads are performing on each of the different platforms on each day of the week. Help them analyze the data using aggregate measures.

import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')


source_count = ad_clicks.groupby('utm_source').user_id.count()
print(source_count)

ad_clicks['is_click'] = ad_clicks['ad_click_timestamp'].isnull()

print(ad_clicks)
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

print(clicks_by_source.head())

clicks_pivot = clicks_by_source.pivot(\
  index = 'utm_source',
  columns = 'is_click',
  values = 'user_id').reset_index()

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)

print(ad_clicks.groupby('experimental_group').count())
