import falcon
import json
import random
import string
import MySQLdb
import settings
from passlib.hash import md5_crypt

conn = MySQLdb.connect(**settings.dbconfig)
cursor = conn.cursor()
cursor.execute('SET NAMES UTF8')

class SetEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, set):
			return list(obj)
		return json.JSONEncoder.default(self, obj)


class UserResource(object):
	# Returns user info
	def on_get(self, req, resp):
		cookies = req.cookies
		if 'sessiontoken' in cookies:
			cookieValue = cookies['sessiontoken']
			cursor.execute('''SELECT email,exp_date FROM users where sessiontoken = ?''', [cookieValue])
			row = cursor.fetchone()
			if (row == None):
				doc = { 'Please sign in' }
			else:
				doc = { row }
		else: doc = { 'no cookie value' }
		resp.body = json.dumps(doc, cls=SetEncoder)


	# Add User
	def on_post(self, req, resp):
		phone = req.get_param('phone')
		pwd = req.get_param('pwd')
		email = req.get_param('email')
		print phone
		print pwd
		print email


		if (phone == None or pwd == None):
			doc = {
				'You did not enter a valid phone and password please try again'
			}
		else:
			passhash = md5_crypt.encrypt(pwd)
			cursor.execute('''INSERT INTO users(phone, pwd, email, sessiontoken)
				VALUES(?,?,?,'')''', (phone, passhash, email))
			doc = { 'Updated' }
		resp.body = json.dumps(doc, cls=SetEncoder)

class UserPutResource(object):
	# Updates info 
	def on_post(self, req, resp):
		newemail = req.get_param('email')
		cookies = req.cookies
		if 'sessiontoken' in cookies:
			cookieValue = cookies['sessiontoken']
			cursor.execute('''SELECT email FROM users WHERE sessiontoken = ?''', [cookieValue])
			row = cursor.fetchone()
			if (row == None):
				doc = { 'Please sign in' }
			else:
				cursor.execute('''UPDATE users SET email = ? WHERE sessiontoken = ?''', 
					(newemail, cookieValue))
				db.commit()
				doc = { 'Updated email' }
		else: doc = { 'no cookie value' }
		resp.body = json.dumps(doc, cls=SetEncoder)

class UserDeleteResource(object):
	# Deletes user
	def on_get(self, req, resp):
		cookies = req.cookies
		if 'sessiontoken' in cookies:
			cookieValue = cookies['sessiontoken']
			cursor.execute('''SELECT * FROM users WHERE sessiontoken = ?''', [cookieValue])
			row = cursor.fetchone()
			if (row == None):
				doc = { 'Please sign in' }
			else: 
				cursor.execute('''DELETE FROM users WHERE sessiontoken = ?''', [cookieValue])
				resp.unset_cookie('sessiontoken')
				doc = { 'Deleted user' }
		else: doc = { 'no cookie value' }
		resp.body = json.dumps(doc, cls=SetEncoder)

class AuthResource(object):
	# Gets Session Token
	def on_post(self, req, resp):
		phone = req.get_param('phone')
		pwd = req.get_param('pwd')

		if (phone == None or pwd == None):
			doc = { 'Please try again' }
		else:
			cursor.execute('''SELECT pwd FROM users WHERE phone = ?''', [phone])
			row = cursor.fetchone()
			if (row == None):
				doc = { 'Invalid phone and pwd' }
			else:
				if (md5_crypt.verify(pwd, row[0])):
					cookie = ''.join(random.SystemRandom().choice(string.ascii_uppercase + 
						string.digits) for _ in range(6))
					resp.set_cookie('sessiontoken', cookie, domain='.localhost', secure = False)
					cursor.execute('''UPDATE users SET sessiontoken = ? WHERE phone = ?''', 
						(cookie, phone))
					db.commit()
					doc = { 'Session Started' }
				else: doc = { 'Wrong pwd' }
		resp.body = json.dumps(doc, cls=SetEncoder)

class AuthDeleteResource(object):
	# Delete Session Token
	def on_get(self, req, resp):
		cookies = req.cookies
		if 'sessiontoken' in cookies:
			cookieValue = cookies['sessiontoken']
			cursor.execute('''UPDATE users SET sessiontoken = Null WHERE sessiontoken = ?''',
				[cookieValue])
			resp.unset_cookie('sessiontoken')
			doc = { 'Unset Token' }
		else: doc = { 'no cookie value' }
		resp.body = json.dumps(doc, cls=SetEncoder)
