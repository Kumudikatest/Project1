import requests

def handler(event, context):
    try:
        res = requests.get(
            "https://api.taxrates.io/api/v1/tax/countrycode",
            params={"domain":"com","country_code":"+94","filter":"test"},
            headers={"Accept":"application/json"}
        )
        # your code goes here
    except BaseException as e:
        # error handling goes here
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
