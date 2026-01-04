# .devcontainer/Dockerfile
FROM mcr.microsoft.com/devcontainers/python:3.11

# 非rootユーザーで作業（既定でvscodeユーザーが用意されている）
USER vscode

# uv をインストール
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# uv が入る ~/.local/bin を PATH に追加
ENV PATH="/home/vscode/.local/bin:${PATH}"

WORKDIR /workspaces/app
CMD ["sleep", "infinity"]
