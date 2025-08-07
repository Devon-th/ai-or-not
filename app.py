from flask import Flask, render_template, request, redirect, session, url_for
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

images = [
    'static/ai/plane.png',
    'static/ai/flower.png', 
    'static/ai/roman.png',
    'static/ai/chair.png',
    'static/ai/tip.png',
    'static/real/ground-squirrel.png',
    'static/real/petroglyphs.png',
    'static/real/shark-volcano.png',
    'static/real/worm.png',
    'static/real/fungus.png',
]

headlines = [
    'Boeing jet lands after "Catastrophic" structural failure in wing',
    "Rare 'Rainbow Bloom' Flower Discovered by Nature Enthusiast in Amazon, Emitting Previously Unknown Light Frequencies",
    "Archaeologists Astonished after Discovery of Roman-era Mosaic in Woman's Backyard",
    'Company introduces monthly subscription for heated office chairs',
    'Self-Checkout Lanes Begin Asking for Tips at All Walmart Stores',
    'Ground Squirrels Are Taking Over a North Dakota City and Officials Are Not Amused',
    'Mystery over 500-year-old petroglyphs that have washed up on a beach',
    'Sharks found living inside underwater volcanoes',
    'A worm has been revived after 46,000 years in the Siberian permafrost',
    'Chernobyl Disaster Fungus That Eats Radiation May One Day Protect Early Mars Inhabitants',
]

is_real = [
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    True,
    True,
    True,
]

def game_reset():
    session['already_played'] = []
    session['lives'] = 3
    session['score'] = 0
    session['question'] = 0
    lives = 3

@app.route('/')
def index():
    return render_template('index.html')

def get_images(): #returns image_data which contains [path, headline, boolean]
        already_played = session.get('already_played')
        while True:
            randIndex = random.randint(0, len(images) - 1)
            if randIndex not in already_played:
                break
        return {
            'path': images[randIndex],
            'headline': headlines[randIndex],
            'reality': is_real[randIndex],
            'index': randIndex,
        }

@app.route('/check-answer', methods=['POST'])
def check_answer():
    already_played = session.get('already_played')
    question_number = session.get('question')
    image_data = session.get('image_data')
    index = image_data['index']
    score = session.get('score')
    lives = session.get('lives')
    user_answer = request.form.get('action')
    print(user_answer)
    image_data = session.get('image_data')
    reality = image_data['reality']
    if request.method == 'POST':
        if (user_answer == "ai" and reality == False) or (user_answer == "real" and reality == True):
            score += 1
        else:
            lives -= 1
        question_number += 1
        session['question'] = question_number
        session['score'] = score
        session['lives'] = lives
        session['already_played'].append(index) # prevents duplicates
        return redirect(url_for('play_round'))
    else:
        return "ERROR"

@app.route('/play')
def start_game():
    session['already_played'] = []
    session['lives'] = 3
    session['score'] = 0
    session['question'] = 0
    return redirect(url_for('play_round'))

@app.route('/play-round')
def play_round():
    question_number = session.get('question', 0) # default is 0 if there is none
    score = session.get('score')
    lives = session.get('lives')
    game_finished = question_number > len(images) - 1
    print(f"game_finished: {game_finished}")
    if game_finished:
        return render_template('finish.html', finishing_message = "Congratulations! You've finished the game!", score = score, lives = lives)
    elif lives == 0:
        return render_template('finish.html', finishing_message = "Game Over!", score = score, lives = lives)
    
    else:
        image_data = get_images()
        session['image_data'] = image_data
        story = question_number + 1
        return render_template('game_page.html', image = image_data['path'], headline = image_data['headline'], score = score, lives = lives, story = story) # maybe this can go to another route called 'results'

if __name__ == '__main__':
    app.run(debug=True)