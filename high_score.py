import pickle
import collections

high_scores = [65536, 10000]
#high_scores = high_scores.sort(reverse=True)
#doesn’t work when you try to sort it
with open("highscores.pkl","wb") as out:
	pickle.dump(high_scores, out)

new_score = 12000

with open("highscores.pkl","rb") as in_:
	high_scores = pickle.load(in_)
if new_score not in high_scores:
	high_scores.append(new_score)
with open("highscores.pkl","wb") as out:
	pickle.dump(high_scores, out)

print("{{TITLE:^{PAGE_WIDTH}}}".format(PAGE_WIDTH=40).format(TITLE="HIGH SCORES"))
print("-" * 40)
for all_scores in high_scores:
	print(all_scores)
