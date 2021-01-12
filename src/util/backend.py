import json
import requests
from pandas.io.json import json_normalize
import pandas
import uuid

from config import S3_BUCKET_NAME, s3_client

github_api = "https://api.github.com"
gh_session = requests.Session()

def commits_of_repo_github(repo, owner, api):
    
    i = 1
    
    url_repos = api + '/repos/{}/{}'.format(owner, repo)
    url_commits = api + '/repos/{}/{}/commits?page={}&per_page=1'.format(owner, repo,i)
    commit_pg = gh_session.get(url = url_commits)
    repos_pg = gh_session.get(url = url_repos)

    if commit_pg.status_code == 200 and repos_pg.status_code == 200:
        
        json_data = json.loads(commit_pg.text)
        json_repos_data = json.loads(repos_pg.text)
        
        result = {}

        result['github_response_code'] = str(repos_pg.status_code)
        result['message'] = 'public'
        result['owner'] = owner
        result['repository'] = repo
        result['clone_url'] = json_repos_data['clone_url']
        if len(json_data) == 1:
            for msg in json_data:
                result['latest_commit'] = msg['commit']['author']['date']
                result['latest_commit_author'] = msg['commit']['author']['name']
                result['commit_message'] = msg['commit']['message']

        else:
            result['latest_commit'] = '-'
            result['latest_commit_author'] = '-'
            result['commit_message'] ='-'
            
        return result

    else:

        result = {}
        result['github_response_code'] = str(repos_pg.status_code)
        result['message'] = 'repo not found / not authorize'
        result['owner'] = owner
        result['repository'] = repo

        return result

def list_process(reqs, output):
    
    download_map = {}
    download_map['owner'] = []
    download_map['repository'] = []
    download_map['github_response_code'] = []
    download_map['message'] = []
    download_map['clone_url'] = []
    download_map['latest_commit'] = []
    download_map['latest_commit_author'] = []
    download_map['commit_message'] = []

    for req in reqs:

        detail = req.split('/')
        owner = detail[0]
        repo = detail[1]

        stats = commits_of_repo_github(repo,owner,github_api)

        download_map['owner'].append(stats['owner'])
        download_map['repository'].append(stats['repository'])
        download_map['github_response_code'].append(stats['github_response_code'])
        download_map['message'].append(stats['message'])
        if stats['github_response_code'] == '200':
            download_map['clone_url'].append(stats['clone_url'])
            download_map['latest_commit'].append(stats['latest_commit'])
            download_map['latest_commit_author'].append(stats['latest_commit_author'])
            download_map['commit_message'].append(stats['commit_message'])

        else:
            download_map['clone_url'].append('-')
            download_map['latest_commit'].append('-')
            download_map['latest_commit_author'].append('-')
            download_map['commit_message'].append('-')

        download_data = pandas.DataFrame(download_map)

    print(download_data)

    path_filename = './result/generation_report_'+str(uuid.uuid4().hex)+'.csv'
    

    if output == 'csv':
        download_data.to_csv(path_filename, index=False)
        return "git stats request is generated"

    elif output == 's3':
        try:
            download_data.to_csv(path_filename, index=False)
            response = s3_client.upload_file(path_filename, S3_BUCKET_NAME, 'result/generation_report_'+str(uuid.uuid4().hex)+'.csv')

            return "git stats request is generated"
        except:

            return "there is problem generate to S3"




    