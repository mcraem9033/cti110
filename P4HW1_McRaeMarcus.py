#Marcus McRae
#04/22/25
#P4WH1
#Score loop

score_num = int(input("How many scores do you want to enter? "))
print()

#empty list
scores = []

for num in range(1, score_num + 1):
    #collect scores
    score = float(input("Enter score #" + str(num)+ ": "))
    #Evaluate entry
    while score < 0 or score > 100:
        print("INVALID SCORE ENTERED!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(num) +" again: "))
    scores.append(score)
    print()
    
#Find lowest score
lowest = min(scores)
scores_modified = scores
#Drop lowest score
scores_modified.remove(lowest)
#Calculate average
avg = sum(scores_modified)/ len(scores_modified)

 #Determine letter grade for average
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

                     
# TO DO: determine lowest, highest , sum and average for grades
low = min(scores)
high = max(scores)
total = sum(scores)
avg = total / len(scores)

#Display results
print("\n------------Results--------------")
print(f"Lowest Scores : {lowest}")
print(f"Modified List : {scores_modified}")
print(f"Scores Average: {avg:.2f}")
print(f"Grade         : {grade}")
print("---------------------------------")


    

   
