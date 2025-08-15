import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
nana_projects = response.json()

for project in nana_projects:
    project_name = project["name"]
    url = project["http_url_to_repo"]
    print(f"Project name: {project_name}\nProject URL: {url}\n")