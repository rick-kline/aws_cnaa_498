
list_of_filenames = []
for i in range(2017,2018):
    for j in range(1,5):
        filename = 'weather_' +str(i)+'_Q'+str(j)
        list_of_filenames.append(filename)
        print(filename)