import json

def process_server_data(json_string):
    try:
        #Converting JSON string to Python dictionary
        #ex: '{"name": "Rahim", "age": 25}' > {'name': 'Rahim', 'age': 25}
        data = json.loads(json_string)  
        servers = data['servers']
        
        for server in servers:
            name = server['name']
            status = server['status']
            print(f"Server: {name} - Status: {status}")
            
    except json.JSONDecodeError as e:
        print(f"JSON Error: {e}")



mock_api = '{"servers": [{"name": "web-01", "status": "up"}, {"name": "db-01", "status": "down"}]}'
process_server_data(mock_api)