# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import requests
import json


class AliyunAPIOCRException(Exception):
    pass


class BaseClient(object):

    def __init__(self, app_code=None, app_key=None, app_secret=None):
        super(BaseClient, self).__init__()
        self._app_code=app_code
        self._app_key=app_key
        self._app_secret=app_secret
        self._url=None

    def _prepend_auth_headers(self, headers={}):
        if self._app_code is not None:
            headers['Authorization'] = 'APPCODE %s' % self._app_code
            return headers
        if self._app_key is not None and self._app_secret is not None:
            pass
            #todo
        raise AliyunAPIOCRException("App Code, App Key, App Secret cannot be all empty.")

    def _post(self, payload, url):
        headers = self._prepend_auth_headers(
            {'Content-Type': 'application/json; charset=UTF-8'}
        )
        result = requests.post(url, data=json.dumps(payload), headers=headers, verify=False)
        return result.json()


class DriverLicense(BaseClient):

    def ocr(self, image_base64):
        url = "http://dm-52.data.aliyun.com/rest/160601/ocr/ocr_driver_license.json"
        payload = {
            "inputs": [
                {
                    "image": {
                        "dataType": 50,
                        "dataValue": image_base64
                    }
                }]
        }
        return self._post(payload, url)


class BusinessLicense(BaseClient):

    def ocr(self, image_base64):
        url = "http://dm-58.data.aliyun.com/rest/160601/ocr/ocr_business_license.json"
        payload = {
            "inputs": [
                {
                    "image": {
                        "dataType": 50,
                        "dataValue": image_base64
                    }
                }
            ]
        }
        return self._post(payload, url)


class IdCard(BaseClient):

    def ocr(self, image_base64, face=True):
        url = "http://dm-51.data.aliyun.com/rest/160601/ocr/ocr_idcard.json"
        payload = {
            "inputs": [
                {
                    "image": {
                        "dataType": 50,
                        "dataValue": image_base64
                    },
                    "configure": {
                        "dataType": 50,
                        "dataValue": "{\"side\":\"%s\"}" % ("face" if face else "back")
                    }
                }
            ]
        }
        return self._post(payload, url)


class VehicleLicense(BaseClient):

    def ocr(self, image_base64):
        url = "http://dm-53.data.aliyun.com/rest/160601/ocr/ocr_vehicle.json"
        payload = {
            "inputs": [
                {
                    "image": {
                        "dataType": 50,
                        "dataValue": image_base64
                    }
                }]
        }
        return self._post(payload, url)

