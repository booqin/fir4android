## Fir For Android

脚步将Android打包生成的apk上传到服务端

1. 传入output路径+环境
2. 根据路径检索第一个apk文件
3. aapt获取apk信息，git采集日志
4. 上传到fir
    - aapt 采集包名，版本，logo等数据，Python通过路径zip解压获取图片
    - git 获取提交日志 CHANGE_LOG

调用控制台打印日志（含中文）编码异常：
locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')

权限不足