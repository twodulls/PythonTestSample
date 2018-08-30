# _*_ coding: utf-8 _*_

def logger(msg):

	def log_message():
		print('Log: ', msg)

	return log_message

log_hi = logger('Hi')
print(log_hi)
log_hi()

del logger
