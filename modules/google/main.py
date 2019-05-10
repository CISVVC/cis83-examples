import urllib.request

def search(terms):
    """Do a Google search and return the results"""
    html = _send_request(terms)
    results = _get_results(html)
    return results

def _send_request(terms):
    """Send search to Google and receive HTML response"""
    terms = terms.replace(' ', '%20')  #replace spaces
         
    #url = 'http://www.google.com/search?q=' + terms
    url = 'http://localhost:8888'
    info = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=info)
                  
    response = urllib.request.urlopen(req)
    html = str(response.read())
    print(html)
    return html

def _strip_html(string):
    new_string = ''
    in_tag = False
    for character in string:
        if character == '<':
            in_tag = True
        if not in_tag:
            new_string += character
        if character == '>':
            in_tag = False
    return new_string

def _get_results(html):
    """
    Finds the links returned in 1st page of results.
    """
    start_tag = '<cite>'  # start of results
    end_tag = '</cite>'   # Results end with this tag
    links = []            # list of result links
                  
    start_tag_loc = html.find(start_tag)  # find 1st link
                     
    while start_tag_loc > -1:
        link_start = start_tag_loc + len(start_tag)
        link_end = html.find(end_tag, link_start)
        links.append(_strip_html(html[link_start:link_end]))
        start_tag_loc = html.find(start_tag, link_end)

    return links

search_term  = input('Enter search terms: ')
result = search(search_term)

print('Google returned %d links:' % len(result))
for link in result:
    print(' ', link)
