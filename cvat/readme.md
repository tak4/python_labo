
# CVAT

[CVAT](https://www.cvat.ai/)

インストール

[Installation Guide](https://docs.cvat.ai/docs/administration/basics/installation/)

```bash
sudo apt-get --no-install-recommends install -y \
apt-transport-https \
ca-certificates \
curl \
gnupg-agent \
software-properties-common
```

- **-no-install-recommends:**
    - パッケージの依存関係にある、推奨されるパッケージはインストールしないように指定します。
- **install -y:**
    - 指定したパッケージをインストールし、インストール中に確認を求められた場合に自動的に「yes」と答えるようにします。
- **apt-transport-https, ca-certificates, curl, gnupg-agent, software-properties-common:**
    - インストールするパッケージの名称です。それぞれ以下のような役割を持ちます。
        - **apt-transport-https:** HTTPSプロトコルを利用してパッケージをダウンロードできるようにするためのパッケージです。
        - **ca-certificates:** HTTPS通信で使用する証明書を管理するためのパッケージです。
        - **curl:** HTTPクライアントであり、リモートファイルのダウンロードやデータの転送に利用されます。
        - **gnupg-agent:** GPG（GNU Privacy Guard）のエージェントプログラムで、GPGキーの管理を支援します。
        - **software-properties-common:** ソフトウェアソースの追加や管理を支援するパッケージです。

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

このコマンドは、**Dockerをインストールする準備として、DockerのGPGキーを取得し、システムに登録する**ためのものです。

### 各要素の役割

- **curl:**
    - 指定されたURLからデータをダウンロードするコマンドです。ここでは、DockerのGPGキーがダウンロードされます。
- **fsSL:**
    - curlコマンドのオプションです。
        - f: エラーが発生しても続行します。
        - s: 標準出力への出力を抑制します。
        - S: ヘッダー情報を表示しません。
        - L: リダイレクトをフォローします。
- [**https://download.docker.com/linux/ubuntu/gpg](https://download.docker.com/linux/ubuntu/gpg):**
    - DockerのGPGキーが公開されているURLです。
- **|:**
    - パイプで、curlコマンドの出力（ダウンロードしたGPGキー）を次のコマンドの入力に接続します。
- **sudo apt-key add -:**
    - sudo: root権限でコマンドを実行します。
    - apt-key add: ダウンロードしたGPGキーをシステムの信頼できるキーリストに追加します。
    - : 標準入力からキーを読み込むことを示します。

### このコマンド全体の意味

1. **GPGキーのダウンロード:** curlコマンドで、Dockerの公式リポジトリからGPGキーをダウンロードします。
2. **GPGキーの追加:** ダウンロードしたGPGキーを、apt-keyコマンドを使ってシステムの信頼できるキーリストに追加します。これにより、aptでDockerのパッケージをインストールする際に、そのパッケージの署名が有効であることを確認できるようになります。

```bash
sudo apt-get --no-install-recommends install -y \
docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

このコマンドは、**Ubuntu/Debian系Linuxシステム上にDockerをインストールする**ためのものです。

### 各要素の役割

- **sudo:**
    - コマンドの実行にroot権限が必要であることを示します。システムの設定を変更するためには、root権限が必要です。
- **apt-get:**
    - Ubuntu/Debian系システムのパッケージ管理ツールです。
- **-no-install-recommends:**
    - パッケージの依存関係にある、推奨されるパッケージはインストールしないように指定します。
- **install -y:**
    - 指定したパッケージをインストールし、インストール中に確認を求められた場合に自動的に「yes」と答えるようにします。
- **docker-ce, docker-ce-cli, containerd.io, docker-compose-plugin:**
    - インストールするパッケージの名称です。それぞれ以下のような役割を持ちます。
    - **docker-ce:** Docker Engineのコミュニティエディションです。コンテナを実行するためのコアエンジンです。
    - **docker-ce-cli:** Docker Engineのコマンドラインインターフェースです。dockerコマンドで利用するインターフェースです。
    - **containerd.io:** コンテナランタイムのデーモンです。Docker Engineがコンテナを管理するために利用します。
    - **docker-compose-plugin:** Docker Composeプラグインです。複数のコンテナをまとめて管理するためのツールです。

docker ステータス確認

```bash
sudo systemctl status docker
```

起動

```bash
sudo docker compose up -d
```

スーパーユーザー追加

```bash
docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
```