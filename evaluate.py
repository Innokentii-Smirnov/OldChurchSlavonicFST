import os, shutil
from os import path
if path.exists('correct.txt'):
	with open('correct.txt') as fin:
		old_correct = set(map(str.rstrip, fin))
else:
	old_correct = set()
if path.exists('errors.txt'):
	with open('errors.txt') as fin:
		old_errors = set(map(str.rstrip, fin))
else:
	old_errors = set()
correct = set()
errors = set()
n_correct = 0
total = 0
with open('output.txt') as fin, open('corr.txt') as ref, open('correct.txt', 'w') as corrf, open('errors.txt', 'w') as errf, open('missing.txt', 'w') as mf:
	it = iter(ref)
	new_word = True
	for line in fin:
		if new_word:
			corr = next(it).rstrip()
			new_word = False
		line = line.rstrip()
		if line != '':
			total += 1
			word, segm = line.split(' ← ')
			if segm == corr:
				string = '{0:20} {1}'.format(word, segm)
				corrf.write(string + '\n')
				correct.add(string)
				n_correct += 1
			elif segm != '+?':
				string = '{0:20} {1:25} {2}'.format(word, segm, corr)
				errf.write(string + '\n')
				errors.add(string)
			else:
				string = '{0:20} {1}'.format(word, corr)
				mf.write(string + '\n')
		else:
			new_word = True
new_correct = correct - old_correct
print('New correct: {0}.'.format(len(new_correct)))
new_errors = errors - old_errors
if len(new_errors) == 0:
	print('No new errors.')
else:
	print('New erors: {0}.'.format(len(new_errors)))
with open('new_correct.txt', 'w') as fout:
	for string in new_correct:
		fout.write(string + '\n')
with open('new_errors.txt', 'w') as fout:
	for string in new_errors:
		fout.write(string + '\n')
accuracy = 100 * n_correct / total
print('Accuracy: {0} % ({1} / {2}).'.format(round(accuracy, 2), n_correct, total))
