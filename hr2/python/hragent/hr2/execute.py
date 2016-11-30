import json
import slate
from resume import Resume
resume_rules_file = open("resume_rules.json","r")
resume_rules_native = resume_rules_file.read()
resume_rules_file.close()
resume_rules = json.loads(resume_rules_native)
headers = resume_rules["headers"]
with open('input/Resume.pdf','r') as f:
	doc = slate.PDF(f)
DOCUMENT_PARSER = dict()
for _h in headers:
	DOCUMENT_PARSER[resume_rules["aliases"][_h]]=list()		
candidate = dict()
r = Resume(DOCUMENT_PARSER, doc, resume_rules)
r.parseResume()
final_resume = r.getJson()