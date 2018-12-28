## Fir For Android

脚步将Android打包生成的apk上传到服务端

1. 传入output路径
2. 检索apk文件
3. 日志收集
4. 上传到fir
    - aapt 采集包名，版本，logo等数据，Python通过路径zip解压获取图片
    - git 获取提交日志 CHANGE_LOG