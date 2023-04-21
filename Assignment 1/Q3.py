num_courses = 20
total_scores= 0
#>90-A
#80-B
#75-79-C
#60-D
#59-F
for i in range(num_courses):
    sum=int(total_scores)
average= int(num_courses)/int(total_scores)
print(average)
if(average_score>90):
    print('A')
elif(average_score>=80):
    print('B')
elif(average_score>=75) and (average_score<79):
    print('C')
elif(average_score<60):
    print('D')
else:
    print('F')


