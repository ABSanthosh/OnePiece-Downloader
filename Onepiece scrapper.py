import requests
from bs4 import BeautifulSoup
import urllib.request
import json


mainList = {
  "E217": "https://ninjashare.to/download/cP9sHutAaGUCsmxWcNrqJK?t=a492e8657a6c2cba51ceef03a1117273",
  "E218": "https://ninjashare.to/download/h9yi7Gy7QBW34JdZnJQaCD?t=2fe19761a8e93aaa1bd48007bc889e0d",
  "E219": "https://ninjashare.to/download/dG5bAXR2rybjqNAScGv8pe?t=ac0179079b6a879911823fc8de3dd22b",
  "E220": "https://ninjashare.to/download/v5PXoRimfXxoKczojbV6bQ?t=0bd8a70a03b431a1bdb6fb31c623285d",
  "E221": "https://ninjashare.to/download/4xQkymo8cue1u78FdSFdXn?t=966080e7e04a12c745ddcecbdb1953c0",
  "E222": "https://ninjashare.to/download/dNCZ8FTxsEfsHqnnfgzArW?t=aff7a1873364b8b88cc8beab5407e776",
  "E223": "https://ninjashare.to/download/mfv5j7ucyDKD1SNskvGWzW?t=62091bcd296ae81add4a6cbc93887d66",
  "E224": "https://ninjashare.to/download/qef5PSDSPo6JiM453VJ3hr?t=40462356184328971ffeee18172dd6ce",
  "E225": "https://ninjashare.to/download/rpH7PUzCYRfsjVvhT8zA2a?t=dfb7beafa16a73439fae909da6e735dd",
  "E226": "https://ninjashare.to/download/cLBNmGJhzJQpuHpZL22w3U?t=b69aba9a77191cc5f879c8829e4a69c9",
  "E227": "https://ninjashare.to/download/mP2KFnUQVh2Z3vZminAj5e?t=0b85eed6296505ddb62b636273032c6b",
  "E228": "https://ninjashare.to/download/rUo3SFUSxc7x1DJWv8qmM7?t=6cbbe3461f079cd080a59fa941b1388d",
  "E229": "https://ninjashare.to/download/ivPrjv1fDztWrnh8QuSrg5?t=2ce80e76bb51d98caa2b7fa2cd428ea7",
  "E230": "https://ninjashare.to/download/g7gs9gwhZhThxrkjYHDtj1?t=1d25760ce0aafde81dc8d7ad60ee7912",
  "E231": "https://ninjashare.to/download/p92iXphBFGVdQC7QvJwudP?t=4a9db8fbe97942b46cf059bf3d746f37",
  "E232": "https://ninjashare.to/download/8mRtbsTTndUoHnZqNwXMJe?t=2c5933b8d990260dd71d7761d85a14f1",
  "E233": "https://ninjashare.to/download/nSH3u9Pi6YGFjv9LoP7bRA?t=d79735f810052c3005b86385df3a78ee",
  "E234": "https://ninjashare.to/download/iAFcW84sXphuxs5ixFD5Se?t=1bd0811d7e0805ea810142af0dd51e1f",
  "E235": "https://ninjashare.to/download/2DPWogVY3uo5QpYaRvro7p?t=88473d69d61e4ea347cb5a64a1f08724",
  "E236": "https://ninjashare.to/download/koHpGSp1REkt9D9xXX8eBQ?t=95f58a6b289ef35a4a9e13ed3cb2eb12",
  "E237": "https://ninjashare.to/download/dPctrApXSXqerSytUvPKnR?t=4a0880db097acde4d88bf2b4cc071233",
  "E238": "https://ninjashare.to/download/iNDivyfAcxgi9AuEzoZGUd?t=77fb81baac153b3ede7bb3460fde2050",
  "E239": "https://ninjashare.to/download/uuGLmV4YWooK94VjvbZ2EA?t=2f7dd50a0571252430fcc5852729f417",
  "E240": "https://ninjashare.to/download/9A927rkVA7xuyhg96cKHTU?t=b705fdc1f61e70ea90fc55f68e125215"
}

newObj={}

def fetchAllDownloadLinks():
    for i in range(0,len(mainList.values())):
        value = list(mainList.values())[i]
        key = list(mainList.keys())[i]
        r = requests.get(value)
        soup = BeautifulSoup(r.text, 'html.parser')

        tempObj = {}

        for link in soup.find_all('a'):
            link = link.get("href")

            if link != None:
                if "stream" in link.lower():
                    if "streamta" in link.lower():
                        tempObj["streamta"] = link
                    if "streamsb" in link.lower():
                        tempObj["streamsb"] = link

                newObj[key] = tempObj

def saveJsonToFile():
    with open('links.json', 'w') as f:
        json.dump(newObj, f)

def downloadVideo(id,name):
    base = "https://2475155055.tapecontent.net/radosgw/{id}/0matIc0E6lPTKOgdGZFsSCP-8VCIUvE83dFp7oN53bTdWTlh5jZ-cVbi1F00TfDflgvjFmaW9M55qhrjKVqrLO8DMZpb5GPspp9oy-8aFgszss90KHy3jVIXwAV06kcI644joVtwDVcDd6I5TO1wavwPsPA7yXmUEFqkqdnQ_OHQrj2kAStYz2SIPbFcC9gy0fN34gvqVDYILh90VJiXSceJDUtQ4_F6HsH68-hTNX0fjiPal7AZul1wdptUND4gf6HjseUaiZaa9sEY/video.mp4?stream=1".format(id=id)
    urllib.request.urlretrieve(base, './OnePiece/{name}.mp4'.format(name=name)) 

# fetchAllDownloadLinks()
# saveJsonToFile()


with open('links.json', 'r') as f:
    data = json.load(f)

    for i in range(0,len(data.keys())):
        value = list(data.values())[i]
        key = list(data.keys())[i]

        if value.get("streamta") != None:
            downloadVideo(value.get("streamta").split("/")[-1],key)
        elif(value.get("streamsb") != None):
            # print(value.get("streamsb"))
            pass
