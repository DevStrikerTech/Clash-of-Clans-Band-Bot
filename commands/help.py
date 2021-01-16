from routes.band import write_comment


class Help:
    def __init__(self, get_all_post):
        self.get_all_post = get_all_post
        self.help_information()

    def help_information(self):
        get_all_post = self.get_all_post
        post_response_content = get_all_post['result_data']['items']

        for item in post_response_content:
            commment_count = item['comment_count']
            content = item['content']
            post_key = item['post_key']

            if '!help' in content and commment_count == 0:
                write_comment(comment_body=f'Here are the list of bot commands:\n'
                                           f'!clan -> Clan Information\n'
                                           f'!player -> Player Infomation\n'
                                           f'!warlog -> Warlog Infomation\n'
                                           f'!joke -> Tells a random joke', post_key=post_key)
