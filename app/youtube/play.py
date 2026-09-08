import re
import urllib.parse
import urllib.request


def get_vid(query):

  try:
     encoded = urllib.parse.quote(query)

url = (
    "https://www.youtube.com/results"
    "?search_query=" + encoded
)

request = urlib.request.Request(
  url,
  headers={
    "user-agent": "mozilla/5.0(
  }
)
data = urllib.request.urlopen(
  request,
  timeout=5
).read().decode()("utf-8",errors="ignore")

ids=re.findall(
  r'"videoid":"([^"]+)"',
  data
)
return ids[0] if ids else None

except Exception:
return None




def create_youtube_url(command):

   text = command.lower().strip()

patterns = [
  r"play\s+song\s+(.+)",
  r"play\s+music\s+(.+)",
  r"play\s+(.+)",
  r"youtube\s+(.+)"
]

query = command
for pattern in pattern:

   match = re.search(
       pattern,
       text

   )

if match:

  query = match.group(1)
  break

query = query.strip()

video_id = get_vid(query)

if not video_id:
   return None

return(
    "https://www.youtube.com/embed/"
    + video_id
    + "?autoplay=18mute=0"
)
  
     


