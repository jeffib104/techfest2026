from flask import Flask, render_template
import os

app = Flask(__name__)

#event datas so that I dont have to make a page for every single event
EVENTS_DATA = {
    "debugging": {
        "name": "Attack On Bugs",
        "description": "A competitive Python debugging event designed to test your ability to identify, analyze, and fix errors in code within a limited time.",
        "rules": [
            "Only Python language is allowed.",
            "Internet usage is strictly prohibited.",
            "External storage devices, notes, or reference material are not allowed.",
            "Participants must work individually.",
            "Time limits are strict for each round (20 mins per round).",
            "Any form of malpractice results in immediate disqualification."
        ],
        "round_structure": [
            "Round 1: 20 points (Need 10+ to qualify for Round 2).",
            "Round 2: 20 points (Need 30+ total to qualify for Final Round).",
            "Final Round: 20 points.",
            "Winners selected based on highest total score out of 60."
        ],
        "prize": "Winner based on total points and completion time",
        "time": "Feb 4-5 | 3 Rounds (20 min each)",
        "requirements": "Individual participation | Python"
    },
    "technical-quiz": {
        "name": "Technoverse (Technical Quiz)",
        "description": "The Ultimate Technical Quiz Battle testing speed and accuracy.",
        "rules": [
            "Each team must have 2 members.",
            "Students from all departments can participate.",
            "No mobile phones or smart devices allowed.",
            "Teams must not discuss after raising their hand.",
            "Quiz master's decision on scoring is final.",
            "Any form of cheating leads to immediate disqualification."
        ],
        "round_structure": [
            "Three total rounds.",
            "First raised hand gets the chance to answer.",
            "Only qualified teams move to next rounds.",
            "Tie-breaker round conducted in case of a tie."
        ],
        "prize": "Excellence in Tech Quiz",
        "time": "4th February | 60 min",
        "requirements": "Team of 2 members"
    },
    "logo-designing": {
        "name": "Vision to Vector (Logo Designing)",
        "description": "Design an original and creative logo based on a spot-given theme using mobile design tools.",
        "rules": [
            "Each participant may submit only one original logo.",
            "Logo must be original and created solely for this competition.",
            "Plagiarism or AI-generated logos lead to disqualification.",
            "Offensive or political content is strictly prohibited.",
            "Late submissions will not be accepted."
        ],
        "software": [
            "Authorised mobile devices (Android/iOS) will be provided.",
            "Software available: CANVA, PIXELLAB, PICSART.",
            "Final format: PNG/JPEG (Transparent background preferred).",
            "Must submit a brief description of the logo concept."
        ],
        "prize": "Winning Logo Design Award",
        "time": "Feb 4-5 | 45 min",
        "requirements": "Individual participation | Mobile provided"
    },
    "rapid-type": {
        "name": "Rapid Type (Type Master)",
        "description": "A typing skill contest where participants compete for speed and accuracy on a keyboard.",
        "rules": [
            "One official attempt per participant (Practice attempts allowed before).",
            "Participants must start together when instructed.",
            "Refreshing or restarting the test page is strictly prohibited.",
            "Accuracy must stay above 90% to avoid disqualification.",
            "No external help, scripts, or auto-typing tools."
        ],
        "software": [
            "Platform: Monkey Type software."
        ],
        "prize": "Type Master Title",
        "time": "Feb 4-5 | Single Round",
        "requirements": "Keyboard typing speed and accuracy"
    },
    "blind-coding": {
        "name": "Blind Coding Contest",
        "description": "Code without access to debugging tools, auto-completion, or syntax highlighting.",
        "rules": [
            "All coding must be done on offline lab systems provided.",
            "Submissions must be original and written during the contest.",
            "No use of personal laptops or online compilers.",
            "Internet resources and pre-written libraries are prohibited.",
            "Judged on correctness, efficiency, and adherence to constraints."
        ],
        "prize": "Blind Coding Excellence Award",
        "time": "Feb 4-5 | Standard Time Limits",
        "requirements": "Languages: Python or C"
    },
    "treasure-hunt": {
        "name": "Code of the Crypt (Treasure Hunt)",
        "description": "Follow a unique sequence of clues across the campus to unlock the final location.",
        "rules": [
            "Teams must have 2-4 members.",
            "Follow clues in a unique sequence; no skipping allowed.",
            "Collect letters at every clue position to unlock the final clue.",
            "Mobile phones and internet not allowed unless permitted.",
            "Stay within the campus area at all times.",
            "Cheating or following other teams leads to disqualification."
        ],
        "prize": "First team to reach final location wins",
        "time": "5th February | 10:30 AM - 11:30 AM",
        "requirements": "Team of 2-4 members | Secondary Entrance"
    },
    "web-design": {
        "name": "WebNOVA (Website Design)",
        "description": "Create a simple, user-friendly, and original website reflecting a spot-given theme.",
        "rules": [
            "Individual participation only.",
            "Website must be original and created within the 1-hour duration.",
            "No pre-made templates or previously created websites.",
            "No AI-generated full websites.",
            "Internet access and online website builders are not allowed.",
            "Final submission: ZIP folder of all website files."
        ],
        "software": [
            "Permitted: HTML, CSS, JavaScript.",
            "Must run properly on a standard web browser.",
            "Must include: Home page, About section, and Navigation menu."
        ],
        "prize": "Web Design Champion",
        "time": "Feb 4-5 | 60 min",
        "requirements": "Individual participation | HTML/CSS/JS"
    }
}


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/events')
def events():
    return render_template('events.html')
@app.route('/help')
def help():
    c_email = os.environ.get('COORD_EMAIL', 'contact@techfest26.com')
    c_phone = os.environ.get('COORD_PHONE', 'Phone number')
    c_phone1 = os.environ.get('COORD_PHONE1', 'Phone number 1')

    return render_template('help.html', coord_email=c_email, coord_phone=c_phone, coord_phone1=c_phone1)

@app.route('/events/<event_id>')
def event_detail(event_id):
    event = EVENTS_DATA.get(event_id)
    return render_template('event_details.html', event=event)

if __name__ == '__main__':
    app.run(debug=True)