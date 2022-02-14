from GPA_Calc import GPA_Calc
from IOption import IOption

c = GPA_Calc()
currentState: IOption = c
def next_handler(pm):
    print("next_handler:", pm)
    msg_text = pm.text
    rsp = currentState.runIt(msg_text)
    bot.send_message(pm.chat.id, rsp)
    if currentState.setup.get('rerun', ''):
        bot.register_next_step_handler(pm, next_handler)  # Next message will call the name_handler function


def runIt(message):
    # sent_msg = bot.send_message(message.chat.id, currentState.setup.get('message', ''))
    print(currentState.setup.get('message', ''))
    if currentState.setup.get('input', ''):
        next_handler()  # Next message will call the name_handler function
    else:
        rsp = currentState.runIt()
        bot.send_message(message.chat.id, rsp)
