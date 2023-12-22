# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import re

class ActionGetSkillProgrammingLanguage(Action):
	def name(self):
		return 'action_get_skill_programming_language'

	@staticmethod
	def skill_db() -> Dict[Text, Text]:
		programming_languages_dictionary = {
			'python': 'very good',
			'java': 'good',
			'c++': 'good',
			'c': 'basic',
			'c#': 'good',
			'javascript': 'very good',
			'typescript': 'good',
			'AL': 'exceptional',
			'C/AL': 'very good',
			'SQL': 'very good',
			'HTML': 'very good, not a programming language though',
			'CSS': 'good, not a programming language though',
			}
		return programming_languages_dictionary

	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		skill = tracker.get_slot("skill_programming_language")
		SlotSet("skill_programming_language", skill)
		programming_languages_dictionary = self.skill_db()
		if skill is None:
			all_skills = ', '.join(programming_languages_dictionary.keys())
			return [SlotSet("skill_programming_languages", all_skills)]

		skill = skill.lower()  # Convert to lowercase after checking if it's None
		if skill in programming_languages_dictionary.keys():
			skill_level = programming_languages_dictionary[skill]
		else:
			skill_level = "no experience yet"
		return[SlotSet("skill_level", skill_level)]