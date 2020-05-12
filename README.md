# 简易语音识别
基于科大讯飞SDK简易语音识别系统，简单应付一下单位开会等活动记录的问题

## 运行方法

### 运行之前
1. 用python3运行
2. 在ServerInteract.py中设置好科大讯飞APPID、APIKEY和APISecret
3. 安装好必须的dependencies包括pyaudio、websocket-client、FFmpeg和noisereduce

### 正式运行
1. 先开始录音
```
$ python3 RecordMain.py
```

2. 开始识别
```
$ python3 Speech2TextMain.py
```


