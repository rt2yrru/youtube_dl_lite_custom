import youtube_dl,json
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
def my_hook(d):
    print(d)
ydl_opts ={
    'format': '480p/best',
    'postprocessors': [],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
fab='list.txt'
url=[]
k=0
fr = open(fab, "r") #file read
for line in fr:
  k+=1
  url.append(line)
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
 for j in url:
   ydl.download([j])
  

