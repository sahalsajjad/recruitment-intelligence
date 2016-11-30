class Resume:
	def __init__(self,EMPTY_DOCUMENT_PARSER, resume_text, json_rules):
		self.DOCUMENT = EMPTY_DOCUMENT_PARSER
		self.candidate = dict()
		self.score = 0.0
		self.rank = 0.0
		text = ''
		for x in resume_text:
			text+=x
		self.resume = text.split('\n\n')
		self.resume = filter(lambda a: a != '', self.resume)
		self.json_rules = json_rules
		pass
	def getJSON(self):
		json_obj = {"candidate":self.candidate, "resume":self.DOCUMENT}
		return json_obj	
	def parseResume(self):
		COLLECTOR = list()
		key = None
		start = 0
		headers = map(str,  self.json_rules["headers"])
		for x in xrange(start, len(self.resume)):
			if str(self.resume[x].lower().replace(' ','_').replace(':','').strip('\n').strip()) in headers:
				start = x
				break
			else:
				COLLECTOR.append(self.resume[x])	
		self.candidate = COLLECTOR
		for x in xrange(start, len(self.resume)):
			if str(self.resume[x].lower().replace(' ','_').replace(':','').strip('\n').strip()) in headers:
				key = str(self.resume[x].replace(' ','_').replace(':','').strip('\n').strip().lower())
			elif key != None:	
				pass
				self.DOCUMENT[self.json_rules["aliases"][key]].append(str(self.resume[x]).replace('\xe2\x80\x94','-'))
		
		


