# HTML Template for styling the chat UI in Streamlit
css = '''
<style>
    .chat-message {
        padding: 1rem 1.5rem; 
        border-radius: 10px; 
        margin-bottom: 1rem; 
        display: flex;
        align-items: flex-start;
        max-width: 80%;
        box-sizing: border-box;
    }

    .chat-message.user {
        background-color: #2b313e;
        margin-left: auto;
    }

    .chat-message.bot {
        background-color: #475063;
        margin-right: auto;
    }

    .chat-message .avatar {
        width: 20%;
    }

    .chat-message .avatar img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        object-fit: cover;
        margin-right: 1rem;
    }

    .chat-message .message {
        width: 80%;
        padding: 0.8rem;
        color: #fff;
        font-size: 16px;
        line-height: 1.5;
        word-wrap: break-word;
    }

    /* Adding hover effect for user and bot messages */
    .chat-message:hover {
        opacity: 0.9;
    }
</style>
'''

# Template for bot message styling
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

# Template for user message styling
user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/zTG7Krv8/chat-user-img.jpg" alt="User Avatar">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
