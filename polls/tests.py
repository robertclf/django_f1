# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import datetime

from django.utils import timezone
from django.urls import reverse

from .models import Question

# Selenium

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

class QuestionModelTests(TestCase):
	"""
	Class to test Question Model.
	"""

	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() returns False from questions whose pub_date
		is in the future.
		"""

		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date = time)

		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""	
		was_published_recently() returns False for questions whose pub_date
		is older than 1 day.
		"""
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		was_published_recently() returns True for questions whose pub_date
		is within the last day.
		"""
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
	"""
	Create a question with the given `question_text` and published the
	given number of `days` offset to now (negative for questions published
	in the past, positive for questions that have yet to be published).
	"""

	time = timezone.now() + datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
	"""
	Class to test Index Views.
	"""

	def test_no_questions(self):
		"""
		If no question exist, an appropiate message is displayed.
		"""
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'],[])

	def test_past_question(self):
		"""
		Questions with a pub_date in the past are displayed on the index page.
		"""

		create_question(question_text="Past question.", days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past question.>'])

	def test_future_question(self):
		"""
		Questions with a pub_Date in the future aren't displayed on the index page.
		"""

		create_question(question_text="Future question.", days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, "No polls are available.")
		self.assertQuerysetEqual(response.context['latest_question_list'],[])

	def test_future_question_and_test_past_question(self):
		"""
		Even if both past and future questions exist, only past questions
		are displayed.
		"""
		create_question(question_text="Past question.", days=-30)
		create_question(question_text="Future question.", days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

	def test_two_past_questions(self):
		"""
		The questions index page may display multiple questions.
		"""
		create_question(question_text="Past question 1.", days=-30)
		create_question(question_text="Past question 2.", days=-5)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],
			['<Question: Past question 2.>','<Question: Past question 1.>'])

class QuestionDetailViewTests(TestCase):
	"""
	Class to test Detail Views.
	"""

	def test_future_question(self):
		"""
		The detail view of a question with a pub_date in the future returns
		a 404 not found.
		"""
		future_question = create_question(question_text='Future question.', days=5)
		url = reverse('polls:detail', args=(future_question.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)

	def test_past_question(self):
		"""
		The detail view of a question with a pub_Date in the past 
		displays the question's text.
		"""
		past_question = create_question(question_text='Past question.', days=-5)
		url = reverse('polls:detail', args=(past_question.id,))
		response = self.client.get(url)
		self.assertContains(response, past_question.question_text)


class VoteTestCase(LiveServerTestCase):
    """
    Selenium vote tests 
    """

    def setUp(self):
        """
        Setting up Selenium tests.
        """

        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()
        self.selenium = webdriver.Firefox()
        super(VoteTestCase, self).setUp()

    def tearDown(self):
        """
        Shutting down Selenium tests.
        """

        self.selenium.quit()
        self.display.stop()
        super(VoteTestCase, self).tearDown()

    def test_vote(self):
        selenium = self.selenium
        selenium.get('http://localhost/django01/polls/2/')

        choice2 = selenium.find_element_by_id('choice2')
        choice2.click()

        #first_name.send_keys('Yusuf')

        #submit = selenium.find_element_by_name('register')
        submit = selenium.find_element_by_id('btnSubmit')

        submit.send_keys(Keys.RETURN)

        selenium.get('http://localhost/django01/polls/2/results/')
        
        assert 'Vote again?' in selenium.page_source





