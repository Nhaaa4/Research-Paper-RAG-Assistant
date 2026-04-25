css = """
<style>
:root {
    color-scheme: light dark;
    --bg-start: #f8fafc;
    --bg: #eef2f7;
    --bg-end: #ffffff;
    --sidebar-bg: #ffffff;
    --panel: #ffffff;
    --panel-strong: #f1f5f9;
    --border: #d8dee8;
    --text: #111827;
    --muted: #475569;
    --accent: #0f766e;
    --user-bg: #d9f99d;
    --assistant-bg: #ffffff;
    --source-bg: #f8fafc;
    --shadow: rgba(15, 23, 42, 0.08);
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg-start: #0b0f14;
        --bg: #0e1117;
        --bg-end: #0b0f14;
        --sidebar-bg: #0b0f14;
        --panel: #161b22;
        --panel-strong: #1f2937;
        --border: #30363d;
        --text: #e6edf3;
        --muted: #9da7b3;
        --accent: #2dd4bf;
        --user-bg: #123f3a;
        --assistant-bg: #171f2b;
        --source-bg: #111827;
        --shadow: rgba(0, 0, 0, 0.24);
    }
}

.stApp {
    background: linear-gradient(180deg, var(--bg-start) 0%, var(--bg) 45%, var(--bg-end) 100%);
    color: var(--text);
}

.main .block-container {
    max-width: 1120px;
    padding-top: 2rem;
}

h1, h2, h3, h4, h5, h6,
p, li, label, span, div {
    color: var(--text);
}

[data-testid="stSidebar"] {
    background-color: var(--sidebar-bg);
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p {
    color: var(--text);
}

[data-testid="stFileUploader"],
[data-testid="stSelectbox"],
[data-testid="stTextInput"],
[data-testid="stSlider"] {
    color: var(--text);
}

.stTextInput input,
.stSelectbox div[data-baseweb="select"] > div {
    background-color: var(--panel);
    border-color: var(--border);
    color: var(--text);
}

.stButton button {
    background-color: var(--panel-strong);
    border: 1px solid var(--border);
    color: var(--text);
    border-radius: 8px;
}

.stButton button:hover {
    border-color: var(--accent);
    color: var(--text);
}

[data-testid="stChatInput"] {
    background-color: var(--panel);
    border-top: 1px solid var(--border);
}

.chat-container {
    max-width: 900px;
    margin: auto;
}

.user-message {
    background-color: var(--user-bg);
    color: var(--text);
    padding: 14px 16px;
    border-radius: 10px;
    margin: 10px 0 10px auto;
    width: fit-content;
    max-width: 70%;
    text-align: left;
    border: 1px solid rgba(45, 212, 191, 0.25);
    box-shadow: 0 10px 28px var(--shadow);
    line-height: 1.55;
}

.bot-message {
    background-color: var(--assistant-bg);
    color: var(--text);
    padding: 14px 16px;
    border-radius: 10px;
    margin: 10px auto 10px 0;
    width: fit-content;
    max-width: 75%;
    text-align: left;
    border: 1px solid var(--border);
    box-shadow: 0 10px 28px var(--shadow);
    line-height: 1.6;
}

.user-message b,
.bot-message b,
.source-box b {
    color: var(--text);
}

.source-box {
    background-color: var(--source-bg);
    color: var(--muted);
    padding: 10px 12px;
    border-radius: 8px;
    font-size: 13px;
    margin-top: 8px;
    border: 1px solid var(--border);
    max-width: 75%;
    line-height: 1.45;
}

.stAlert {
    background-color: var(--panel);
    color: var(--text);
}
</style>
"""

user_template = """
<div class="user-message">
    <b>You:</b><br>
    {{MSG}}
</div>
"""

bot_template = """
<div class="bot-message">
    <b>Assistant:</b><br>
    {{MSG}}
</div>
"""

source_template = """
<div class="source-box">
    <b>Sources:</b><br>
    {{SOURCES}}
</div>
"""
