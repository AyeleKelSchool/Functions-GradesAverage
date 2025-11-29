def get_average():
    total = 0
    average = 0
    count = 0 # count keep tracks of how many times a score was entered.
    for i in range(1, 4): # usage of for loop, since it known how many iteration is needed
        score = float(input(f"Enter Score {i}: ")) # the usage of float because it provides more flexibility
        total += score

    average = total / 3

    return average # the avg is returned

def check_average_score(averages):
    if averages > 95.0:
        print(f'The average score is {averages:.1f}')
        print("Congratulations! You did great!")
    elif averages >= 85.0 and averages <= 95.0:
        print(f'The average score is {averages:.1f}')
        print("You did great, but did not reach the Top High.")
    elif averages >=70.0 and averages <= 84.0:
        print(f'The average score is {averages:.1f}')
        print("Good effort, but you could do better.")
    else: # this anything less than 70
        print(f'The average score is {averages:.1f}')
        print("You need to study harder next time.")

def main():
   average_score = get_average()
   check_average_score(average_score)

main()




