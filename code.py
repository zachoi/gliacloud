import urllib2  
from collections import Counter
import operator

def find_bigrams(input_list):
	return zip(input_list, input_list[1:])

def find_trigrams(input_list):
  return zip(input_list, input_list[1:], input_list[2:])

def ngram_probs(input_list):
	b_list = find_bigrams(input_list)
	bigram_probs =Counter(b_list)

	t_list = find_trigrams(input_list)
	trigram_probs =Counter(t_list)
	
	return bigram_probs, trigram_probs

def prob3(bigram, cnt2, cnt3):
	dic = {}
	b_v = cnt2[bigram]
	for k, v in cnt3.iteritems():
		if k[0:2] == bigram:
			dic[k[2]] = float(v)/b_v
	return dic

def predict_max(starting, cnt2, cnt3):
	
	bigram = starting
	list_of_words = []

	for k, v in cnt2.iteritems():
		p = prob3(bigram, cnt2, cnt3)
		work = max(p.iteritems(), key=operator.itemgetter(1))[0]
		list_of_words.append(work)
		bigram = (bigram[1], work)
		if work == '.' or len(list_of_words) > 15:
			break
	
	'''
	p = prob3(bigram, cnt2, cnt3)
	work = max(p.iteritems(), key=operator.itemgetter(1))[0]
	
	test =  (starting[0], work)
	print test
	p = prob3(test, cnt2, cnt3)
	work = max(p.iteritems(), key=operator.itemgetter(1))[0]
	print work 
	
	#list_of_words.append(work)
	'''	
	return list_of_words


data = urllib2.urlopen("https://raw.githubusercontent.com/livingbio/DeepLearningTutorial/master/raw_sentences.txt") 
lines = ""
for line in data: 
    lines += line
lines =  lines.lower()
input_list = lines.split(" ");


#Quiz 2-1
cnt2, cnt3  = ngram_probs(input_list)
print(cnt2[('we', 'are')])
#Quiz 2-2
p = prob3(('we', 'are'), cnt2, cnt3)
print(p['family'])

#Quiz 2-3
sent = predict_max(('we', 'are'), cnt2, cnt3)
print(' '.join(sent))




'''
print(cnt3[('we', 'are')])
for k, v in cnt3.iteritems():
	if v > 1:
		print k, v
		print k[0:2] == ('made', 'a')
		print k[2]
		break

'''

