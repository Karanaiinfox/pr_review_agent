from pr_agent import cli
from pr_agent.config_loader import get_settings
# from Flask import Flask, request, jsonify
from flask import Flask, render_template, request, jsonify, send_file
# app=flask.app()
app = Flask(__name__, static_folder="reports")
@app.route('/')
def main():
    pr_url = request.args.get("pr_url")
    print(pr_url,'pr_url--------------->>>>>>>>>')
    # Fill in the following values
    provider = "github" # github/gitlab/bitbucket/azure_devops
    user_token = "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"  #  user token
    openai_key = "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"  # OpenAI key
    pr_url = "https://github.com/shoyo-www/Aws/pull/1/commits/ac525321bd874fe5c2e02201209498ab4c3a7446"      # PR URL, for example 'https://github.com/Codium-ai/pr-agent/pull/809'
    command = '/review' # Command to run (e.g. '/review', '/describe', '/ask="What is the purpose of this PR?"', ...)
    # pr_url = request.args.get("pr_url")s
    # Setting the configurations
    get_settings().set("CONFIG.git_provider", provider)
    get_settings().set("openai.key", openai_key)
    get_settings().set("github.user_token", user_token)
    
    # Run the command. Feedback will appear in GitHub PR comments
    cli.run_command(pr_url, command)
    return "Command executed successfully",200