# Solution 02  (language and region)
# Authored by: Daniella Kim :))

lang = ['English', 'Mandarin', 'Hindi', 'Spanish', 'French', 'Arabic', 'Bengali', 'Russian', 'Portugese', 'Indonesian', \
        'Urdu', 'German', 'Japanese', 'Swahili', 'Marathi', 'Telugu', 'Western Punjabi (Lahnda)', 'Wu', 'Tamil', 'Turkish']

region = ['Europe and Central Asia', 'East Asia and the Pacific', 'South Asia', 'Europe and Central Asia', 'Europe and Central Asia', \
          'Middle East and North Africa', 'South Asia', 'Europe and Central Asia', 'Europe and Central Asia', 'East Asia and the Pacific',\
          'South Asia', 'Europe and Central Asia', 'East Asia and the Pacific', 'Sub-Saharan Africa', 'South Asia', 'South Asia', 'South Asia',\
          'East Asia and the Pacific', 'South Asia', 'Europe and Central Asia']


region = 'East Asia and the Pacific'

def language(region):
  for i in range(len(region)):
    if region == 'East Asia and the Pacific':
      region[i] = lang[i]
      language = region[i]
      return language

l = language(region)
print(l)