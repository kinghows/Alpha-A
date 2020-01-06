import {Injectable} from '@angular/core';

@Injectable()
export class GlobalData {

  private _phone: string;//用户phone
  private _logintoken: string;//logintoken
  private _sessiontoken: string;//sessiontoken
  private _authTime: number;//sessiontoken认证时间

  //设置http请求是否显示loading,注意:设置为true,接下来的请求会不显示loading,请求执行完成会自动设置为false
  private _showLoading: boolean = true;

  //app更新进度.默认为0,在app升级过程中会改变
  private _updateProgress: number = -1;

  //是否启用文件缓存
  private _enabledFileCache :boolean = true;

  get phone(): string {
    return this._phone;
  }

  set phone(value: string) {
    this._phone = value;
  }

  get logintoken(): string {
    return this._logintoken;
  }

  set logintoken(value: string) {
    this._logintoken = value;
  }

  get showLoading(): boolean {
    return this._showLoading;
  }

  set showLoading(value: boolean) {
    this._showLoading = value;
  }

  get updateProgress(): number {
    return this._updateProgress;
  }

  set updateProgress(value: number) {
    this._updateProgress = value;
  }

  get sessiontoken(): string {
    return this._sessiontoken;
  }

  set sessiontoken(value: string) {
    this._sessiontoken = value;
  }


  get authTime(): number {
    return this._authTime;
  }

  set authTime(value: number) {
    this._authTime = value;
  }

  get enabledFileCache(): boolean {
    return this._enabledFileCache;
  }

  set enabledFileCache(value: boolean) {
    this._enabledFileCache = value;
  }
}
