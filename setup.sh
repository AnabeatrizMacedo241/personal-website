mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor = '#0056b3'\n\
backgroundColor = '#ffffff'\n\
secondaryBackgroundColor = '#f9f9f9'\n\
textColor = '#333'\n\
" > ~/.streamlit/config.toml