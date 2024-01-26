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
from rasa_sdk.events import UserUtteranceReverted
from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import re

class ActionSetJanEmail(Action):
	def name(self) -> Text:
		return "action_set_jan_email"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		jan_email = 'jankompatscher@gmail.com'

		return [SlotSet("jan_email", jan_email)]
	
class ActionDefaultFallback(Action):
	def name(self) -> Text:
		return "action_default_fallback"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		dispatcher.utter_message(template="utter_default")

		return [UserUtteranceReverted()]
	
programming_languages_dictionary = {
	'python': 'a lot of experience',
	'java': 'intermediate skills',
	'c++': 'intermediate skills',
	'c': 'basic ecperience',
	'c#': 'intermediate skills',
	'javascript': 'a lot of experience',
	'typescript': 'intermediate skills',
	'AL': 'exceptional skills',
	'C/AL': 'a lot of experience',
	'SQL': 'a lot of experience',
	'HTML': 'a lot of experience. That is not exactly a programming language though',
	'CSS': 'intermediate skills. That is not exactly a programming language though',
}
class ActionGetSkillProgrammingLanguage(Action):
	def name(self):
		return 'action_get_skill_programming_language'


	def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		skill = tracker.get_slot("skill_programming_language")
		SlotSet("skill_programming_language", skill)

		skill = skill.lower()
		programming_languages_dictionary_lower = {k.lower(): v for k, v in programming_languages_dictionary.items()}
		if skill in programming_languages_dictionary_lower.keys():
			skill_level = programming_languages_dictionary_lower[skill]
		else:
			skill_level = "no experience yet"
		return[SlotSet("skill_level", skill_level)]
	
class ActionGetSkills(Action):
	def name(self) -> Text:
		return 'action_get_skills'
	
	def run(seld, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		all_skills = ', '.join(programming_languages_dictionary.keys())
		return[SlotSet("skill_programming_languages", all_skills)]