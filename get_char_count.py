import urllib.request
import re

#insert starting episode
episode=1

#Insert final episode num 
number_of_episodes=79

#StarTrek Series
series='StarTrek'

print('CHARACTER, LINE_COUNT, WORD_COUNT, EPISODE, NOTE')

while number_of_episodes >= episode:
    
    #Gets URL data
    try:
        url_request = urllib.request.urlopen("http://www.chakoteya.net/%s/%s.htm" % (series, episode) )
        pass
    except:
        print(',,,, episode %s not found on chakoteya.net' % episode )
        episode+=1
        continue
    
    mybytes = url_request.read()
    
    #turns mybytes into string
    url_str = mybytes.decode("utf8")
    
    #Cleans the string so regex can interpret
    str_preped_for_regex=''
    split=url_str.splitlines()
    for elem in split:
        str_preped_for_regex=str_preped_for_regex+elem
    
    #find all charaters in episode. the set() function is deduping the data.
    characters=list(set(re.findall('>([A-Z]*?):', str_preped_for_regex)))

    for character in characters:

        output=re.findall('%s:(.*?)<' % character, str_preped_for_regex)
        
        word_count=0
        for elem in output:
            word_count += len(elem.split())
        
        print('%s, %s, %s, %s,' % (character,  len(output),  word_count, episode  ))
    
    url_request.close()
    episode+=1
