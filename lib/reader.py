import parser
import webbrowser
import re

def repl():
    while True:
        read = input('rss>> ')
        eval = feed_eval(read)
        if eval is not None:
            post_repl(eval)
            print('Exited Feed')

def post_repl(feed):
    print('In feed '+ feed.title)
    curr = 0
    while True:
        found_n = False
        found_p = False
        found_k = False
        if curr > len(feed.posts)-1 or curr < 0:
            return None
        inp = input('post {0} of {1}>> '.format(curr, len(feed.posts)-1))
        if re.search('n', inp):
            inp = re.sub('n','',inp)
            found_n = True
        if re.search('p(?!\[)', inp):
            inp = re.sub('p','',inp)
            found_p = True
        if re.search('k(?!\[)', inp):
            inp = re.sub('k','',inp)
            found_k = True
        if inp == 'ls':
            i = 0
            for post in feed.posts:
                print(str(i) + ' ' + post.title)
                i += 1
            continue
        if inp == 'q' or inp == 'quit' or inp == 'exit':
            return None
        if inp == 'ar' or inp == 'readall':
            feed.printout()
            continue
        if inp == 'h' or inp == 'help':
            rss_help()
            continue
        curr_post = feed.posts[curr]
        if re.search('\[(.*?)\]', inp):
            st = re.split('\[', inp)
            st = [re.sub('\[|\]','', elem) for elem in st]
            if st[0] == 'r':
                for i in range(int(st[1])):
                    curr_post.printout()
                    curr += 1
                    if curr > len(feed.posts)-1:
                        return None
                    curr_post = feed.posts[curr]
                continue
            if st[0] == 'k':
                curr += int(st[1])
                continue
            if st[0] == 'g':
                curr = int(st[1])
                continue
            if st[0] == 'p':
                curr -= int(st[1])
                continue
        if inp == 'r':
            curr_post.printout()
        elif inp == 't':
            print(curr_post.title)
        elif inp == 'd':
            print(curr_post.time)
        elif inp == 'a':
            print(curr_post.author)
        elif inp == 'lp':
            print(curr_post.link)
            found_p = False
        elif inp == 'l':
            open_link(curr_post.link)
        if found_n and not found_p and not found_k:
            curr += 1
            continue
        elif found_p and not found_n and not found_k:
            curr -= 1
            continue
        elif found_k and not found_n and not found_p:
            curr = len(feed.posts)-1
            continue

def feed_eval(str):
    if str == 'exit' or str == 'quit' or str == 'q':
        print('Goodbye!')
        exit()
    elif str == 'help' or str == 'h':
        rss_help()
        return None
    elif str == 'url' or str == 'link' or str == 'l':
        return start(input('Feed URL>> '))
    else:
        rss_help()
        return None

def start(url_str):
    return parser.feed(url_str)
    
def open_link(link):
    webbrowser.open(link, 2)
    
def rss_help():
    post_opts = '''
    ar - print all information for all posts
    ls - list all post titles and their numbers
    q - exit feed
    h - show this help dialog
    r - print all post information for the current post
    r[x] - print all information for next x posts. The current post will be changed to the next post in line
    t - print title only of current post
    d - print post time only of current post
    a - print author only of current post
    l - open the current post in your web browser
    lp - prints the link of the current post
    k - skip to last post (suffix)
    k[x] - skip the next x posts (including the current one)
    g[x] - skip to post number x (can go backwards)
    n - go to next post (can be used as suffix)
    p - skip to previous post (suffix)
    p[x] - go back x posts
    '''
    feed_opts = '''
    q - quit app
    h - show this help dialog
    url - enter a feed url and start reading that feed
    '''
    print("App Options:")
    print(feed_opts)
    print("Feed Options")
    print(post_opts)
    print("Post {n}>> indicates the current position in the feed.")
    
repl()