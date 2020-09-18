import csv
'''data= [{"FormSubmissionID":68223,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data123","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"06\/01\/2021","Numbers":"198"},{"FormSubmissionID":68222,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"08\/01\/2020","Numbers":"3"},{"FormSubmissionID":68221,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"02\/01\/2021","Numbers":"156"},{"FormSubmissionID":68220,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"11\/01\/2020","Numbers":"135"},{"FormSubmissionID":68219,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"01\/01\/2021","Numbers":"148"},{"FormSubmissionID":68218,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"04\/01\/2021","Numbers":"175"},{"FormSubmissionID":68217,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"10\/01\/2020","Numbers":"120"},{"FormSubmissionID":68216,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"03\/01\/2021","Numbers":"165"},{"FormSubmissionID":68215,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"05\/01\/2021","Numbers":"186"},{"FormSubmissionID":68214,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Planned","Month and Year":"07\/01\/2020","Numbers":"1"},{"FormSubmissionID":68213,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Actual","Month and Year":"09\/01\/2020","Numbers":"6"},{"FormSubmissionID":68212,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Planned","Month and Year":"12\/01\/2020","Numbers":"141"}]


headers = ["FormSubmissionID", "FormID","CFT","Group","Category","Sub-Category","Initiative","Type","Month and Year","Numbers"]

with open('C:\Users\Zestl Software\PycharmProjects\Assignments1\outputdata.csv', 'w') as outfile:
    mywriter = csv.DictWriter(outfile, fieldnames=headers)
    mywriter.writeheader()

    for d in data:
        mywriter.writerow(d)'''



def write_csv(data):
    headers = ["FormSubmissionID", "FormID", "CFT", "Group", "Category", "Sub-Category", "Initiative", "Type",
               "Month and Year", "Numbers"]

    with open('C:\Users\Zestl Software\PycharmProjects\Assignments1\outputdata2.csv', 'w') as outfile:
        mywriter = csv.DictWriter(outfile, fieldnames=headers)
        mywriter.writeheader()

        for d in data:
            mywriter.writerow(d)
