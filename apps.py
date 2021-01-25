from flask import Flask,jsonify

app=Flask(__name__)

courses=[{
    'name':"Python Proframming Certification",
    'course_id':"0",
    'description':"Python Programming certificate will you learn "
                   "python in the structured learning path with innovation",
    'price':"2500"
},
    {
        'name':"Data science with python certification",
        'course_id':"1",
        'description':"Data science with python helps you master the"
                    "data science",
        'price':"3000"
    }]

@app.route('/')
def index():
    return  "Welcome To The Rest Api"
@app.route('/courses',methods=["GET"])
def all_courses():
    return jsonify({'Courses':courses} )

@app.route('/courses/<int:courseid>',methods=["GET"])
def get_course(courseid):
    return jsonify({'Your Course':courses[courseid]})

@app.route('/courses',methods=["POST"])
def create():
    course= {
           'name':"Python Proframming Certification",
           'course_id':"5",
           'description':"Python Programming certificate will you learn "
                         "python in the structured learning path with innovation",
            'price':"2500"
        }

    courses.append(course)
    return jsonify({'created':course})

@app.route('/courses/<int:course_id>',methods=["PUT"])
def update(course_id):
    courses[course_id]['description']="Hi this is updated text"
    return jsonify({'Updated Course':courses[course_id]})



if __name__=="__main__":
    app.run(debug=True)
