import json
import requests

token = 'y0_AgAAAAA9YtyoAADLWwAAAADTgsDRg5Wd6L4kSd-JdHnBpwfIVAO0tXI'
apiurl = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': 'OAuth ' + token}


def createfolder(folder_name):
    params = {'path': folder_name}
    result = requests.put(apiurl, headers=headers, params=params)
    print(result.status_code)
    return result.status_code


def get_folder_info(folder_name):
    params = {'path': folder_name}
    result = requests.get(apiurl, headers=headers, params=params)
    if result.status_code == 200:
        res_dict = json.loads(result.text)
        return res_dict.get('type')


if __name__ == '__main__':
    print(createfolder('dir'))
    print(get_folder_info('dir'))