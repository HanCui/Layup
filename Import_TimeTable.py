from bs4 import BeautifulSoup
import requests
import logging

class TimetableService:

    #def __init__(self, request_storage_service):
        #self.request_storage_service = request_storage_service

    def get_course_data(self, course_request):
        """
        Post request to timetable, then parse html
        :param course_request:
        :return:
        """

        # get page source and create parser
        logging.info("Making POST request for " + str(course_request))
        search_results = requests.post('http://oracle-www.dartmouth.edu/dart/groucho/timetable.display_courses',
                             data= {'distribradio': "alldistribs"
                                    'depts': "no_value"
                                    'periods': "no_value"
                                    'distribs:' "no_value"
                                    'distribs_i': 'no_value'
                                    'distribs_wc': 'no_value'
                                    'pmode': 'public'
                                    'term':
                                    'levl':
                                    'fys': 'n'
                                    'wrt': 'n'
                                    'pe': 'n'
                                    'review': 'n'
                                    'crnl': 'no_value'
                                    'classyear': '2008'
                                    'searchtype': 'Subject + Area%28s%29'
                                    'termradio': 'allterms'
                                    'terms': 'no_value'
                                    'subjectradio': 'allsubjects
                                    'hoursradio': 'allhours'
                                    'sortorder': 'dept'}


        soup = BeautifulSoup(search_results, 'html.parser')
        row_data = soup.find("div", {"class": "data-table"}).tr
        column_names = [th.text.encode('ascii', 'ignore') for th in row_data.find_all('th')]

        # get table data (mainly column names)
        column_name_to_index = {}
        for index, name in enumerate(column_names):
                column_name_to_index[index] = name

        row_data = row_data.next_sibling.next_sibling.next_sibling.next_sibling

        # parse row data, store in dictionary
        while row_data:
            td_list = row_data.find_all('td')
            course_data = {}

            for index, data in enumerate(td_list):
                course_data[column_name_to_index[index]] = data.text.encode('ascii', 'ignore')

            big_ass_course_table.add(course_data)

            row_data = row_data.next_sibling.next_sibling
        
        return big_ass_course_table 
        #logging.info("Could not find course. Removing from watch list")
        #self.request_storage_service.remove(course_request)
        #return None
