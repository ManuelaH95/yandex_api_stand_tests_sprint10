import configuration
import requests
import data

def post_new_user(user_data):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_data,
                         headers=data.headers)

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=data.headers)

'''if __name__ == '__main__':
    response = post_new_client_kit(data.kit_body)
    print(response.content.decode('utf-8'))'''
