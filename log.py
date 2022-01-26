def log_message(message):
    with open('logs.txt','a') as f:
        f.write(str(message)+'\n')
