from application.agents.classic_agent import ClassicAgent
from application.agents.react_agent import ReActAgent
import logging

logger = logging.getLogger(__name__)


class AgentCreator:
    agents = {
        "classic": ClassicAgent,
        "react": ReActAgent,
    }

    @classmethod
    def create_agent(cls, type, *args, **kwargs):
        agent_class = cls.agents.get(type.lower())
        if not agent_class:
            raise ValueError(f"No agent class found for type {type}")
        
        # Remove gpt_model from kwargs so it isn't passed to constructors
        # that don't accept it, but preserve it as an attribute on the
        # created agent instance so callers/tests can access it.
        gpt_model = kwargs.pop("gpt_model", None)
        agent = agent_class(*args, **kwargs)
        if gpt_model is not None:
            setattr(agent, "gpt_model", gpt_model)
        return agent
