import dspy
import modules.signatures as signatures
import utils.messaging as messaging
import services.tools as tools


def attendant(user_msg):
    chat = dspy.ReAct(
        signature=signatures.Attendant,
        tools=[dspy.Tool(tool) for tool in [tools.calutator, tools.get_time]],
    )

    response = chat(user_msg=user_msg)

    messaging.sendMsg(response.answer)
