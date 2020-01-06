/*----------------------------------------后台Api地址----------------------------------------*/
export const APP_SERVE_URL = 'http://221.133.231.70:9000/';

/*----------------------------------------文件服务器地址----------------------------------------*/
export const FILE_SERVE_URL = 'http://111.111.111.111/kit_file_server/';//文件服务:测试环境

/*----------------------------------------app版本升级服务地址----------------------------------------*/
export const APP_VERSION_SERVE_URL = 'http://111.111.111.111:8111/api/';//app版本升级服务;测试环境,查询app最新版本号,更新日志等信息.

export const IS_DEBUG = true;//是否开发(调试)模式
export const REQUEST_TIMEOUT = 20000;//请求超时时间,单位为毫秒
export const IMAGE_SIZE = 1024;//拍照/从相册选择照片压缩大小
export const QUALITY_SIZE = 94;//图像压缩质量，范围为0 - 100
export const APK_DOWNLOAD = 'http://111.111.111.111/ionic2_tabs.apk';//android apk下载完整地址,用于android本地升级
export const APP_DOWNLOAD = 'http://111.111.111.111/download.html';//app网页下载地址,用于ios升级或android本地升级失败

//code push 部署key
export const CODE_PUSH_DEPLOYMENT_KEY = {
  'android':{
    'Production':'i0LgJRugiIfjVYTgmXs9go45Xc7g26690215-d954-4697-a879-90e0c4612b59',
    'Staging':'WY29_Zyq_hg0eB3TSTGaKRSKPE6k26690215-d954-4697-a879-90e0c4612b59'
  },
  'ios':{
    'Production':'kn3VJ28z0hB_zQYnW-KnblldnBzN26690215-d954-4697-a879-90e0c4612b59',
    'Staging':'SRoxClVMoed8SgwIRxeVCPWx26Fk26690215-d954-4697-a879-90e0c4612b59'
  }
};
