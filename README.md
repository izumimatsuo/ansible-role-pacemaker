# ansible-role-pacemaker [![Build Status](https://www.travis-ci.com/izumimatsuo/ansible-role-pacemaker.svg?branch=main)](https://www.travis-ci.com/izumimatsuo/ansible-role-pacemaker)

CentOS 7 に pacemaker を導入する ansible role です。


## 設定項目

以下の設定項目は上書き可能。

| 項目名                          | デフォルト値             | 説明                           |
| ------------------------------- | ------------------------ | ------------------------------ |
| pacemaker_cluster_name          | hacluster                | クラスタ名                     |
| pacemaker_cluster_hosts         | {{ ansible_play_hosts }} | 監視対象                       |
| pacemaker_cluster_auth_password | password                 | クラスタ管理ユーザのパスワード |
