#!/usr/bin/python -u

import re, sys
from collections import OrderedDict

preamble = '''
import random
import sys

'''

faceRepMap = OrderedDict({
	':P' : 'print ',
	':p' : 'sys.stdout.write(str(\\1))',
	'(?_?)' : 'if \\1:',
	'(!_?)' : 'elif \\1:',
	'(!_!)' : 'else:',
	'._.' : '.',
	',_,' : ',',
	'( -_-)' : 'try:',
	'( O_O)' : 'except:',
	'(;-_-)' : 'finally:',
	'( \')3' : 'def \\1 :', 			# I know, these don't
	'(@_@)' : 'for i in \\1 :', 		#  make any sense
	'*_*' : '*',
	'+_+' : '+',
	'%_%' : '%',
	'^_^' : '**',
	':\\/' : '/',
	'>_>' : '>',
	'<_<' : '<',
	'=_=' : '==',
	'>_<' : '!=',
	'(:' : '(',
	':)' : ')',
	'[:' : '[',
	':]' : ']',
	'{:' : '{',
	':}' : '}',
	':-)' : 'True',
	':-(' : 'False',
	':|' : 'or',
	':&' : 'and',
	':!' : 'not',
	'=>' : ':',
	'(#)' : 'random.random()',
	':=' : '=',
	'(>")>' : 'return ',
	'(^-^)/' : 'exit(\\1)',
	'\\(>o<)/' : 'raise Exception(\\1)'
})

faceRepMap['-_-'] = '-' 			# ensure this will be done last

def run(fileName='example.emo'):
	raw = preamble + open(fileName).read()
	raw = re.sub(':X.*', '', raw) 			# Strip comments
	raw = re.sub(':-([A-z]+)', '\\1', raw)	# Substitute identifiers
	for face, repl in faceRepMap.items():	# Substitute operators, etc.
		if '\\1' in repl:
			regex = re.escape(face) + '(.*)'
			raw = re.sub(regex, repl, raw)
		else:
			raw = raw.replace(face, repl)
	exec raw

if len(sys.argv) > 1:
	run(sys.argv[1])
