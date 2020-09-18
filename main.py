import Assignment_1
import Assignment_2
import datetime
data= [{"FormSubmissionID":68223,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data123","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"06\/01\/2021","Numbers":"198"},{"FormSubmissionID":68222,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"08\/01\/2020","Numbers":"3"},{"FormSubmissionID":68221,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"02\/01\/2021","Numbers":"156"},{"FormSubmissionID":68220,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"11\/01\/2020","Numbers":"135"},{"FormSubmissionID":68219,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"01\/01\/2021","Numbers":"148"},{"FormSubmissionID":68218,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"04\/01\/2021","Numbers":"175"},{"FormSubmissionID":68217,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"10\/01\/2020","Numbers":"120"},{"FormSubmissionID":68216,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"03\/01\/2021","Numbers":"165"},{"FormSubmissionID":68215,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Forecast","Month and Year":"05\/01\/2021","Numbers":"186"},{"FormSubmissionID":68214,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Planned","Month and Year":"07\/01\/2020","Numbers":"1"},{"FormSubmissionID":68213,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Actual","Month and Year":"09\/01\/2020","Numbers":"6"},{"FormSubmissionID":68212,"FormID":"54792","CFT":"Sourcing","Group":"Testing Reports","Category":"Testing Report Data","Sub-Category":"Testing Report Data Bot","Initiative":"Bot for Testing Report Data","Type":"Planned","Month and Year":"12\/01\/2020","Numbers":"141"}]
Assignment_2.write_csv(data)

Assignment_1.date_format(data,"Month and Year")

Assignment_1.sumOfNum(data,"Numbers")

Assignment_1.cummmu_sum(data,"Numbers")
Assignment_1.deleteValues(data,"FormID")
Assignment_1.deleteValues(data,"FormSubmissionID")
Assignment_1.concat_values(data,"Category","Sub-Category")
Assignment_1.type_entry(data,"Type","Actual")
Assignment_1.type_entry(data,"Type","Forecast")
print Assignment_1.get_number(data)

for row in data:
    date1 = datetime.date(2020,01,01)
    date2 = (datetime.datetime.strptime(row["Month and Year"],"%m\/%d\/%Y")).date()
    Assignment_1.no_of_days(date1, date2)




