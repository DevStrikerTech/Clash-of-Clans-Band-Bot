import emoji

from routes.coc import coc_request
from routes.band import write_post, write_comment


class Player:
    def __init__(self, get_all_post):
        self.get_all_post = get_all_post
        self.player_infomation()

    def player_infomation(self):
        get_all_post = self.get_all_post
        post_response_content = get_all_post['result_data']['items']

        for item in post_response_content:
            commment_count = item['comment_count']
            content = item['content']
            post_key = item['post_key']

            split_content = content.split(' ')
            player_tag = ''.join(split_content[1:]).strip('#')

            if '!player' in split_content and commment_count == 0:

                if player_tag == '':
                    write_comment(comment_body=f"Invalid Commmand: {emoji.emojize(':red_circle:')}", post_key=post_key)

                else:
                    write_comment(comment_body=f"Fatching Data: {emoji.emojize(':dizzy:')}", post_key=post_key)
                    player_response_content = coc_request(f'/players/%23{player_tag}')
                    write_post(post_content=f"Clan Name: {player_response_content['name']} - {player_response_content['tag']}\n"
                                            f"Clan Points: {player_response_content['attackWins']}{emoji.emojize(':crossed_swords:')}")
