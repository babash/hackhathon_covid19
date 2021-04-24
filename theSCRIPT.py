#!/usr/bin/env python3.8

import pandas as pd
import subprocess

print('anxiety')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr anxiété until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr anxiety until:2021-04-22' > file2.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr anxiétéé until:2021-04-22' > file3.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#
s3 = pd.read_json('file3.json', lines=True)

ss = pd.concat([s1, s2, s3])

ssn = ss.drop_duplicates(subset='id', keep='first')

ssn.to_csv('anxiety_tweets.csv', index=False)

print('Depression')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr dépression until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr depressif until:2021-04-22' > file2.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr depression until:2021-04-22' > file4.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr deppression until:2021-04-22' > file5.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr deprime until:2021-04-22' > file6.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr deprimée until:2021-04-22' > file7.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#
s3 = pd.read_json('file3.json', lines=True)
s4 = pd.read_json('file4.json', lines=True)
s5 = pd.read_json('file5.json', lines=True)
s6 = pd.read_json('file6.json', lines=True)
s7 = pd.read_json('file7.json', lines=True)

ss = pd.concat([s1, s2, s3, s4, s5, s6, s7])
ssn = ss.drop_duplicates(subset='id', keep='first')
ssn.to_csv('depression_tweets.csv', index=False)

print('Suicide')


subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr suicide until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr sucide until:2021-04-22' > file2.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr suicidee until:2021-04-22' > file3.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr sucidee until:2021-04-22' > file4.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#
s3 = pd.read_json('file3.json', lines=True)
s4 = pd.read_json('file4.json', lines=True)
ss = pd.concat([s1, s2, s3, s4])
ssn = ss.drop_duplicates(subset='id', keep='first')
ssn.to_csv('suicide_tweets.csv', index=False)

print('Psychiatrie')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr psychiatre until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr psychiatrie until:2021-04-22' > file2.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr psychiatrique until:2021-04-22' > file3.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr Psychiatry until:2021-04-22' > file4.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#
s3 = pd.read_json('file3.json', lines=True)
s4 = pd.read_json('file4.json', lines=True)

ss = pd.concat([s1, s2, s3, s4])
ssn = ss.drop_duplicates(subset='id', keep='first')
ssn.to_csv('psychiatrie_tweets.csv', index=False)

print('Psychologie')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr psychologue until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr psychologie until:2021-04-22' > file2.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr psychologique until:2021-04-22' > file3.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr Psychology until:2021-04-22' > file4.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#
s3 = pd.read_json('file3.json', lines=True)
s4 = pd.read_json('file4.json', lines=True)

ss = pd.concat([s1, s2, s3, s4])
ssn = ss.drop_duplicates(subset='id', keep='first')
ssn.to_csv('psychologie_tweets.csv', index=False)

print('Fatigue')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr fatigue until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr fatiguee until:2021-04-22' > file2.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#

ss = pd.concat([s1, s2])
ssn = ss.drop_duplicates(subset='id', keep='first')
ssn.to_csv('fatigue_tweets.csv', index=False)

print('Stress')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr stress until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr stressé until:2021-04-22' > file2.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr stressee until:2021-04-22' > file3.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr stresser until:2021-04-22' > file4.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#
s3 = pd.read_json('file3.json', lines=True)
s4 = pd.read_json('file4.json', lines=True)

ss = pd.concat([s1, s2, s3, s4])
ssn = ss.drop_duplicates(subset='id', keep='first')
ssn.to_csv('stress_tweets.csv', index=False)

print('Insomnie')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr insomnie until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr insomniaque until:2021-04-22' > file2.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr insomnia until:2021-04-22' > file3.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr insomnies until:2021-04-22' > file4.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#
s3 = pd.read_json('file3.json', lines=True)
s4 = pd.read_json('file4.json', lines=True)

ss = pd.concat([s1, s2, s3, s4])
ssn = ss.drop_duplicates(subset='id', keep='first')
ssn.to_csv('insomnie_tweets.csv', index=False)

print('Tristesse')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr tristesse until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr triste until:2021-04-22' > file2.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#

ss = pd.concat([s1, s2])
ssn = ss.drop_duplicates(subset='id', keep='first')
ssn.to_csv('tristesse_tweets.csv', index=False)

print('Panique')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr panique until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr paniquee until:2021-04-22' > file2.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr panic until:2021-04-22' > file3.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#
s3 = pd.read_json('file3.json', lines=True)

ss = pd.concat([s1, s2, s3])

ssn = ss.drop_duplicates(subset='id', keep='first')
#print(ssn)
ssn.to_csv('panique_tweets.csv', index=False)

print('Ennui')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr ennui until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr ennuyé until:2021-04-22' > file2.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr ennuyee until:2021-04-22' > file3.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr ennuie until:2021-04-22' > file4.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr ennuyeux until:2021-04-22' > file5.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr ennuyeuse until:2021-04-22' > file6.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#
s3 = pd.read_json('file3.json', lines=True)
s4 = pd.read_json('file4.json', lines=True)
s5 = pd.read_json('file5.json', lines=True)
s6 = pd.read_json('file6.json', lines=True)

ss = pd.concat([s1, s2, s3, s4, s5, s6])

ssn = ss.drop_duplicates(subset='id', keep='first')
#print(ssn)
ssn.to_csv('ennui_tweets.csv', index=False)

print('Heureux')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr heureux until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr heureuse until:2021-04-22' > file2.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#


ss = pd.concat([s1, s2])

ssn = ss.drop_duplicates(subset='id', keep='first')

ssn.to_csv('heureux_tweets.csv', index=False)

print('bonheur/joie')

subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr bonheur until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr joyeux until:2021-04-22' > file2.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr joyeuse until:2021-04-22' > file1.json", shell=True)
subprocess.run("snscrape --jsonl --progress --max-results 2000000 --since 2019-01-01 twitter-search 'lang:fr joie until:2021-04-22' > file2.json", shell=True)

s1 = pd.read_json('file1.json', lines=True)#
s2 = pd.read_json('file2.json', lines=True)#
s3 = pd.read_json('file3.json', lines=True)#
s4 = pd.read_json('file4.json', lines=True)#


ss = pd.concat([s1, s2, s3, s4])

ssn = ss.drop_duplicates(subset='id', keep='first')

ssn.to_csv('bonheur_joie_tweets.csv', index=False)
