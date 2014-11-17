"HSH" is a python extension developed by Sanhe. Many useful standard library and 3rd party extension are repacked by functionaility. Then it is way more easier to keep focus on development rather than wasting time on writing tools.

prerequisition:
	requests 2.3.0
	psycopg2 2.5.4

|--- Data (Collection of miscellaneous to process data)
	|--- js.py (json utility) py2,3
	|--- iterable.py (high performance iterator recipes) py2,3
	|--- hsh_hashlib.py (hash everything, string, object and file) py2,3

|--- DBA (Database management gadget in sqlite3, postgres, mysql)

|--- LinearSpider (Linear web crawler framework)
	|--- crawler.py (http utility, repack of requests 2.3.0) py2,3
	|--- logger.py (exception information log handler) py2,3
	
|--- RobotHand (mouse, keyboard action simulator)

unit test:
	all the unit test should not be done inside the module.py it self.
	all the unit test is locate at the project directory, which is the parent directory of package dir

Compatible:
	

