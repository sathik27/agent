from flask import blueprint , justify , jsonify

youtube_bp = blueprint(
    " youtube ",
     __name__
)

@youtube_bp.route(
"/play" ,
methods =["post"]

)
def play():

data = request.get_json(
  silent = True
  )or ()

command = data.get(
"command", 
""
).strip()

if not command :

  return jsonify({
    "success"="false",
    "message"="there's no song name , mentioned "
  })400
  
  
