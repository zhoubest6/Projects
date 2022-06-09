import pyttsx3
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast,POINTER
#控制音量
dev=AudioUtilities.GetSpeakers()
inter=dev.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
vol=cast(inter,POINTER(IAudioEndpointVolume))
vl=vol.GetMasterVolumeLevel()
vr=vol.GetVolumeRange()
# vol.SetMasterVolumeLevel(vr[1], None)  # 索引：:1是最大值，0是最小值
#语言输出
tts=pyttsx3.init()
tts.setProperty("rate",200)#默认200，控制语速
# tts.setProperty("volume", 1)  # 按当前音量0~1之间
tty="hallo"
# tty = "一天天的不务正业，天底下哪有这种好事，还不快去学习快去学习快去学习！"
# tts.save_to_file(tty,"%s.mp3"%tty)
# tts.runAndWait()
print("————————智能语音————————")

while True:
    vol.SetMasterVolumeLevel(vr[1], None)  # 索引：:1是最大值，0是最小值
    voi = tts.getProperty("voices")  # 获取音色
    tts.setProperty("voice", voi[0].id)  # 英文voi[1]，中文voi[0]
    tts.setProperty("volume", 0.1)  # 按当前音量0~1之间
    print(tty)
    tts.say(tty)

    tts.runAndWait()
    tts.stop()


