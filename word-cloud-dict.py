def make_wordcloud_dict(long_string):
    words = long_string.lower().split(" ")

    wordcloud = {}

    for word in words:
        if word in wordcloud:
            wordcloud[word] += 1
        else:
            wordcloud[word] = 1
        
    return wordcloud


print(make_wordcloud_dict("After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar."))

#get individ words --> split on " ", make lower case
#make empty dictionary, call it wordcloud
#get count of each word
#wordcloud[word] = count of that word
#return dict
