### mongodb host can be changed from config

### create desire environments as follow
`
SECRET_KEY = ***
ALGORITHM = ***
ACCESS_TOKEN_EXPIRE_MINUTES = ***
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
uvicorn main:app --reload
`

### test
`
pytest --cov=app test_app.py 
` 