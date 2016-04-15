arrBad = [
'facebook',
'google',
'gmail',
'yahoo',
'bing',
'twitter',
'tinder',
'social',
'gmail'
]

def profanityFilter(text):
	brokenStr1 = text.split()
	badWordMask = '!@#$%!@#$%^~!@%^~@#$%!@#$%^~!'
	new = ''
	for word in brokenStr1:
		if word in arrBad:
    	# if word in arrBad:
    			print brokenStr1
    			print word + ' <-- Social section found, this is categorized'
    	text = text.replace(word,badWordMask[:len(word)])
	    	#print new
	return text
print profanityFilter("This sentence contain some gmail sentence")