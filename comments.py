import os
import requests
from dotenv import load_dotenv


def get_list():
    load_dotenv()
    access_token = os.environ.get('GHP_ACCESS_TOKEN')
    if not access_token:
        return []

    query = """
    query {
      repository(owner: "kaffa", name: "kaffa.im") {
        discussions(last: 100) {
          # type: DiscussionConnection
          totalCount # Int!
    
          pageInfo {
            # type: PageInfo (from the public schema)
            startCursor
            endCursor
            hasNextPage
            hasPreviousPage
          }
    
          edges {
            # type: DiscussionEdge
            cursor
            node {
              # type: Discussion
              id
              title
              body
            }
          }
    
          nodes {
            # type: Discussion
            id
            title
            body
            comments(first:100){
              edges{
                node{
                  id
                  body
                  publishedAt
                  createdAt
                  author{
                    avatarUrl
                  }
                }
              }
            }
          }
        }
      }
    }
    """

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.github.com/graphql", json={"query": query}, headers=headers)

    if response.status_code != 200:
        print(f"请求失败，状态码: {response.status_code}")
        return []

    data = response.json()['data']
    comment_nodes = data['repository']['discussions']['nodes']

    return comment_nodes


def main():
    nodes = get_list()
    for node in nodes:
        print('-' * 100)
        print('Title: ' + node['title'])


if __name__ == '__main__':
    main()

