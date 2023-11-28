import requests

def test_github_repository():
    # 测试一，请求访问自己的GitHub仓库
    url = f"https://api.github.com/users/1128zl/repos"

    # 测试二，请求访问一个未存在的GitHub用户仓库
    # url = f"https://api.github.com/users/1128zlz/repos"

    # 获取请求结果
    response = requests.get(url)

    # 请求成功时
    if response.status_code == 200:
        # 将 HTTP 响应内容解析为 JSON 格式
        repos = response.json()
        # 检查返回结果是否为列表
        assert isinstance(repos, list)
        # 打印总的存储库数目
        print(f"Total repositories: {len(repos)}")

        # 遍历存储库，打印名称，URL
        for repo in repos:
            repo_name = repo["name"]
            repo_url = repo["html_url"]
            print(f"Repository: {repo_name}")
            print(f"URL: {repo_url}")
    
    # 请求失败时：
    else:
        # 检查请求是否成功
        assert response.status_code == 200
        print(f"Failed to retrieve repositories. Status code: {response.status_code}")

test_github_repository()