from flask import Flask, render_template
import random

app = Flask(__name__)

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

lives = 3

"""

- Get random number /
- Use that as index for images, headlines, is_real /
- Display to site
- Allow player to click button
- Check answer: Correct -> score+=1, incorrect -> lives-=1
    
"""

def game_reset():
    lives = 3

@app.route('/')
def index():
    return render_template('index.html')

def get_images(): #returns image_data which contains [path, headline, boolean]
        image_data = [] #[path, headline, boolean]
        randindex = random.randint(0, len(images) - 1)
        image_data.extend([images[randindex], headlines[randindex], is_real[randindex]])
        return image_data

#@app.route('/check-answer')
#def check_answer():
#    user_answer = request.form.get('action')
#    if user_answer == 'ai' and #something here:

@app.route('/play')
def game_play():
    while lives > 0:
        image_data = get_images()
        image_path = image_data[0]
        headline = image_data[1]
        is_real = image_data[2]
        return render_template('game_page.html', image=image_path, headline=headline)

if __name__ == '__main__':
    app.run(debug=True)