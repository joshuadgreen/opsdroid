"""Decorator functions to use when creating skill modules."""

import logging

from opsdroid.const import REGEX_PARSE_SCORE_FACTOR
from opsdroid.helper import add_skill_attributes

_LOGGER = logging.getLogger(__name__)


def match_event(event_type):
    """Return event type matcher.

    Decorator that calls skill based on passed event_type.

    Args:
        event_type (str): opsdroidstarted, message, typing, reaction, file, image
    Returns:
        Decorated function

    """

    def matcher(func):
        """Add decorated function to list for event matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"event_type": {"type": event_type}})
        return func

    return matcher


def match_regex(
    regex, case_sensitive=True, matching_condition="match", score_factor=None
):
    """Return regex match decorator.

    Decorator used to handle regex matching in skills. Decorated function will be called if regex
    string matches. Matching can be customized based on the matching condition passed.

    Args:
        regex (str): Regex expression as a string.
        case_sensitive (bool): Flag to check for case sensitive matching, defaults to True.
        matching_condition (str): Type of matching to be applied, can be "search", "match" or
            "fullmatch"
        score_factor (float): Score multiplier used by Rasa NLU skills

    Returns:
        Decorated function

    """

    def matcher(func):
        """Add decorated function to skills list for regex matching."""
        func = add_skill_attributes(func)
        func.matchers.append(
            {
                "regex": {
                    "expression": regex,
                    "case_sensitive": case_sensitive,
                    "matching_condition": matching_condition,
                    "score_factor": score_factor or REGEX_PARSE_SCORE_FACTOR,
                }
            }
        )
        return func

    return matcher


def match_parse(
    format_str, case_sensitive=True, matching_condition="match", score_factor=None
):
    """Return parse match decorator.

    Decorator that matches the message from the user against a string with python format syntax.
    If the string matches then the function is called. matching_condition can be set to customize
    if string match should match format_str only at the beginning of input string or match in the
    first location where format_str is found.

    Args:
        format_str (str): A python format string to be matched.
        case_sensitive (bool):  Boolean flag to check if matching should be case sensitive.
        matching_condition (str): Type of matching to be applied, can be "match" or "search"
        score_factor (float): Score multiplier used by Rasa NLU skills

    Returns:
        Decorated function

    """

    def matcher(func):
        """Add decorated function to skills list for parse matching."""
        func = add_skill_attributes(func)
        func.matchers.append(
            {
                "parse_format": {
                    "expression": format_str,
                    "case_sensitive": case_sensitive,
                    "matching_condition": matching_condition,
                    "score_factor": score_factor or REGEX_PARSE_SCORE_FACTOR,
                }
            }
        )
        return func

    return matcher


def match_dialogflow_action(action):
    """Return Dialogflow action match decorator."""

    def matcher(func):
        """Add decorated function to skills list for Dialogflow matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"dialogflow_action": action})
        return func

    return matcher


def match_dialogflow_intent(intent):
    """Return Dialogflow intent match decorator."""

    def matcher(func):
        """Add decorated function to skills list for Dialogflow matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"dialogflow_intent": intent})
        return func

    return matcher


def match_luisai_intent(intent):
    """Return luisai intent match decorator."""

    def matcher(func):
        """Add decorated function to skills list for luisai matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"luisai_intent": intent})
        return func

    return matcher


def match_rasanlu(intent):
    """Return Rasa NLU intent match decorator."""

    def matcher(func):
        """Add decorated function to skills list for Rasa NLU matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"rasanlu_intent": intent})
        return func

    return matcher


def match_recastai(intent):
    """Return recastai intent match decorator."""

    def matcher(func):
        """Add decorated function to skills list for recastai matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"sapcai_intent": intent})
        return func

    _LOGGER.warning(
        _(
            "Recast.AI is now called SAP Conversational AI, "
            "this matcher  will stop working in the future. "
            "Use match_sapcai instead."
        )
    )
    return matcher


def match_sapcai(intent):
    """Return SAP Conversational AI intent match decorator."""

    def matcher(func):
        """Add decorated function to skills list for SAPCAI matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"sapcai_intent": intent})
        return func

    return matcher


def match_watson(intent):
    """Return watson intent match decorator."""

    def matcher(func):
        """Add decorated function to skills list for watson matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"watson_intent": intent})
        return func

    return matcher


def match_witai(intent):
    """Return witai intent match decorator."""

    def matcher(func):
        """Add decorated function to skills list for witai matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"witai_intent": intent})
        return func

    return matcher


def match_crontab(crontab, timezone=None):
    """Return crontab match decorator."""

    def matcher(func):
        """Add decorated function to skills list for crontab matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"crontab": crontab, "timezone": timezone})
        return func

    return matcher


def match_webhook(webhook):
    """Return webhook match decorator."""

    def matcher(func):
        """Add decorated function to skills list for webhook matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"webhook": webhook})

        return func

    return matcher


def match_always(func=None):
    """Return always match decorator."""

    def matcher(func):
        """Add decorated function to skills list for always matching."""
        func = add_skill_attributes(func)
        func.matchers.append({"always": True})
        return func

    # Allow for decorator with or without parenthesis as there are no args.
    if callable(func):
        return matcher(func)
    return matcher
