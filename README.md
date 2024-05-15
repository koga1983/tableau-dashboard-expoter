# 🚀 Tableau Dashboard Exporter

このリポジトリには、Tableau ServerおよびTableau Cloud上の特定のタグが設定されたダッシュボードを定期的にPDFとしてエクスポートし、指定されたSlackチャンネルにアップロードするPythonスクリプトが含まれています。これにより、チームメンバーや関係者が最新のダッシュボードを簡単に確認できるようになります。

## 📁 ファイル構成

- `config.json`: 設定情報を含むファイル。
- `main.py`: メインのPythonスクリプト。
- `requirements.txt`: 必要なライブラリを記載したファイル。

## 🛠️ 設定

1. **Slack Bot Tokenの取得**:
   - [Slack API: Applications](https://api.slack.com/apps) にアクセスし、新しいアプリを作成します。
   - Botユーザーを作成し、必要な権限（`files:write`、`chat:write`）を付与します。
   - アプリをワークスペースにインストールし、Bot Tokenを取得します。
   - Botを対象のSlackチャンネルに招待します（例: `/invite @your-bot-name`）。

2. **Tableau Personal Access Tokenの取得**:
   - Tableau ServerまたはTableau Cloudの設定で、Personal Access Tokenを作成します。

3. **config.jsonの編集**:
   - `config.json` ファイルにTableau ServerまたはTableau CloudとSlackの認証情報を入力します。

```json
{
  "tableau": {
    "server_url": "your_tableau_server_or_cloud_url",
    "personal_access_token_name": "your_personal_access_token_name",
    "personal_access_token": "your_personal_access_token",
    "site_id": "your_site_id"
  },
  "slack": {
    "slack_bot_token": "your_slack_bot_token",
    "slack_channel_id": "your_slack_channel_id"
  }
}
```

## 💻 必要な環境

このスクリプトを実行するには、以下の環境が必要です：

- Tableau Server または Tableau Online アカウント
- API トークンの生成
- Python 3.6以上
- Tableau Server Client ライブラリのインストール
- SlackワークスペースとBotトークン

## ⚠️ 注意事項

1. **SSL証明書のインストール**:
   - SlackにPDFファイルをアップロードする際、PythonのSSL証明書が必要です。特にmacOSユーザーは、Pythonの公式インストールに含まれている以下のコマンドを実行してSSL証明書をインストールしてください：

```sh
/Applications/Python\ 3.x/Install\ Certificates.command
```

2. **チャンネルIDの確認**:
   - SlackチャンネルのIDを確認し、正しいチャンネルIDを`config.json`に記載してください。チャンネルIDは、SlackのチャンネルURLの末尾に表示される「C」で始まる文字列です。

3. **Botのチャンネル参加**:
   - Botが対象のSlackチャンネルに参加していることを確認してください。参加していない場合、`/invite @your-bot-name`コマンドを使用してBotをチャンネルに招待します。

4. **トークンの管理**
   - このスクリプトを実行する際には、適切なAPIトークンとアクセス権限が必要です。APIトークンの管理には十分注意してください。

## ▶️ 実行方法

以下のコマンドを実行して必要なライブラリをインストールし、スクリプトを実行します：

```sh
pip install -r requirements.txt
python main.py
```

## 📦 必要なライブラリ

プロジェクトに必要なライブラリは `requirements.txt` ファイルに記載されています：

```plaintext
tableauserverclient
slack_sdk
```

## 🌟 機能

- JSONファイルから設定情報を読み込みます。
- Tableau ServerまたはTableau Cloudの認証にPersonalAccessTokenAuthを使用します。
- 特定のタグが設定されたダッシュボードをPDFとしてエクスポートします。
- データソースに接続できない、もしくは接続エラーのダッシュボードは無視します。
- エクスポートしたPDFファイルを指定されたSlackチャンネルにアップロードします。

## 💡 ユースケース

このスクリプトは、さまざまなユースケースで活用できます。以下にいくつかの具体的な例を挙げます。

1. **定期的なレポート共有**:
   - 週次や月次の定期レポートとして、指定されたタグが付いた最新のダッシュボードをPDF形式でチーム全体に自動的に共有できます。これにより、関係者は最新のデータに基づいて迅速に意思決定を行うことができます。

2. **プロジェクトの進捗確認**:
   - プロジェクトごとにタグを設定し、進捗状況を示すダッシュボードを自動的にSlackにアップロードすることで、プロジェクトチームが最新の状況を簡単に把握できます。

3. **パフォーマンス監視**:
   - 業績やKPIを監視するためのダッシュボードを定期的に共有することで、マネージャーやエグゼクティブがリアルタイムでパフォーマンスを確認できるようになります。

4. **部署間の情報共有**:
   - 異なる部署間で必要なダッシュボードを共有することで、情報の透明性を高め、全体的な効率を向上させることができます。

## 📋 ライセンス
このプロジェクトはMITライセンスの下で公開されています。詳細については、`LICENSE`ファイルを参照してください。
