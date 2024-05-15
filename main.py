import tableauserverclient as TSC
from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json
import os


# JSONファイルから設定情報を読み込む関数
def load_config(config_file='config.json'):
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config


# Tableauからタグ付きダッシュボードをPDFとしてエクスポートする関数
def export_dashboards_to_pdf(server, tag):
    with server.auth.sign_in(server_auth):
        req_option = TSC.RequestOptions()
        req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Tags, TSC.RequestOptions.Operator.Equals, tag))
        all_views, pagination_item = server.views.get(req_option)

        pdf_files = []
        for view in all_views:
            try:
                server.views.populate_pdf(view)
                pdf = view.pdf
                file_name = f"{view.name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
                with open(file_name, 'wb') as f:
                    f.write(pdf)
                pdf_files.append(file_name)
            except TSC.ServerResponseError as e:
                print(f"Failed to export view {view.name}: {e}")
        return pdf_files


# Slackにファイルをアップロードする関数
def upload_files_to_slack(slack_client, channel_id, files):
    for file in files:
        try:
            response = slack_client.files_upload_v2(
                channel=channel_id,
                file=file,
                filename=os.path.basename(file),
                title=os.path.basename(file)
            )
        except SlackApiError as e:
            print(f"Error uploading {file} to Slack: {e.response['error']}")


if __name__ == "__main__":
    config = load_config()

    tableau_config = config['tableau']
    slack_config = config['slack']

    server = TSC.Server(tableau_config['server_url'], use_server_version=True)
    server_auth = TSC.PersonalAccessTokenAuth(
        tableau_config['personal_access_token_name'],
        tableau_config['personal_access_token'],
        tableau_config['site_id']
    )

    slack_client = WebClient(token=slack_config['slack_bot_token'])
    slack_channel_id = slack_config['slack_channel_id']  # チャンネルIDを確認
    tag = "pdf"  # 対象のタグを指定

    print(f"Starting dashboard export and upload at {datetime.now()}")
    pdf_files = export_dashboards_to_pdf(server, tag)
    upload_files_to_slack(slack_client, slack_channel_id, pdf_files)
    print("Completed dashboard export and upload.")
