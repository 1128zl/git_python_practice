import requests

# 执行API调用并查看响应
languages = ["javascript", "ruby", "c", "java", "perl", "haskell", "go"]
headers = {"Accept": "application/vnd.github.v3+json"}

for language in languages:
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc"
    r = requests.get(url, headers=headers)
    print(f"\n{language.capitalize()} Popular Projects:")

    # 响应请求是否成功
    if r.status_code == 200:
        # 将响应转换为字典
        response_dict = r.json()

        # 检测API返回的结果是否完整
        if not response_dict['incomplete_results']:
            # 返回的所有仓库的详细信息列表
            repo_dicts = response_dict['items']

            # 输出每个项目的信息
            for repo_dict in repo_dicts[:5]:  # 只打印前五个项目
                print(f"\nName: {repo_dict['name']}")
                print(f"Owner: {repo_dict['owner']['login']}")
                print(f"Stars: {repo_dict['stargazers_count']}")
                print(f"Repository: {repo_dict['html_url']}")
                print(f"Description: {repo_dict['description']}")
        else:
            print("Incomplete results returned from API.")
    else:
        print("Failed to retrieve data from the API.")
