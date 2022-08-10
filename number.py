import boto3
print("hello word")
##Billing
client=boto3.client('ce')
responce=client.get_cost_and_usage(
    TimePeriod={
        'Start': '2022-06-27',
        'End': '2022-07-27'
    },
    Granularity='DAILY',
    Metrics = ["BlendedCost"]

)
print((responce))