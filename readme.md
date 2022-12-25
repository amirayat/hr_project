### Store presence_duration of arrival departure history times listed in enter_exit_time of employees by setting up a crontab to run update_scheduler.js file. inside update_scheduler.js there is a custom update function to subtract entrance and exit times and this will allow employees to have hourly leave. Final result will look like as follow which means employee with 1234567890 national_code had two arrival and one hourly leave at 1671989039716:
`
{
  "_id": {
    "$oid": "63a8557615c9135cc2e72cd4"
  },
  "national_code": "1234567890",
  "arrived": true,
  "departured": true,
  "date": {
    "$date": {
      "$numberLong": "1671926400000"
    }
  },
  "enter_exit_time": [
    {
      "$date": {
        "$numberLong": "1671988946614"
      }
    },
    {
      "$date": {
        "$numberLong": "1671989039716"
      }
    },
    {
      "$date": {
        "$numberLong": "1671989060443"
      }
    }
  ],
  "presence_duration": 6987958
}
`  

### mongodb host can be changed from config

### create desire environments as follow
`
SECRET_KEY = ***
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = ***(in seconds)
`

### create admin user command
`
python3 admin_manager.py --action=create --username=*** --password=***
`

### run cronjob periodic tasks to save employees presence_duration at every 5 minuts
`
python3 scheduler.py
`

### use can swagger to access endpoints
`
{host_ip}:{port}/docs/
`

### to run project
`
python3 main.py
`

### test
`
pytest test_main.py 
` 