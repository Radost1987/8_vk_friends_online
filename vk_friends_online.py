import vk
import getpass


APP_ID = 5804520  

def get_user_login():
    your_login=input('Enter your login: ')
    return your_login


def get_user_password():
    your_password=getpass.getpass('Enter your password: ')
    return your_password    


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    id_friends_online=api.friends.getOnline()
    if not id_friends_online:
        return None
    info_friends_online=api.users.get(user_ids=id_friends_online)
    return info_friends_online
    
if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    try:
        friends_online = get_online_friends(login, password)
    except:
        print('Incorrect login or password')
    else:
        if friends_online is not None:
            print('Friends online:' )
            for friend in friends_online:
                print(friend['first_name'], friend['last_name'])
        else:        
            print('No friends online')   

