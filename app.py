from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = "SHAFSDFHW"

images = [
    'static/ai/plane.png',
    'static/ai/flower.png', 
    'static/ai/roman.png',
    'static/ai/chair.png',
    'static/ai/tip.png',
    'static/real/radioactive-wasps.png', 
    'static/real/ground-squirrel.png',
    'static/real/petroglyphs.png',
    'static/real/shark-volcano.png',
    'static/real/worm.png',
]

headlines = [
    'Boeing jet lands after "Catastrophic" structural failure in wing',
    'Rare "Rainbow Bloom" Flower Discovered by Nature Enthusiast in Amazon, Emitting Previously Unknown Light Frequencies',
    "Archaeologists Astonished after Discovery of Roman-era Mosaic in Woman's Backyard",
    'Company introduces monthly subscription for heated office chairs',
    'Self-Checkout Lanes Begin Asking for Tips at All Walmart Stores',
    'Radioactive wasp nest found at site where US once made nuclear bombs',
    'Ground Squirrels Are Taking Over a North Dakota City and Officials Are Not Amused',
    'Mystery over 500-year-old petroglyphs that have washed up on a beach',
    'Sharks found living inside underwater volcanoes',
    'A worm has been revived after 46,000 years in the Siberian permafrost',
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

"""

- Get random number /
- Use that as index for images, headlines, is_real /
- Display to site
- Allow player to click button
- Check answer: Correct -> score+=1, incorrect -> lives-=1
    
"""

def game_reset():
    session['lives'] = 3
    session['score'] = 0
    session['question'] = 0
    lives = 3

@app.route('/')
def index():
    return render_template('index.html')

def get_images(): #returns image_data which contains [path, headline, boolean]
        image_data = [] #[path, headline, boolean]
        randIndex = random.randint(0, len(images) - 1)
        image_data.extend([images[randIndex], headlines[randIndex], is_real[randIndex], randIndex])
        return {
            'path': images[randIndex],
            'headline': headlines[randIndex],
            'reality': is_real[randIndex],
            'index': randIndex,
        }

@app.route('/check-answer', methods=['POST'])
def check_answer():
    question_number = session.get('question')
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
        return redirect(url_for('play_round'))
    else:
        return "ERROR"

@app.route('/play')
def start_game():
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
        return render_template('game_page.html', image = image_data['path'], headline = image_data['headline']) # maybe this can go to another route called 'results'

if __name__ == '__main__':
    app.run(debug=True)