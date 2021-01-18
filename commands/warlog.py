import emoji

from routes.coc import coc_request
from routes.band import write_post, write_comment


class Warlog:
    def __init__(self, get_all_post):
        self.get_all_post = get_all_post
        self.warlog_infomation()

    def warlog_infomation(self):
        get_all_post = self.get_all_post
        post_response_content = get_all_post['result_data']['items']

        for item in post_response_content:
            commment_count = item['comment_count']
            content = item['content']
            post_key = item['post_key']

            split_content = content.split(' ')
            clan_tag = ''.join(split_content[1:]).strip('#')

            if '!warlog' in split_content and commment_count == 0:

                if clan_tag == '':
                    write_comment(comment_body=f"Invalid Commmand: {emoji.emojize(':red_circle:')}", post_key=post_key)

                else:
                    write_comment(comment_body=f"Fatching Data: {emoji.emojize(':dizzy:')}", post_key=post_key)
                    warlog_response_content = coc_request(f'/clans/%23{clan_tag}/warlog?limit=2')['items']
                    
                    warlog_result = ''
                                  
                    for warlog in warlog_response_content:
                                  warlog_result = warlog_result + f"{warlog['clan']['name']} VS {warlog['opponent']['name']}"

                    write_post(post_content=warlog_result)
