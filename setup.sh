#The code in this file is base upon How to Deploy a Streamlit App with Heroku by Jack Smart
#https://medium.com/analytics-vidhya/how-to-deploy-a-streamlit-app-with-heroku-5f76a809ec2e

mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"blant.jesse@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml