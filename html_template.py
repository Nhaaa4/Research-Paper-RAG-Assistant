css = """
<style>
:root {
    color-scheme: light dark;
    --rp-bg: Canvas;
    --rp-panel: color-mix(in srgb, CanvasText 5%, Canvas);
    --rp-panel-strong: color-mix(in srgb, CanvasText 9%, Canvas);
    --rp-text: CanvasText;
    --rp-muted: color-mix(in srgb, CanvasText 68%, Canvas);
    --rp-border: color-mix(in srgb, CanvasText 18%, Canvas);
    --rp-accent: var(--primary-color, #0f766e);
    --rp-user-bg: color-mix(in srgb, var(--rp-accent) 18%, Canvas);
    --rp-assistant-bg: color-mix(in srgb, CanvasText 4%, Canvas);
    --rp-source-bg: color-mix(in srgb, CanvasText 6%, Canvas);
    --rp-shadow: color-mix(in srgb, CanvasText 10%, transparent);
}

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stToolbar"] {
    background-color: var(--rp-bg) !important;
    color: var(--rp-text) !important;
}

.main .block-container {
    max-width: 1120px;
    padding-top: 2rem;
}

h1, h2, h3, h4, h5, h6,
p, li, label,
[data-testid="stMarkdownContainer"],
[data-testid="stWidgetLabel"] {
    color: var(--rp-text) !important;
}

a {
    color: var(--rp-accent) !important;
}

code,
pre {
    background-color: var(--rp-panel-strong) !important;
    color: var(--rp-text) !important;
    border-radius: 6px;
}

[data-testid="stSidebar"] {
    background-color: var(--rp-panel) !important;
    border-right: 1px solid var(--rp-border) !important;
}

[data-testid="stSidebar"] * {
    color: var(--rp-text);
}

.stTextInput input,
.stNumberInput input,
.stTextArea textarea,
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea,
.stSelectbox div[data-baseweb="select"] > div,
[data-testid="stChatInput"],
[data-testid="stChatInput"] textarea {
    background-color: var(--rp-bg) !important;
    border-color: var(--rp-border) !important;
    color: var(--rp-text) !important;
}

.stTextInput input::placeholder,
.stTextArea textarea::placeholder,
[data-testid="stChatInput"] textarea::placeholder {
    color: var(--rp-muted) !important;
}

[data-baseweb="popover"],
[data-baseweb="popover"] > div,
[data-baseweb="popover"] [data-baseweb="block"],
[data-baseweb="popover"] [data-baseweb="menu"],
[data-baseweb="menu"],
[data-testid="stMainMenu"],
[data-testid="stMainMenu"] *,
[role="listbox"],
[role="option"],
[role="menu"],
[role="menuitem"] {
    background-color: var(--rp-panel) !important;
    color: var(--rp-text) !important;
}

[role="option"]:hover,
[role="option"][aria-selected="true"],
[role="menuitem"]:hover {
    background-color: color-mix(in srgb, var(--rp-accent) 18%, var(--rp-panel)) !important;
    color: var(--rp-text) !important;
}

[data-testid="stMainMenu"] button,
[data-testid="stMainMenu"] div,
[data-testid="stMainMenu"] span,
[data-testid="stMainMenu"] p,
[data-baseweb="popover"] button,
[data-baseweb="popover"] div,
[data-baseweb="popover"] span,
[data-baseweb="popover"] p {
    color: var(--rp-text) !important;
}

[data-baseweb="popover"] svg,
[data-testid="stMainMenu"] svg {
    color: var(--rp-text) !important;
    fill: currentColor !important;
}

body > div[data-baseweb="popover"],
body > div[data-baseweb="popover"] *,
body [data-baseweb="popover"] [class*="st-"],
body [data-baseweb="popover"] [class*="menu"] {
    background-color: var(--rp-panel) !important;
    color: var(--rp-text) !important;
    border-color: var(--rp-border) !important;
}

.stButton button {
    background-color: var(--rp-panel) !important;
    border: 1px solid var(--rp-border) !important;
    color: var(--rp-text) !important;
    border-radius: 8px;
}

.stButton button:hover {
    background-color: var(--rp-bg) !important;
    border-color: var(--rp-accent) !important;
    color: var(--rp-text) !important;
}

[data-testid="stFileUploader"] section,
[data-testid="stFileUploaderDropzone"] {
    background-color: var(--rp-bg) !important;
    border: 1px dashed var(--rp-border) !important;
    color: var(--rp-text) !important;
}

[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploaderDropzoneInstructions"] {
    color: var(--rp-muted) !important;
}

.chat-container {
    max-width: 900px;
    margin: auto;
}

.user-message {
    background-color: var(--rp-user-bg);
    color: var(--rp-text);
    padding: 14px 16px;
    border-radius: 10px;
    margin: 10px 0 10px auto;
    width: fit-content;
    max-width: 70%;
    text-align: left;
    border: 1px solid color-mix(in srgb, var(--rp-accent) 35%, transparent);
    box-shadow: 0 10px 28px var(--rp-shadow);
    line-height: 1.55;
}

.bot-message {
    background-color: var(--rp-assistant-bg);
    color: var(--rp-text);
    padding: 14px 16px;
    border-radius: 10px;
    margin: 10px auto 10px 0;
    width: fit-content;
    max-width: 75%;
    text-align: left;
    border: 1px solid var(--rp-border);
    box-shadow: 0 10px 28px var(--rp-shadow);
    line-height: 1.6;
}

.source-box {
    background-color: var(--rp-source-bg);
    color: var(--rp-muted);
    padding: 10px 12px;
    border-radius: 8px;
    font-size: 13px;
    margin-top: 8px;
    border: 1px solid var(--rp-border);
    max-width: 75%;
    line-height: 1.45;
}

.user-message b,
.bot-message b,
.source-box b {
    color: var(--rp-text);
}

[data-testid="stAlert"] {
    background-color: var(--rp-panel) !important;
    color: var(--rp-text) !important;
    border: 1px solid var(--rp-border) !important;
}

[data-testid="stAlert"] div,
[data-testid="stAlert"] p {
    color: var(--rp-text) !important;
}

hr {
    border-color: var(--rp-border) !important;
}

@media (max-width: 720px) {
    .main .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .user-message,
    .bot-message,
    .source-box {
        max-width: 100%;
    }
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
