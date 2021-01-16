from routes.joke import get_random_joke
from routes.band import write_comment


class Joke:
    def __init__(self, get_all_post):
        self.get_all_post = get_all_post
        self.random_joke_generator()

    def random_joke_generator(self):
        get_all_post = self.get_all_post
        post_response_content = get_all_post['result_data']['items']

        for item in post_response_content:
            commment_count = item['comment_count']
            content = item['content']
            post_key = item['post_key']

            if '!joke' in content and commment_count == 0:
                write_comment(comment_body=f"{get_random_joke()['setup']}\n{get_random_joke()['punchline']}",
                              post_key=post_key)
