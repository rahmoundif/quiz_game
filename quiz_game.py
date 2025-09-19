print("Welcome to my computer quiz !")

playing = input("Do you want to play ? ")

if playing != "yes":
    quit();
    
print("Okay Lets go !")

score = 0

answer = input("What does HTTP 201 indicate ? ")
if answer.lower() == "created":
    print('Well done, +1 point')
    score += 1
else:
    print("Wrong, -1 point !")
    score -= 1
    
answer = input("What's the Difference between PUT and PATCH ? ")
if answer.lower() == "replace vs partial update":
    print("Correct ! +1 point")
    score += 1
else:
    print("Nop, -1 point !")
    score -= 1
    
answer = input ("what is the CSS specificity order ? (use '>') ")
if answer.lower() == "inline > id > class > element":
    print("BOOM, +1 point")
    score += 1
else: 
    print("Argh, -1 point !")
    score -= 1
    
answer = input ("What does === in JavaScript ? ")
if answer.lower() == "strict equality":
    print("Very good, +1 point")
    score += 1
else: 
    print("Dammit, -1 point !")
    score -= 1
    
answer = input ("How to prevent XSS primarly ? ")
if answer.lower() == "eyesscapes output":
    print("Rampage ! +1 point")
    score += 1
else:
    print("No, -1 point !")
    score -= 1
    
    
points_label = "point" if abs(score) == 1 else "points"
print("You got " + str(score) + " " + points_label + "!")
if score <= 0:
    print("Keep practicing!")
elif score >= 4:
    print("Excellent!")
else:
    print("Not bad!")



    
    
