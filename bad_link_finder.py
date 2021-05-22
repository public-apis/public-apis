"""
Note:
 This Program fillters out most of the good links and collect links that returned error save them in separate file
 Some of the links may work in browser but not in python due to security of webpage
 So a manual check on those filtered record is needed
 Since the program already filtered most of the good links we can easily check the reaming link and save time
 This program takes a while depending on internet speed

 Instruction:
 Download the bad_link_filter and readme as raw file
 Then execute in your machine
 The bad links will be saved in error.txt file
 Then you have to manually check the links mentioned in error.txt file and remove the good links from the file
 
"""

def is_url_requests(url):   #Check the status code of webpage
    import requests
    try:
        headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-us,en;q=0.5',
                        'Accept-Encoding': 'gzip,deflate',
                        'Connection': 'keep-alive',
                        'Access-Control-Allow-Methods': 'POST',
                        'Access-Control-Allow-Headers': 'X-PINGOTHER, Content-Type',
                        'Pragma': 'no-cache',
                        'Cache-Control': 'no-cache',
                   }
        proxies = {"http": None,"https": None}
        response=requests.get(url,headers=headers,proxies=proxies)
        status=response.status_code
        if status>=400:
            return status
    except requests.exceptions.ConnectionError as ce:
        return 'HTTPSConnectionPool error'
    except Exception as e:
        return e

def func(indexes):
    error_links=[]
    print('InProgress, Sections completed will be shown below.Please wait for a while')
    for index,section in indexes.items():
        for title,row in section.items():
            error=is_url_requests(row['link'])
            if error:
                e={
                    'index':index,
                    'title':title,
                    'link': row['link'],
                    'error':error
                    }
                error_links.append(e)
        print(index,' section completed')
    return error_links

def get_lines_from_file(location):      #open,read,return lines after filtering empty lines and spaces
    lines=[]
    with open(location,'r') as file:
        lines=[line.strip() for line in file.readlines() if line.strip()]
    return lines

def line_to_dict(line):     #covert api row to dict
    line=line.strip().split('|')
    name,link=line[1].strip().split('](')
    name,link=name[1:],link[:-1]
    row={
        'link':link,
        'description':line[2],
        'auth':line[3],
        'https':line[4],
        'cors':line[5],
        }
    return name,row

def section_to_dict(lines,ind):     #convert section to dict
    section={}
    while ind<len(lines):
        if 'Back to Index' in lines[ind]:       #Break a section
            break
        name,row=line_to_dict(lines[ind])
        section[name]=row
        ind+=1
    return ind,section

def get_section_wise_dict(lines):   #convert unstructured lines to section wise dict
    ind=0
    indexes={}
    while ind<len(lines):
        if '###' in lines[ind]:                 #Enters a section
            name=lines[ind][3:].strip()
            ind,indexes[name]=section_to_dict(lines,ind+1+1+1)
        ind+=1
    return indexes

def link_to_error_file(error_links):    #Enters the bad links to a file which further requires manual check
    lines=[]
    for row in error_links:
        statement='| {} | [{}]({}) | {} |'.format(row['index'], row['title'], row['link'], str(row['error']))
        lines.append(statement)
    print(lines)
    with open('error.txt','w') as file:
        file.write('\n#Manual check has to be done on following links#\n\n')
        file.write('| Section | API  |Error/Satus Code |\n')
        file.write('|---|---|---|\n')
        for line in lines:
            file.write(line)
            file.write('\n')
    print("Written to file")
    print('Manual check has to be done for the links saved in error.txt')
    
location= input('Location of readme public api readme file: ')       #Get location of raw readme file
lines=get_lines_from_file(location)
indexes=get_section_wise_dict(lines)
error_links=func(indexes)
link_to_error_file(error_links)
